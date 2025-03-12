package UI;

import Domain.*;
import Exceptions.RepositoryException;
import Repository.*;
import Service.CakeService;
import Service.OrderService;
import util.Settings;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;



public class MainMenu {
    public static void runCli() throws RepositoryException {
        Scanner scanner = new Scanner(System.in);

        IDGenerator idGenerator = new IDGenerator("last_id.txt");

        String repoType = Settings.getInstance().getRepoType();
        String cakeFileName = Settings.getInstance().getCakeFileName();
        String orderFileName = Settings.getInstance().getOrderFileName();


        AbstractRepository<Cake> cakeRepo = createRepository(repoType, cakeFileName, new CakeConverter(Cake.class));
        AbstractRepository<Order> orderRepo = createRepository(repoType, orderFileName, new OrderConvertor(Order.class));

        if (cakeRepo == null || orderRepo == null) {
            System.out.println("Error in the settings file!");
            return;
        }

        if (repoType.equals("sql") && cakeRepo instanceof SQLCakeRepository) {
            SQLCakeRepository sqlCakeRepo = (SQLCakeRepository) cakeRepo;

            // Verificăm câte entități sunt deja în baza de date
            int existingCakes = sqlCakeRepo.getEntities().size();
            if (existingCakes < 100) {
                int cakesToGenerate = 100 - existingCakes;
                sqlCakeRepo.generateRandomCakes(cakesToGenerate);
                System.out.printf("Generated %d random cakes in the database.%n", cakesToGenerate);
            }
        }


        if (repoType.equals("sql") && orderRepo instanceof SQLOrderRepository) {
            SQLOrderRepository sqlOrderRepo = (SQLOrderRepository) orderRepo;

            // Verificăm câte entități sunt deja în baza de date
            int existingOrders = sqlOrderRepo.getEntities().size();
            if (existingOrders < 100) {
                int ordersToGenerate = 100 - existingOrders;
                sqlOrderRepo.generateRandomOrders(ordersToGenerate); // Adjust the count as needed
                System.out.printf("Generated %d random cakes in the database.%n", ordersToGenerate);
            }
        }

        CakeService cakeService = new CakeService(cakeRepo, idGenerator);
        OrderService orderService = new OrderService(orderRepo, idGenerator);
        UI ui = new UI(orderService, cakeService);

        addEntities(cakeRepo, orderRepo, idGenerator);

        boolean running = true;
        System.out.println("Welcome to my pastry's cake order management system!");

        while (running) {
            System.out.println("1. Place a new order");
            System.out.println("2. View all orders");
            System.out.println("3. Cancel an order");
            System.out.println("4. Update an order");
            System.out.println("5. Add a new cake");
            System.out.println("6. View all cakes");
            System.out.println("7. Delete a cake");
            System.out.println("8. Update a cake");
            System.out.println("9. Number of cakes ordered daily");
            System.out.println("10. Number of cakes ordered each month");
            System.out.println("11. Most ordered cakes");
            System.out.println("0. Exit");

            System.out.print("Please select an option (1...11, 0 - stop): ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1 -> UI.placeOrder(scanner);
                case 2 -> UI.viewOrders(scanner);
                case 3 -> UI.cancelOrder(scanner);
                case 4 -> UI.updateOrder(scanner);
                case 5 -> UI.addNewCake(scanner);
                case 6 -> UI.viewCakes(scanner);
                case 7 -> UI.deleteCake(scanner);
                case 8 -> UI.updateCake(scanner);
                case 9 -> UI.getCakesOrderedPerDay(scanner);
                case 10 -> UI.getCakesOrderedPerMonth(scanner);
                case 11 -> UI.getMostOrderedCakes(scanner);
                case 0 -> {
                    System.out.println("Thank you for your input. Goodbye!");
                    running = false;
                }
                default -> System.out.println("Invalid option. Please try again by choosing one of the available options!.");
            }
        }

        scanner.close();
    }

    private static <T extends Entity> AbstractRepository<T> createRepository(String repoType, String fileName, EntityConvertor<T> convertor) throws RepositoryException {
        if (convertor == null) {
            throw new RepositoryException("Convertor cannot be null");
        }
        Class<T> entityClass = convertor.getEntityClass();
        if (entityClass == null) {
            throw new RepositoryException("Entity class cannot be null in convertor");
        }
        return switch (repoType) {
            case "memory" -> new MemoryRepository<>();
            case "text" -> new TextFileRepository<>(fileName, convertor);
            case "binary" -> new BinaryFileRepository<>(fileName);
            case "json" -> new JsonFileRepository<>(fileName, entityClass);
            case "sql" -> {
                if (entityClass.equals(Cake.class)) {
                    yield (AbstractRepository<T>) new SQLCakeRepository();
                } else if (entityClass.equals(Order.class)) {
                    yield (AbstractRepository<T>) new SQLOrderRepository();
                } else {
                    throw new RepositoryException("Unsupported entity type for SQL repository");
                }
            }

            default -> null;
        };
    }

    private static void addEntities(AbstractRepository<Cake> cakeRepo, AbstractRepository<Order> orderRepo, IDGenerator idGenerator) {
        if (cakeRepo.size() == 0) {
            try {
                cakeRepo.add(new Cake(1, "chocolate"));
                cakeRepo.add(new Cake(2, "mango"));
                cakeRepo.add(new Cake(3, "cheesecake"));
                cakeRepo.add(new Cake(4, "oreo"));
                cakeRepo.add(new Cake(5, "banana"));
            } catch (RepositoryException re) {
                System.out.println(re.getMessage());
            }
        }

        if (orderRepo.size() == 0) {
            // for order 1
            ArrayList<Cake> order1 = new ArrayList<>();
            order1.add(cakeRepo.getEntityById(1));
            order1.add(cakeRepo.getEntityById(3));
            order1.add(cakeRepo.getEntityById(4));

            // for order 2
            ArrayList<Cake> order2 = new ArrayList<>();
            order2.add(cakeRepo.getEntityById(2));
            order2.add(cakeRepo.getEntityById(5));

            // for order 3
            ArrayList<Cake> order3 = new ArrayList<>();
            order3.add(cakeRepo.getEntityById(1));

            // for order 4
            ArrayList<Cake> order4 = new ArrayList<>();
            order4.add(cakeRepo.getEntityById(3));
            order4.add(cakeRepo.getEntityById(4));
            order4.add(cakeRepo.getEntityById(2));

            // for order 5
            ArrayList<Cake> order5 = new ArrayList<>();
            order5.add(cakeRepo.getEntityById(1));
            order5.add(cakeRepo.getEntityById(2));
            order5.add(cakeRepo.getEntityById(4));

            try {
                Date orderDate1 = new SimpleDateFormat("yyyy-MM-dd").parse("2024-10-09");
                Date orderDate2 = new SimpleDateFormat("yyyy-MM-dd").parse("2024-04-15");
                Date orderDate3 = new SimpleDateFormat("yyyy-MM-dd").parse("2024-12-15");
                Date orderDate4 = new SimpleDateFormat("yyyy-MM-dd").parse("2024-06-12");
                Date orderDate5 = new SimpleDateFormat("yyyy-MM-dd").parse("2024-02-01");

                orderRepo.add(new Order(idGenerator.generateId(), order1, orderDate1));
                orderRepo.add(new Order(idGenerator.generateId(), order2, orderDate2));
                orderRepo.add(new Order(idGenerator.generateId(), order3, orderDate3));
                orderRepo.add(new Order(idGenerator.generateId(), order4, orderDate4));
                orderRepo.add(new Order(idGenerator.generateId(), order5, orderDate5));

            } catch (RepositoryException re) {
                System.out.println("Error adding orders to the repository: " + re.getMessage());
            } catch (ParseException pe) {
                System.out.println("Invalid date format! Please try again!");
            }
        }
    }
}