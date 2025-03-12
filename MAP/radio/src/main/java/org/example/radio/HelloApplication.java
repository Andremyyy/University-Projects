package org.example.radio;

import Domain.Radio;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;
import Repository.SQLRadioRepository;
import Service.RadioService;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

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
        // Obținem radiourile sortate din serviciu
        ObservableList<Radio> radioObservableList = FXCollections.observableArrayList(radioService.getSortedItems());

        radioTable.setItems(radioObservableList);

        // configurez comparatorii pentru coloane
        formatieColumn.setComparator(String::compareToIgnoreCase);
        titluColumn.setComparator(String::compareToIgnoreCase);

        // Setăm ordinea implicită de sortare
        radioTable.getSortOrder().add(formatieColumn);



        // Secțiunea de filtrare
        VBox filterBox = new VBox(20);
        filterBox.setAlignment(Pos.TOP_CENTER);


        TextField filterField = new TextField();
        filterField.setAlignment(Pos.CENTER);
        filterField.setPromptText("Textul pt filtrare");
        Button resetButton = new Button("Resetare");

        TableView<Radio> filteredTable = new TableView<>();
        filteredTable.setPrefWidth(500);

        TableColumn<Radio, Integer> filteredIdColumn = new TableColumn<>("ID");
        TableColumn<Radio, String> filteredFormatieColumn = new TableColumn<>("Formatie");
        TableColumn<Radio, String> filteredTitluColumn = new TableColumn<>("Titlu");
        TableColumn<Radio, String> filteredGenMuzicalColumn = new TableColumn<>("Gen muzical");
        TableColumn<Radio, String> filteredDurataColumn = new TableColumn<>("Durata");

        filteredIdColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        filteredFormatieColumn.setCellValueFactory(new PropertyValueFactory<>("formatie"));
        filteredTitluColumn.setCellValueFactory(new PropertyValueFactory<>("titlu"));
        filteredGenMuzicalColumn.setCellValueFactory(new PropertyValueFactory<>("genMuzical"));
        filteredDurataColumn.setCellValueFactory(new PropertyValueFactory<>("durata"));

        filteredTable.getColumns().addAll(filteredIdColumn, filteredFormatieColumn, filteredTitluColumn, filteredGenMuzicalColumn, filteredDurataColumn);


        ObservableList<Radio> filteredList = FXCollections.observableArrayList();
        filteredTable.setItems(filteredList);


        // Filtrare pe baza textului introdus
        filterField.textProperty().addListener((observable, oldValue, newValue) -> {
            filteredList.clear();
            if (newValue == null || newValue.isEmpty()) {
                return;
            }

            try {
                filteredList.addAll(radioService.getFilteredRadios(newValue));
            } catch (RepositoryException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("EROARE filtrare");
                alert.setHeaderText(null);
                alert.setContentText("Eroare la filtrare: " + e.getMessage());
                alert.showAndWait();
            }

            if (filteredList.isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setTitle("EROARE filtrare");
                alert.setHeaderText(null);
                alert.setContentText("Nu s-au găsit rezultate pentru căutarea introdusă!");
                alert.showAndWait();
            }
        });

        // Resetare
        resetButton.setOnAction(event -> {
            filterField.clear();
            filteredList.clear();
            filteredList.addAll(radioObservableList);
        });

        filterBox.getChildren().addAll(filterField, filteredTable, resetButton);


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

            try {
                List<Radio> generatedPlaylist = radioService.generatePlaylist(playlistName);
                playlistList.clear();
                playlistList.addAll(generatedPlaylist);

            } catch (RepositoryException | ParseException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("EROARE");
                alert.setHeaderText(null);
                alert.setContentText("Nu s-a putut genera lista de redare: " + e.getMessage());
                alert.showAndWait();
            }
        });

        playlistBox.getChildren().addAll(playlistNameField, generateButton, playlistTable);

        // Adăugăm totul în layout-ul principal
        mainBox.getChildren().addAll(radioTable, filterBox, playlistBox);

        Scene scene = new Scene(mainBox, 1340, 820);
        stage.setTitle("My radio management system!");
        stage.setScene(scene);
        stage.show();

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

    public static void main(String[] args) {
        launch();
    }
}