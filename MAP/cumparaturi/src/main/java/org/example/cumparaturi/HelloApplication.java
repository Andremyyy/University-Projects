package org.example.cumparaturi;

import Domain.Produs;
import Exceptions.RepositoryException;
import Repository.BinaryFileRepository;
import Service.ProdusService;
import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
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

public class HelloApplication extends Application {

    @Override
    public void start(Stage stage) throws IOException {

        String fileName = "produse.bin";



        {
            try {
                BinaryFileRepository<Produs> produsRepo = new BinaryFileRepository<>(fileName);
                ProdusService produsService = new ProdusService(produsRepo);

                addEntities(produsRepo);


                //layout-ul principal
                HBox mainBox = new HBox(20);

                //cream un tabel in care vom afisa datele radiourilor
                TableView<Produs> produsTable = new TableView<>();

                produsTable.setPrefWidth(400);

                //cream cate o coloana pe rand
                //textul din paranteze este header-ul
                TableColumn<Produs, Integer> idColumn = new TableColumn<>("ID");
                TableColumn<Produs, String> marcaColumn = new TableColumn<>("Marca");
                TableColumn<Produs, String> numeColumn = new TableColumn<>("Nume");
                TableColumn<Produs, Integer> pretColumn = new TableColumn<>("Pret");
                TableColumn<Produs, String> cantitateColumn = new TableColumn<>("Cantitate");

                //specificam cum se vor completa coloanele - ce camp dintr-un
                //obiect Radio vine pe fiecare coloana

                idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
                marcaColumn.setCellValueFactory(new PropertyValueFactory<>("marca"));
                numeColumn.setCellValueFactory(new PropertyValueFactory<>("nume"));
                pretColumn.setCellValueFactory(new PropertyValueFactory<>("pret"));
                cantitateColumn.setCellValueFactory(cellData -> {
                    // dacă cantitatea este 0, returnează "n/a", altfel returnează valoarea cantității
                    if (cellData.getValue().getCantitate() == 0) {
                        return new SimpleStringProperty("n/a");
                    } else {
                        return new SimpleStringProperty(String.valueOf(cellData.getValue().getCantitate()));
                    }
                });

                //adaugam coloanele la tabel
                produsTable.getColumns().add(idColumn);
                produsTable.getColumns().add(marcaColumn);
                produsTable.getColumns().add(numeColumn);
                produsTable.getColumns().add(pretColumn);
                produsTable.getColumns().add(cantitateColumn);

                //cream o lista de radiouri care se vor afisa in tabel
                //https://docs.oracle.com/javase/8/javafx/api/javafx/collections/ObservableList.html
                ObservableList<Produs> produseObservableList = FXCollections.observableArrayList(produsService.getProduse());

                // Sortez lista observabilă
                produseObservableList.sort((radio1, radio2) -> Integer.compare(radio1.getId(), radio2.getId()));

                produsTable.setItems(produseObservableList);

                // configurez comparatorii pentru coloane
                idColumn.setComparator(Integer::compare);



                VBox rightSideBox = new VBox(5);
                GridPane labelsAndFieldsPane = new GridPane();
                labelsAndFieldsPane.setVgap(3.5);
                labelsAndFieldsPane.setHgap(3.5);

                Label marcaLabel = new Label("Marca:");
                Label numeLabel = new Label("Nume:");
                Label pretLabel = new Label("Pret:");
                Label cantitateLabel = new Label("Cantitate:");

                TextField marcaTextField = new TextField();
                TextField numeTextField = new TextField();
                TextField pretTextField = new TextField();
                TextField cantitateTextField = new TextField();

                labelsAndFieldsPane.add(marcaLabel, 0, 0);
                labelsAndFieldsPane.add(marcaTextField, 1, 0);
                labelsAndFieldsPane.add(numeLabel, 0, 1);
                labelsAndFieldsPane.add(numeTextField, 1, 1);
                labelsAndFieldsPane.add(pretLabel, 0, 2);
                labelsAndFieldsPane.add(pretTextField, 1, 2);
                labelsAndFieldsPane.add(cantitateLabel, 0, 3);
                labelsAndFieldsPane.add(cantitateTextField, 1, 3);


                rightSideBox.getChildren().add(labelsAndFieldsPane);



                //new HBox pentru butoane
                HBox buttonBox = new HBox();



                Button addProdusButton = new Button("Add Produs");

                addProdusButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
                    @Override
                    public void handle(MouseEvent mouseEvent) {
                        try{
                            // incerc sa folosesc idGenerator
                            String marca = marcaTextField.getText();
                            String nume = numeTextField.getText();
                            String pret = pretTextField.getText();
                            String cantitate = cantitateTextField.getText();
                            if (marca.isEmpty())
                                throw new Exception("Marca cannot be empty!");
                            if (nume.isEmpty())
                                throw new Exception("Nume cannot be empty!");
                            if (pret.isEmpty())
                                throw new Exception("Pret cannot be empty!");
                            if (cantitate.isEmpty())
                                throw new Exception("Cantitate cannot be empty!");
                            if (Integer.parseInt(pret) < 0)
                                throw new Exception("Pret cannot be negative!");
                            if (Integer.parseInt(cantitate) < 0)
                                throw new Exception("Cantitate cannot be negative!");

                            // Găsim cel mai mare ID existent și incrementăm cu 1
                            int newId = getNextId(produsService);

                            produsService.addProdus(newId, marca, nume, Integer.parseInt(pret), Integer.parseInt(cantitate));
                            produseObservableList.setAll(produsService.getProduse());
                            System.out.println("Produs added succesfully");
                        } catch (Exception e ){
                            Alert alert = new Alert(Alert.AlertType.ERROR);
                            alert.setTitle("Error");
                            alert.setContentText("An error has occurred: "+e.getMessage());
                            alert.show();
                        }
                        // Resetăm câmpurile după actualizare

                        marcaTextField.clear();
                        numeTextField.clear();
                        pretTextField.clear();
                        cantitateTextField.clear();
                    }
                });




                buttonBox.getChildren().addAll(addProdusButton, labelsAndFieldsPane);

                //aranjam butoanele in HBox sa fie centrate
                //https://openjfx.io/javadoc/13/javafx.graphics/javafx/geometry/Pos.html#BASELINE_CENTER
                buttonBox.setAlignment(Pos.BASELINE_CENTER);
                buttonBox.setSpacing(10);


                // pentru FILTRARE

                // Secțiunea de filtrare
                VBox filterBox = new VBox(20);
                filterBox.setAlignment(Pos.TOP_CENTER);


                TextField filterField = new TextField();
                filterField.setAlignment(Pos.CENTER);
                filterField.setPromptText("Textul pt filtrare");
                Button filterButton = new Button("Filtreaza");


                // Butonul pentru filtrare
                filterButton.setOnMouseClicked(mouseEvent -> {
                    try {
                        String filterText = filterField.getText();

                        // Lista originală de produse
                        ObservableList<Produs> originalList = FXCollections.observableArrayList(produsService.getProduse());

                        // Dacă câmpul de filtrare este gol, nu facem nicio modificare
                        if (filterText == null || filterText.isEmpty()) {
                            produseObservableList.setAll(originalList);
                            return;
                        }

                        // Creăm o listă filtrată
                        ObservableList<Produs> filteredList = FXCollections.observableArrayList();

                        for (Produs produs : originalList) {
                            if (produs.getNume().toLowerCase().contains(filterText.toLowerCase()) ||
                                    produs.getMarca().toLowerCase().contains(filterText.toLowerCase())) {
                                filteredList.add(produs);
                            }
                        }

                        // Dacă lista filtrată este goală, afișăm un mesaj de eroare și nu modificăm lista curentă
                        if (filteredList.isEmpty()) {
                            Alert alert = new Alert(Alert.AlertType.WARNING);
                            alert.setTitle("EROARE filtrare");
                            alert.setHeaderText(null);
                            alert.setContentText("Nu s-au găsit rezultate pentru căutarea introdusă!");
                            alert.showAndWait();
                        } else {
                            // Actualizăm lista observabilă doar dacă lista filtrată nu este goală
                            produseObservableList.setAll(filteredList);
                        }

                    } catch (Exception e) {
                        Alert alert = new Alert(Alert.AlertType.ERROR);
                        alert.setTitle("Eroare");
                        alert.setHeaderText(null);
                        alert.setContentText("A apărut o eroare: " + e.getMessage());
                        alert.showAndWait();
                    }
                });

                filterBox.getChildren().addAll(filterField, filterButton);

                mainBox.getChildren().addAll(produsTable, buttonBox, filterBox);

                Scene scene = new Scene(mainBox, 1340, 820);
                stage.setTitle("My Shop Management System!");
                stage.setScene(scene);
                stage.show();


            } catch (RepositoryException e) {
                System.out.println("Eroare la incercarea rularii fisierului binar : " + e.getMessage());
            }
        }


    }

    public void addEntities(BinaryFileRepository<Produs> produsRepo) {
        if (produsRepo.size() < 6) {
            try {
                produsRepo.add(new Produs(100, "Lenovo", "ThinkPad S100", 9500, 14));
                produsRepo.add(new Produs(101, "Asus", "Strix 45", 7700, 4));
                produsRepo.add(new Produs(102, "Ariston", "WSL-1002", 2240, 2));
                produsRepo.add(new Produs(103, "Bosch", "Series 4", 1900, 11));
                produsRepo.add(new Produs(104, "Whirlpool", "SuperFridge 100LE", 3200, 10));
                produsRepo.add(new Produs(105, "Element fara cantitate", "Ceva", 1000, 0));

            } catch (RepositoryException re) {
                System.out.println(re.getMessage());
            }
        }
    }

    // Metodă care returnează cel mai mic ID mai mare decât cele existente
    private int getNextId(ProdusService produsService) {
        // Preluăm toate produsele existente
        ObservableList<Produs> produse = FXCollections.observableArrayList(produsService.getProduse());

        // Verificăm dacă lista este goală (adică nu există produse)
        if (produse.isEmpty()) {
            return 1; // Dacă nu există produse, ID-ul inițial va fi 1
        }

        // Găsim cel mai mare ID existent
        int maxId = produse.stream()
                .mapToInt(Produs::getId)
                .max()
                .orElse(0); // Dacă lista este goală, maxId va fi 0

        // Returnăm ID-ul următor (maxId + 1)
        return maxId + 1;
    }

    public static void main(String[] args) {
        launch();
    }


}