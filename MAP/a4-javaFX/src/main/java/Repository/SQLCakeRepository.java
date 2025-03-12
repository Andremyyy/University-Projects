package Repository;

import Domain.Cake;
import Exceptions.RepositoryException;
import com.github.javafaker.Faker;
import org.sqlite.SQLiteDataSource;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

//File -> Project Structure -> Libraries -> + -> From Maven
//org.xerial:sqlite-jdbc:3.46.0.0


//Am creat database-ul prin urmatorul proces (nu este singura modalitate):
//click dreapta pe proiect -> New -> Data Source in Path
//Driver: SQLite
//copy URL provided in second window that appears
//modificat de la seminar cu relative path
//anterior: jdbc:sqlite:D:/Facultate/Ore 2024-2025/MAP/Mine/SEMINAR4_321/musician_db.db
//url-ul ar putea fi dat si prin parametru in constructor

public class SQLCakeRepository extends MemoryRepository<Cake> implements AutoCloseable {

    Connection connection = null ;
    private static final String DB_URL = "jdbc:sqlite:D:/MAP/a4-Andremyyy/src/Repository/cakes";

    public SQLCakeRepository() {
        openConnection();
        createTable();
        loadData();

    }

    private void createTable() {
        String s = "Create Table if not exists cakes( id int, typeOfCake varchar(100), PRIMARY KEY (id) )";
        try {
            //Statement vs. Prepared Statement
            //Statement: --nu poate fi parametrizat
            //   i.e. putem scrie SELECT * FROM musicians WHERE id = " + id+";", dar ce
            //        facem este doar sa construim query-ul prin concatenare de string
            //           --vulnerabil la SQL injection
            Statement statement = connection.createStatement();

            //.execute() returns: true if the first result is a ResultSet object
            //                    false if it is an update count or there are no results
            boolean executionResult = statement.execute(s);
//            System.out.println("Execution result from createTable(): " + executionResult);
        } catch (SQLException e) {
            System.out.println("Error in creating the table Cakes" + e.getMessage());
        }
    }

    // o metodă pentru a genera 100 de torturi aleatorii
    public void generateRandomCakes(int count) {
        Faker faker = new Faker();
        Set<String> uniqueCakeTypes = new HashSet<>();

        while (uniqueCakeTypes.size() < count) {
            String cakeType = faker.food().ingredient() + " cake";
            uniqueCakeTypes.add(cakeType);
        }

        int id = 2000;
        for (String cakeType : uniqueCakeTypes) {
            try {
                Cake cake = new Cake(id++, cakeType);
                add(cake); // salvează tortul în baza de date
            } catch (RepositoryException e) {
                System.out.println("Failed to add cake: " + e.getMessage());
            }
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
            System.out.println("Error while creating the connection" + e);
        }
    }

    private void loadData() {
        //adding directly to list of entities
        //why not call super.add() pentru fiecare Musician?
        System.out.println("Found " + this.getEntities().size() + " cakes in the table.");
        entities.addAll(this.getEntities());
    }

    @Override
    public void add(Cake elem) throws RepositoryException {
        super.add(elem);
        String s = "INSERT INTO cakes VALUES (?,?);";
        try (PreparedStatement add_statement = connection.prepareStatement(s)){
            add_statement.setInt(1, elem.getId());
            add_statement.setString(2, elem.getTypeOfCake());
            int executionResult = add_statement.executeUpdate();
            System.out.println("From add(), execution result is: " + executionResult);
        }catch (SQLException e) {
            //throw new RepoException cu mesajul erorii SQL
            throw new RepositoryException(e.getMessage());
        }
    }

    @Override
    public void removeById(int id) throws RepositoryException {
        super.removeById(id);
        String s = "DELETE FROM cakes WHERE id=?";
        //try-with-resources
        //https://docs.oracle.com/javase/8/docs/technotes/guides/language/try-with-resources.html
        try (PreparedStatement remove_statement = connection.prepareStatement(s)) {
            remove_statement.setInt(1, id);
            remove_statement.executeUpdate();
        } catch (SQLException e) {
            throw new RepositoryException(e.getMessage());
        }
    }

    @Override
    public ArrayList<Cake> getEntities() {
        // = get all rows from the musician table
        ArrayList<Cake> resultList = new ArrayList<>();
        String s = "SELECT * FROM cakes";
        try (PreparedStatement getAllSstatement = connection.prepareStatement(s)) {
            ResultSet result = getAllSstatement.executeQuery();
            while (result.next()) {
                Cake c = new Cake(result.getInt("id"), result.getString("typeOfCake"));
                resultList.add(c);
            }
            return resultList;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Cake getEntityById(int id) {
        String s = "SELECT * FROM cakes WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Cake(resultSet.getInt("id"), resultSet.getString("typeOfCake"));
            } else {
                return null; // Or throw a custom exception if preferred
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving Cake with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public boolean findById(int id)  {
        String s = "SELECT 1 FROM cakes WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // If a row is found, return true; else, false
        } catch (SQLException e) {
            throw new RuntimeException("Error checking Cake existence with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public void update(Cake elem) throws RepositoryException {
        String s = "UPDATE cakes SET typeOfCake = ? WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setString(1, elem.getTypeOfCake());
            statement.setInt(2, elem.getId());
            int rowsUpdated = statement.executeUpdate();
            if (rowsUpdated == 0) {
                throw new RepositoryException("No Cake found with id = " + elem.getId() + " to update.");
            }
        } catch (SQLException e) {
            throw new RepositoryException("Error updating Cake with id = " + elem.getId() + " : " + e.getMessage());
        }
    }

    @Override
    public void close() throws Exception {
        try {
            if (connection!= null)
                connection.close();
        } catch (SQLException e) {
            // In metoda close e descurajata aruncarea de exceptii
            e.printStackTrace();
        }
    }
}
