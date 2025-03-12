package Repository;

//File -> Project Structure -> Libraries -> + -> From Maven
//org.xerial:sqlite-jdbc:3.46.0.0

//Am creat database-ul prin urmatorul proces (nu este singura modalitate):
//click dreapta pe proiect -> New -> Data Source in Path
//Driver: SQLite
//copy URL provided in second window that appears


import Domain.Produs;
import Exceptions.RepositoryException;
import org.sqlite.SQLiteDataSource;

import java.sql.*;
import java.util.ArrayList;

public class SQLProdusRepository extends MemoryRepository<Produs> implements AutoCloseable {

    Connection connection = null ;
    private static final String DB_URL = "jdbc:sqlite:D:/MAP/cumparatori_min_max/produse";

    public SQLProdusRepository() {
        openConnection();
        createTable();
        loadData();

    }

    private void createTable() {
        String s = "Create Table if not exists produse( id int, marca varchar(100), nume varchar(100), pret int,  cantitate int, PRIMARY KEY (id) )";
        try {
            //Statement vs. Prepared Statement
            //Statement: --nu poate fi parametrizat
            //   i.e. putem scrie SELECT * FROM musicians WHERE id = " + id+";", dar ce
            //        facem este doar sa construim query-ul prin concatenare de string
            //           --vulnerabil la SQL injection
            Statement statement = connection.createStatement();

            //.execute() returns: true if the first result is a ResultSet object
            //                    false if it is an update count or there are no results
            statement.execute(s);

//            System.out.println("Execution result from createTable(): " + executionResult);
        } catch (SQLException e) {
            System.out.println("Error in creating the table Produse" + e.getMessage());
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
        System.out.println("Found " + this.getEntities().size() + " produse in the table.");
        entities.addAll(this.getEntities());
    }

    @Override
    public void add(Produs elem) throws RepositoryException {
        super.add(elem);
        String s = "INSERT INTO produse VALUES (?,?,?,?,?);";
        try (PreparedStatement add_statement = connection.prepareStatement(s)){
            add_statement.setInt(1, elem.getId());
            add_statement.setString(2, elem.getMarca());
            add_statement.setString(3, elem.getNume());
            add_statement.setInt(4, elem.getPret());
            add_statement.setInt(5, elem.getCantitate());
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
        String s = "DELETE FROM produse WHERE id=?";
        try (PreparedStatement remove_statement = connection.prepareStatement(s)) {
            remove_statement.setInt(1, id);
            remove_statement.executeUpdate();
        } catch (SQLException e) {
            throw new RepositoryException(e.getMessage());
        }
    }

    @Override
    public ArrayList<Produs> getEntities() {
        // = get all rows from the musician table
        ArrayList<Produs> resultList = new ArrayList<>();
        String s = "SELECT * FROM produse";
        try (PreparedStatement getAllSstatement = connection.prepareStatement(s)) {
            ResultSet result = getAllSstatement.executeQuery();
            while (result.next()) {
                Produs p = new Produs(result.getInt("id"), result.getString("marca"), result.getString("nume"), result.getInt("pret"), result.getInt("cantitate"));
                resultList.add(p);
            }
            return resultList;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Produs getEntityById(int id) {
        String s = "SELECT * FROM produse WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Produs(resultSet.getInt("id"), resultSet.getString("marca"), resultSet.getString("nume"), resultSet.getInt("pret"), resultSet.getInt("cantitate"));
            } else {
                return null; // Or throw a custom exception if preferred
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving Produs with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public boolean findById(int id)  {
        String s = "SELECT 1 FROM produse WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // If a row is found, return true; else, false
        } catch (SQLException e) {
            throw new RuntimeException("Error checking Produs existence with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public void update(Produs elem) throws RepositoryException {
        //todo: vezi aici
        String s = "UPDATE produse SET cantitate = ? WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, elem.getCantitate()-1);
            statement.setInt(2, elem.getId());
            int rowsUpdated = statement.executeUpdate();
            if (rowsUpdated == 0) {
                throw new RepositoryException("No Produs found with id = " + elem.getId() + " to update.");
            }
        } catch (SQLException e) {
            throw new RepositoryException("Error updating Produs with id = " + elem.getId() + " : " + e.getMessage());
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
