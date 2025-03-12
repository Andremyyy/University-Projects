package org.example.radio_fire_de_executie;

import Domain.PlaylistGenerationJob;
import Domain.Radio;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;
import Repository.SQLRadioRepository;
import Service.RadioService;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException, RepositoryException {


        AbstractRepository<Radio> radioRepo = new SQLRadioRepository();

        RadioService radioService = new RadioService(radioRepo);

        addEntities(radioRepo);


        //layout-ul principal
        HBox mainBox = new HBox(20);

        //cream un tabel in care vom afisa datele radiourilor
        TableView<Radio> radioTable = new TableView<>();

        radioTable.setPrefWidth(500);

        //cream cate o coloana pe rand
        //textul din paranteze este header-ul
        TableColumn<Radio, Integer> idColumn = new TableColumn<>("ID");
        TableColumn<Radio, String> formatieColumn = new TableColumn<>("Formatie");
        TableColumn<Radio, String> titluColumn = new TableColumn<>("Titlu");
        TableColumn<Radio, String> gen_muzicalColumn = new TableColumn<>("Gen muzical");
        TableColumn<Radio, String> durataColumn = new TableColumn<>("Durata");

        //specificam cum se vor completa coloanele - ce camp dintr-un
        //obiect Radio vine pe fiecare coloana

        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        formatieColumn.setCellValueFactory(new PropertyValueFactory<>("formatie"));
        titluColumn.setCellValueFactory(new PropertyValueFactory<>("titlu"));
        gen_muzicalColumn.setCellValueFactory(new PropertyValueFactory<>("genMuzical"));
        durataColumn.setCellValueFactory(new PropertyValueFactory<>("durata"));


        //adaugam coloanele la tabel
        radioTable.getColumns().add(idColumn);
        radioTable.getColumns().add(formatieColumn);
        radioTable.getColumns().add(titluColumn);
        radioTable.getColumns().add(gen_muzicalColumn);
        radioTable.getColumns().add(durataColumn);

        //cream o lista de radiouri care se vor afisa in tabel
        //https://docs.oracle.com/javase/8/javafx/api/javafx/collections/ObservableList.html
        ObservableList<Radio> radioObservableList = FXCollections.observableArrayList(radioService.getRadios());

        // Sortez lista observabilă
        radioObservableList.sort((radio1, radio2) -> {
            int result = radio1.getFormatie().compareToIgnoreCase(radio2.getFormatie());
            if (result == 0) {
                result = radio1.getDurata().compareToIgnoreCase(radio2.getDurata());
            }
            return result;
        });

        radioTable.setItems(radioObservableList);

        // configurez comparatorii pentru coloane
        formatieColumn.setComparator(String::compareToIgnoreCase);
        durataColumn.setComparator(String::compareToIgnoreCase);

        // Setăm ordinea implicită de sortare
        radioTable.getSortOrder().add(formatieColumn);


        // cerinta 2


        //Vertical Box
        //https://openjfx.io/javadoc/13/javafx.graphics/javafx/scene/layout/VBox.html
        //componentele sunt aranjate pe o coloana, pe verticala
        //rightSideBox este unde vom pune label-urile si text field-urile
        //si butoanele

        VBox rightSideBox = new VBox(5);
        GridPane labelsAndFieldsPane = new GridPane();
        labelsAndFieldsPane.setVgap(3.5);
        labelsAndFieldsPane.setHgap(3.5);

        Label formatieLabel = new Label("Formatie:");
        Label titluLabel = new Label("Titlu:");
        Label genMuzicalLabel = new Label("Gen muzical:");
        Label durataLabel = new Label("Durata:");


        TextField formatieTextField = new TextField();
        TextField titluTextField = new TextField();
        TextField genMuzicalTextField = new TextField();
        TextField durataTextField = new TextField();

        labelsAndFieldsPane.add(formatieLabel, 0, 0);
        labelsAndFieldsPane.add(formatieTextField, 1, 0);
        labelsAndFieldsPane.add(titluLabel, 0, 1);
        labelsAndFieldsPane.add(titluTextField, 1, 1);
        labelsAndFieldsPane.add(genMuzicalLabel, 0, 2);
        labelsAndFieldsPane.add(genMuzicalTextField, 1, 2);
        labelsAndFieldsPane.add(durataLabel, 0, 3);
        labelsAndFieldsPane.add(durataTextField, 1, 3);

        rightSideBox.getChildren().add(labelsAndFieldsPane);

        //new HBox pentru butoane
        HBox buttonBox = new HBox();
        Button addRadioButton = new Button("Add Radio");

//        addCakeButton.setPrefHeight(80);
//        addCakeButton.setPrefWidth(80);

        buttonBox.getChildren().add(addRadioButton);

        //aranjam butoanele in HBox sa fie centrate
        //https://openjfx.io/javadoc/13/javafx.graphics/javafx/geometry/Pos.html#BASELINE_CENTER
        buttonBox.setAlignment(Pos.BASELINE_CENTER);
        buttonBox.setSpacing(10);

        rightSideBox.getChildren().add(buttonBox);


        addRadioButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                try{
                    // incerc sa folosesc idGenerator
                    String formatie = formatieTextField.getText();
                    String titlu = titluTextField.getText();
                    String genMuzical = genMuzicalTextField.getText();
                    String durata = durataTextField.getText();
                    if (formatie.isEmpty())
                        throw new Exception("Formatie cannot be empty!");
                    if (titlu.isEmpty())
                        throw new Exception("titlu cannot be empty!");
                    if (genMuzical.isEmpty())
                        throw new Exception("Gen Muzical cannot be empty!");
                    if (durata.isEmpty())
                        throw new Exception("Durata cannot be empty!");

                    //todo: durata sa fie intr 1 min si 10 min

                    // Găsim cel mai mare ID existent și incrementăm cu 1
                    int newId = getNextId(radioService);

                    radioService.addRadio(newId, formatie, titlu, genMuzical, durata);
                    radioObservableList.setAll(radioService.getRadios());
                    System.out.println("Radio added succesfully");
                } catch (Exception e ){
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error");
                    alert.setContentText("An error has occurred: "+e.getMessage());
                    alert.show();
                }
                // Resetăm câmpurile după actualizare

                formatieTextField.clear();
                titluTextField.clear();
                durataTextField.clear();
                genMuzicalTextField.clear();
            }
        });

        //3. Generarea unei liste de redare.
        // Utilizatorul va completa numele listei,
        // iar aplicatia va genera o lista de redare care
        // va fi salvata in baza de date, in tabelul avand
        // numele dat de utilizator.
        // Piesele incluse in lista vor fi alese in mod
        // aleator de program, cu conditia ca sa nu existe
        // doua piese consecutive cantate de aceeasi formatie,
        // sau avand acelasi gen. Constructia listei de redare
        // se va termina odata ce durata totala a pieselor incluse
        // depaseste 15 minute. In cazul in care construirea listei
        // nu este posibila, aplicatia va afisa un mesaj de eroare
        // folosind un dialog de tip Alert



        // Generare lista de redare/PLAYLIST-urilor
        VBox playlistBox = new VBox(20);
        playlistBox.setAlignment(Pos.TOP_CENTER);

        TextField playlistNameField = new TextField();
        playlistNameField.setPromptText("Introduceti numele playlistului");
        Button generateButton = new Button("Generează Playlist");

        TableView<Radio> playlistTable = new TableView<>();
        playlistTable.setPrefWidth(500);

        TableColumn<Radio, Integer> playlistIdColumn = new TableColumn<>("ID");
        TableColumn<Radio, String> playlistFormatieColumn = new TableColumn<>("Formatie");
        TableColumn<Radio, String> playlistTitluColumn = new TableColumn<>("Titlu");
        TableColumn<Radio, String> playlistGenMuzicalColumn = new TableColumn<>("Gen muzical");
        TableColumn<Radio, String> playlistDurataColumn = new TableColumn<>("Durata");

        playlistIdColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        playlistFormatieColumn.setCellValueFactory(new PropertyValueFactory<>("formatie"));
        playlistTitluColumn.setCellValueFactory(new PropertyValueFactory<>("titlu"));
        playlistGenMuzicalColumn.setCellValueFactory(new PropertyValueFactory<>("genMuzical"));
        playlistDurataColumn.setCellValueFactory(new PropertyValueFactory<>("durata"));

        playlistTable.getColumns().addAll(playlistIdColumn, playlistFormatieColumn, playlistTitluColumn, playlistGenMuzicalColumn, playlistDurataColumn);

        ObservableList<Radio> playlistList = FXCollections.observableArrayList();
        playlistTable.setItems(playlistList);

        generateButton.setOnAction(event -> {
            String playlistName = playlistNameField.getText();
            if (playlistName.isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setTitle("EROARE");
                alert.setHeaderText(null);
                alert.setContentText("Trebuie să introduceți un nume pentru playlist!");
                alert.showAndWait();
                return;
            }

            generatePlaylistInThreads(playlistName, playlistList, radioService);


        });

        playlistBox.getChildren().addAll(playlistNameField, generateButton, playlistTable);

        // Adăugăm totul în layout-ul principal
        mainBox.getChildren().addAll(radioTable, rightSideBox, playlistBox);

        Scene scene = new Scene(mainBox, 1340, 820);
        stage.setTitle("My radio management system!");
        stage.setScene(scene);
        stage.show();

    }

    private void generatePlaylistInThreads(String playlistName, ObservableList<Radio> playlistList, RadioService radioService) {

        playlistList.clear();

        int totalDuration = 0;
        String lastFormatie = "";
        String lastGen = "";
        int totalThreads = 4; // Exemple, numărul de thread-uri poate fi un parametru din UI

        // Calculăm intervalul pentru fiecare thread
        int chunkSize = radioService.getRadios().size() / totalThreads;

        Thread[] threads = new Thread[totalThreads];
        for (int i = 0; i < totalThreads; i++) {
            int start = i * chunkSize;
            int end = (i + 1) * chunkSize;
            if (i == totalThreads - 1) {
                end = radioService.getRadios().size(); // Ultimul thread va prelua restul pieselor
            }

            PlaylistGenerationJob job = new PlaylistGenerationJob(playlistList, radioService, start, end);
            threads[i] = new Thread(job);
        }

        // Pornim thread-urile
        for (int i = 0; i < totalThreads; i++) {
            threads[i].start();
        }

        // Așteptăm finalizarea fiecărui thread
        for (int i = 0; i < totalThreads; i++) {
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // După ce toate thread-urile au terminat, actualizăm UI-ul cu playlist-ul complet
        Platform.runLater(() -> {
            // Update UI with the complete playlist
            System.out.println("Playlist generation complete!");
        });

    }

    private void generatePlaylist(String playlistName, ObservableList<Radio> playlistList, RadioService radioService) throws RepositoryException, ParseException {

        //Generarea unei liste de redare aleatorii care respectă cerințele
        List<Radio> selectedRadios = new ArrayList<>();
        int totalDuration = 0;
        String lastFormatie = "";
        String lastGen = "";

        while (totalDuration <= 15 * 60) { // 15 minute = 900 secunde
            Radio randomSong = getRandomSong(radioService);
            if ((selectedRadios.isEmpty() || !randomSong.getFormatie().equals(lastFormatie)) &&
                    (selectedRadios.isEmpty() || !randomSong.getGenMuzical().equals(lastGen))) {

                int songDurationInSeconds = convertDurationToSeconds(randomSong.getDurata());
                if (totalDuration + songDurationInSeconds > 15 * 60) {
                    break;
                }

                selectedRadios.add(randomSong);
                totalDuration += songDurationInSeconds;
                lastFormatie = randomSong.getFormatie();
                lastGen = randomSong.getGenMuzical();
            }
        }

        playlistList.clear();
        playlistList.addAll(selectedRadios);
    }

    private int convertDurationToSeconds(String durata) throws ParseException {
        SimpleDateFormat format = new SimpleDateFormat("mm:ss");
        Date date = format.parse(durata);
        return (int) (date.getTime() / 1000);
    }

    // Metodă de selecție aleatorie a unei piese
    private Radio getRandomSong(RadioService radioService) throws RepositoryException {
        // Alege o piesă aleatorie
        List<Radio> allRadios = new ArrayList<>(radioService.getRadios());
        int randomIndex = (int) (Math.random() * allRadios.size());
        return allRadios.get(randomIndex);
    }

    private void addEntities(AbstractRepository<Radio> radioRepo) {
        if (radioRepo.size() < 6) {
            try {
                radioRepo.add(new Radio(1000, "Coldplay", "A Head Full of Dreams", "Alternative", "03:43"));
                radioRepo.add(new Radio(1001, "One Direction", "Midnight Memories", "Pop", "02:56"));
                radioRepo.add(new Radio(1002, "The Beatles", "Hey Jude", "Rock", "03:58"));
                radioRepo.add(new Radio(1003, "The Beatles", "Yesterday - Remastered 2009", "Rock", "02:05"));
                radioRepo.add(new Radio(1004, "One Direction", "Diana", "Pop", "03:04"));
                radioRepo.add(new Radio(1005, "5 Seconds of Summer", "She Looks So Perfect", "Pop", "03:22"));

            } catch (RepositoryException re) {
                System.out.println(re.getMessage());
            }
        }
    }

    // Metodă care returnează cel mai mic ID mai mare decât cele existente
    private int getNextId(RadioService radioService) {
        // Preluăm toate produsele existente
        ObservableList<Radio> radios = FXCollections.observableArrayList(radioService.getRadios());

        // Verificăm dacă lista este goală (adică nu există radios)
        if (radios.isEmpty()) {
            return 1; // Dacă nu există radios, ID-ul inițial va fi 1
        }

        // Găsim cel mai mare ID existent
        int maxId = radios.stream()
                .mapToInt(Radio::getId)
                .max()
                .orElse(0); // Dacă lista este goală, maxId va fi 0

        // Returnăm ID-ul următor (maxId + 1)
        return maxId + 1;
    }

    public static void main(String[] args) {
        launch();
    }
}