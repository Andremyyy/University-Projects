package Repository;

import Domain.Cake;
import Domain.Order;
import Exceptions.RepositoryException;
import org.sqlite.SQLiteDataSource;

import java.sql.*;
import java.util.Date;
import java.util.*;


public class SQLOrderRepository extends MemoryRepository<Order> implements AutoCloseable {

    private Connection connection = null;
    private static final String DB_URL = "jdbc:sqlite:D:/MAP/a4-Andremyyy/src/Repository/orders";

    public SQLOrderRepository() {
        openConnection();
        createTables();
        loadData();
    }

    private void createTables() {
        try {
            Statement statement = connection.createStatement();
            // Create `orders` table
            String ordersTable = """
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    date DATE
                );
                """;
            statement.execute(ordersTable);

            // Create `order_cakes` table for the relationship between orders and cakes
            String orderCakesTable = """
                CREATE TABLE IF NOT EXISTS order_cakes (
                    order_id INTEGER,
                    cake_id INTEGER,
                    PRIMARY KEY (order_id, cake_id),
                    FOREIGN KEY (order_id) REFERENCES orders(id),
                    FOREIGN KEY (cake_id) REFERENCES cakes(id)
                );
                """;
            statement.execute(orderCakesTable);

            System.out.println("Tables created successfully.");
        } catch (SQLException e) {
            System.out.println("Error creating tables: " + e.getMessage());
        }
    }

    private void openConnection() {
        try {
            SQLiteDataSource dataSource = new SQLiteDataSource();
            dataSource.setUrl(DB_URL);

            if (connection == null || connection.isClosed()) {
                connection = dataSource.getConnection();
            }
        } catch (SQLException e) {
            System.out.println("Error while creating the connection: " + e.getMessage());
        }
    }

    // o metodă pentru a genera 100 de comenzi aleatorii
    public void generateRandomOrders(int count) {

        Random rand = new Random();
        int id = 3000;

        // toate torturile
        List<Cake> allCakes = new SQLCakeRepository().getEntities();

        for (int i = 0; i < count; i++) {
            // generez o data aleatorie intre 2023-01-01 si data actuala
            Calendar calendar = Calendar.getInstance();

            // data minima = 2023-01-01
            calendar.set(2023, Calendar.JANUARY, 1); // 2023-01-01
            long minTime = calendar.getTimeInMillis();

            // data maxima = data curenta
            long maxTime = System.currentTimeMillis();

            // generez o data aleatorie intre data minima si data maxima
            long randomTime = minTime + (long) (rand.nextDouble() * (maxTime - minTime));


            Date orderDate = new Date(randomTime);

            Order order = new Order(id++, new ArrayList<>(), orderDate);

            // adaug torturi aleatorii (intre 1 si 4 torturi per comanda)
            int numberOfCakes = rand.nextInt(4) + 1;
            for (int j = 0; j < numberOfCakes; j++) {
                Cake randomCake = allCakes.get(rand.nextInt(allCakes.size()));
                order.getCakes().add(randomCake);
            }

            try {
                add(order); // salvează comanda în baza de date
            } catch (RepositoryException e) {
                System.out.println("Failed to add order: " + e.getMessage());
            }
        }
    }



    private void loadData() {
        List<Order> orders = getEntities();
        System.out.println("Found " + orders.size() + " orders in the database.");
        entities.addAll(orders);
    }

    @Override
    public void add(Order order) throws RepositoryException {
        super.add(order);
        String insertOrder = "INSERT INTO orders (id, date) VALUES (?, ?);";
        String insertOrderCakes = "INSERT INTO order_cakes (order_id, cake_id) VALUES (?, ?);";

        try (PreparedStatement orderStatement = connection.prepareStatement(insertOrder);
             PreparedStatement orderCakesStatement = connection.prepareStatement(insertOrderCakes)) {

            // Insert order
            orderStatement.setInt(1, order.getId());
            orderStatement.setDate(2, new java.sql.Date(order.getDate().getTime()));
            orderStatement.executeUpdate();

            // Insert cakes related to the order
            for (Cake cake : order.getCakes()) {
                orderCakesStatement.setInt(1, order.getId());
                orderCakesStatement.setInt(2, cake.getId());
                orderCakesStatement.executeUpdate();
            }

        } catch (SQLException e) {
            throw new RepositoryException("Error adding order: " + e.getMessage());
        }
    }

    @Override
    public void removeById(int id) throws RepositoryException {
        super.removeById(id);
        String deleteOrder = "DELETE FROM orders WHERE id = ?;";
        String deleteOrderCakes = "DELETE FROM order_cakes WHERE order_id = ?;";

        try (PreparedStatement orderCakesStatement = connection.prepareStatement(deleteOrderCakes);
             PreparedStatement orderStatement = connection.prepareStatement(deleteOrder)) {

            // Delete order_cakes entries
            orderCakesStatement.setInt(1, id);
            orderCakesStatement.executeUpdate();

            // Delete order entry
            orderStatement.setInt(1, id);
            orderStatement.executeUpdate();

        } catch (SQLException e) {
            throw new RepositoryException("Error removing order: " + e.getMessage());
        }
    }

    @Override
    public ArrayList<Order> getEntities() {
        ArrayList<Order> orders = new ArrayList<>();
        String selectOrders = "SELECT * FROM orders;";
        String selectOrderCakes = "SELECT cake_id FROM order_cakes WHERE order_id = ?;";

        try (PreparedStatement ordersStatement = connection.prepareStatement(selectOrders);
             PreparedStatement orderCakesStatement = connection.prepareStatement(selectOrderCakes)) {

            ResultSet ordersResult = ordersStatement.executeQuery();
            while (ordersResult.next()) {
                int orderId = ordersResult.getInt("id");
                Date date = ordersResult.getDate("date");

                // Get cakes for this order
                orderCakesStatement.setInt(1, orderId);
                ResultSet cakesResult = orderCakesStatement.executeQuery();
                ArrayList<Cake> cakes = new ArrayList<>();
                while (cakesResult.next()) {
                    int cakeId = cakesResult.getInt("cake_id");
                    cakes.add(new Cake(cakeId, "")); // Retrieve cake type if needed
                }

                // Add the order to the list
                orders.add(new Order(orderId, cakes, date));
            }

        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving orders: " + e.getMessage(), e);
        }

        return orders;
    }

    @Override
    public Order getEntityById(int id) {
        String selectOrder = "SELECT * FROM orders WHERE id = ?;";
        String selectOrderCakes = "SELECT cake_id FROM order_cakes WHERE order_id = ?;";

        try (PreparedStatement orderStatement = connection.prepareStatement(selectOrder);
             PreparedStatement orderCakesStatement = connection.prepareStatement(selectOrderCakes)) {

            orderStatement.setInt(1, id);
            ResultSet orderResult = orderStatement.executeQuery();

            if (orderResult.next()) {
                Date date = orderResult.getDate("date");

                // Get cakes for this order
                orderCakesStatement.setInt(1, id);
                ResultSet cakesResult = orderCakesStatement.executeQuery();
                ArrayList<Cake> cakes = new ArrayList<>();
                while (cakesResult.next()) {
                    int cakeId = cakesResult.getInt("cake_id");
                    cakes.add(new Cake(cakeId, "")); // Retrieve cake type if needed
                }

                return new Order(id, cakes, date);
            } else {
                return null; // nu exista comanda
            }

        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving order with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public boolean findById(int id) {
        String query = "SELECT 1 FROM orders WHERE id = ?;";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next();
        } catch (SQLException e) {
            throw new RuntimeException("Error checking order existence with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public void update(Order order) throws RepositoryException {
        String updateOrder = "UPDATE orders SET date = ? WHERE id = ?;";
        String deleteOrderCakes = "DELETE FROM order_cakes WHERE order_id = ?;";
        String insertOrderCakes = "INSERT INTO order_cakes (order_id, cake_id) VALUES (?, ?);";

        try (PreparedStatement updateOrderStatement = connection.prepareStatement(updateOrder);
             PreparedStatement deleteOrderCakesStatement = connection.prepareStatement(deleteOrderCakes);
             PreparedStatement insertOrderCakesStatement = connection.prepareStatement(insertOrderCakes)) {

            // Update comanda
            updateOrderStatement.setDate(1, new java.sql.Date(order.getDate().getTime()));
            updateOrderStatement.setInt(2, order.getId());
            updateOrderStatement.executeUpdate();

            // sterg torturile comenzii pe care vreau sa o anulez
            deleteOrderCakesStatement.setInt(1, order.getId());
            deleteOrderCakesStatement.executeUpdate();

            // adaug torturi noi
            for (Cake cake : order.getCakes()) {
                insertOrderCakesStatement.setInt(1, order.getId());
                insertOrderCakesStatement.setInt(2, cake.getId());
                insertOrderCakesStatement.executeUpdate();
            }

        } catch (SQLException e) {
            throw new RepositoryException("Error updating order: " + e.getMessage());
        }
    }

    @Override
    public void close() {
        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
