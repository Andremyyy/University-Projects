package Repository;

//File -> Project Structure -> Libraries -> + -> From Maven
//org.xerial:sqlite-jdbc:3.46.0.0

//Am creat database-ul prin urmatorul proces (nu este singura modalitate):
//click dreapta pe proiect -> New -> Data Source in Path
//Driver: SQLite
//copy URL provided in second window that appears


import Domain.Radio;
import Exceptions.RepositoryException;

//import com.github.javafaker.Faker;
import org.sqlite.SQLiteDataSource;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class SQLRadioRepository extends MemoryRepository<Radio> implements AutoCloseable {

    Connection connection = null ;
    private static final String DB_URL = "jdbc:sqlite:D:/MAP/radio/src/main/java/Repository/radios";

    public SQLRadioRepository() {
        openConnection();
        createTable();
        loadData();

    }

    private void createTable() {
        String s = "Create Table if not exists radios( id int, formatie varchar(100), titlu varchar(100), gen_muzical varchar(100),  durata varchar(10), PRIMARY KEY (id) )";
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


            // Crearea tabelului pentru Playlisturi (cerinta 3)
            String createPlaylistsTable = "CREATE TABLE IF NOT EXISTS playlists (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "nume VARCHAR(100))";
            statement.execute(createPlaylistsTable);

            // Crearea tabelului de legătură între playlisturi și piese
            String createPlaylistRadioTable = "CREATE TABLE IF NOT EXISTS playlist_radio (" +
                    "playlist_id INTEGER, " +
                    "radio_id INTEGER, " +
                    "durata INTEGER, " +   // durata piesei in secunde pe care o voi converti din String
                    "PRIMARY KEY (playlist_id, radio_id), " +
                    "FOREIGN KEY (playlist_id) REFERENCES playlists(id), " +
                    "FOREIGN KEY (radio_id) REFERENCES radios(id))";
            statement.execute(createPlaylistRadioTable);

//            System.out.println("Execution result from createTable(): " + executionResult);
        } catch (SQLException e) {
            System.out.println("Error in creating the table Radios" + e.getMessage());
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
        System.out.println("Found " + this.getEntities().size() + " radios in the table.");
        entities.addAll(this.getEntities());
    }

    @Override
    public void add(Radio elem) throws RepositoryException {
        super.add(elem);
        String s = "INSERT INTO radios VALUES (?,?,?,?,?);";
        try (PreparedStatement add_statement = connection.prepareStatement(s)){
            add_statement.setInt(1, elem.getId());
            add_statement.setString(2, elem.getFormatie());
            add_statement.setString(3, elem.getTitlu());
            add_statement.setString(4, elem.getGenMuzical());
            add_statement.setString(5, elem.getDurata());
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
        String s = "DELETE FROM radios WHERE id=?";
        try (PreparedStatement remove_statement = connection.prepareStatement(s)) {
            remove_statement.setInt(1, id);
            remove_statement.executeUpdate();
        } catch (SQLException e) {
            throw new RepositoryException(e.getMessage());
        }
    }

    @Override
    public ArrayList<Radio> getEntities() {
        // = get all rows from the musician table
        ArrayList<Radio> resultList = new ArrayList<>();
        String s = "SELECT * FROM radios";
        try (PreparedStatement getAllSstatement = connection.prepareStatement(s)) {
            ResultSet result = getAllSstatement.executeQuery();
            while (result.next()) {
                Radio r = new Radio(result.getInt("id"), result.getString("formatie"), result.getString("titlu"), result.getString("gen_muzical"), result.getString("durata"));
                resultList.add(r);
            }
            return resultList;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Radio getEntityById(int id) {
        String s = "SELECT * FROM radios WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Radio(resultSet.getInt("id"), resultSet.getString("formatie"), resultSet.getString("titlu"), resultSet.getString("gen_muzical"), resultSet.getString("durata"));
            } else {
                return null; // Or throw a custom exception if preferred
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving Radio with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public boolean findById(int id)  {
        String s = "SELECT 1 FROM radios WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // If a row is found, return true; else, false
        } catch (SQLException e) {
            throw new RuntimeException("Error checking Radio existence with id = " + id + " : " + e.getMessage(), e);
        }
    }

    @Override
    public void update(Radio elem) throws RepositoryException {
        //todo: vezi aici
        String s = "UPDATE radios SET formatie = ? WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setString(1, elem.getFormatie());
            statement.setInt(2, elem.getId());
            int rowsUpdated = statement.executeUpdate();
            if (rowsUpdated == 0) {
                throw new RepositoryException("No Radio found with id = " + elem.getId() + " to update.");
            }
        } catch (SQLException e) {
            throw new RepositoryException("Error updating Radio with id = " + elem.getId() + " : " + e.getMessage());
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

    public int convertDurataToSecunde(String durata) {
        if (durata != null && durata.matches("\\d{1,2}:\\d{2}")) {  // Verificăm dacă durata este în format mm:ss
            String[] parts = durata.split(":");
            int minute = Integer.parseInt(parts[0]);
            int secunde = Integer.parseInt(parts[1]);
            return minute * 60 + secunde;  // Returnează durata în secunde
        } else {
            throw new IllegalArgumentException("Durata nu are un format valid: " + durata);
        }
    }

    public void addSongToPlaylist(int playlistId, int radioId, String durata) throws RepositoryException {
        int durataInSecunde = convertDurataToSecunde(durata);  // Convertesc durata în secunde
        String s = "INSERT INTO playlist_radio (playlist_id, radio_id, durata) VALUES (?, ?, ?);";
        try (PreparedStatement add_statement = connection.prepareStatement(s)) {
            add_statement.setInt(1, playlistId);
            add_statement.setInt(2, radioId);
            add_statement.setInt(3, durataInSecunde);  // Adăugăm durata în secunde
            add_statement.executeUpdate();
        } catch (SQLException e) {
            throw new RepositoryException(e.getMessage());
        }
    }

    public void createPlaylist(String numePlaylist) throws RepositoryException {
        addPlaylist(numePlaylist); // Adăugăm playlistul în DB
        int playlistId = getPlaylistIdByName(numePlaylist); // Obținem ID-ul playlistului creat

        // Seturi pentru a păstra formatiile și genurile pentru a evita repetițiile
        Set<String> formatii = new HashSet<>();
        Set<String> genuri = new HashSet<>();
        int durataTotala = 0;

        while (durataTotala < 15 * 60) {  // 15 minute în secunde
            Radio piesa = getRandomSong(); // O funcție care selectează aleatoriu o piesă
            if (piesa != null) {
                // Verificăm condițiile
                if (!formatii.contains(piesa.getFormatie()) && !genuri.contains(piesa.getGenMuzical())) {
                    int durataPiesaInSecunde = convertDurataToSecunde(piesa.getDurata());  // Convertem durata piesei în secunde
                    addSongToPlaylist(playlistId, piesa.getId(), piesa.getDurata());  // Adăugăm durata piesei în playlist
                    formatii.add(piesa.getFormatie());
                    genuri.add(piesa.getGenMuzical());
                    durataTotala += durataPiesaInSecunde;  // Adăugăm durata piesei la total
                }
            }
        }
    }

    private void addPlaylist(String numePlaylist) throws RepositoryException {
        String s = "INSERT INTO playlists (nume) VALUES (?);";
        try (PreparedStatement add_statement = connection.prepareStatement(s)) {
            add_statement.setString(1, numePlaylist); // Setăm numele playlistului
            add_statement.executeUpdate();
        } catch (SQLException e) {
            throw new RepositoryException("Eroare la adăugarea playlistului: " + e.getMessage());
        }
    }

    public int getPlaylistIdByName(String numePlaylist) throws RepositoryException {
        String s = "SELECT id FROM playlists WHERE nume = ?;";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            statement.setString(1, numePlaylist);  // Setăm numele playlistului în interogare
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getInt("id");  // Dacă există un playlist cu numele respectiv, returnăm ID-ul său
            } else {
                throw new RepositoryException("Playlistul cu numele " + numePlaylist + " nu a fost găsit.");
            }
        } catch (SQLException e) {
            throw new RepositoryException("Eroare la obținerea ID-ului playlistului: " + e.getMessage());
        }
    }

    public Radio getRandomSong() throws RepositoryException {
        String s = "SELECT * FROM radios ORDER BY RANDOM() LIMIT 1;";
        try (PreparedStatement statement = connection.prepareStatement(s)) {
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Radio(
                        resultSet.getInt("id"),
                        resultSet.getString("formatie"),
                        resultSet.getString("titlu"),
                        resultSet.getString("gen_muzical"),
                        resultSet.getString("durata")
                );
            } else {
                throw new RepositoryException("Nu s-a găsit nicio piesă în baza de date.");
            }
        } catch (SQLException e) {
            throw new RepositoryException("Eroare la obținerea piesei aleatorii: " + e.getMessage());
        }
    }


}
