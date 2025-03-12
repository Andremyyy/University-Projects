package org.example.cumparatori_min_max;

import Domain.Produs;
import Exceptions.RepositoryException;
import Repository.SQLProdusRepository;
import Service.ProdusService;
import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) {
        SQLProdusRepository produsRepo = new SQLProdusRepository();
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



        //cerinta 2
        VBox rightSideBox = new VBox(5);
        GridPane labelsAndFieldsPane = new GridPane();
        labelsAndFieldsPane.setVgap(3.5);
        labelsAndFieldsPane.setHgap(3.5);

        Label pret_minim_Label = new Label("Pret Minim:");
        Label pret_Maxim_Label = new Label("Pret Maxim:");

        TextField pret_minim_TextField = new TextField();
        TextField pret_maxim_TextField = new TextField();

        labelsAndFieldsPane.add(pret_minim_Label, 0, 0);
        labelsAndFieldsPane.add(pret_minim_TextField, 1, 0);
        labelsAndFieldsPane.add(pret_Maxim_Label, 0, 1);
        labelsAndFieldsPane.add(pret_maxim_TextField, 1, 1);


        rightSideBox.getChildren().add(labelsAndFieldsPane);


        Button filtareButton = new Button("Filtare");

        rightSideBox.getChildren().add(filtareButton);

        filtareButton.setOnMouseClicked(mouseEvent -> {
            try {

                // Lista originală de produse
                ObservableList<Produs> originalList = FXCollections.observableArrayList(produsService.getProduse());

                // Dacă câmpurile de filtrare este goale, nu facem nicio modificare
                if (pret_minim_TextField.getText().isEmpty() && pret_maxim_TextField.getText().isEmpty()) {
                    produseObservableList.setAll(originalList);
                    Alert alert = new Alert(Alert.AlertType.WARNING);
                    alert.setTitle("EROARE filtrare");
                    alert.setHeaderText(null);
                    alert.setContentText("Nu s-au găsit rezultate pentru căutarea introdusă!");
                    alert.showAndWait();
                    return;
                }

                // Creăm o listă filtrată
                ObservableList<Produs> filteredList = FXCollections.observableArrayList();

                if (!pret_minim_TextField.getText().isEmpty()  && pret_maxim_TextField.getText().isEmpty())
                    for (Produs produs : originalList) {

                            if (produs.getPret() >= Integer.parseInt((pret_minim_TextField.getText()))) {
                                filteredList.add(produs);
                            }
                    }
                else if (pret_minim_TextField.getText().isEmpty() &&
                        !pret_maxim_TextField.getText().isEmpty())
                    for (Produs produs : originalList) {

                        if (produs.getPret() <= Integer.parseInt((pret_maxim_TextField.getText()))) {
                            filteredList.add(produs);
                        }
                    }
                else {
                    for (Produs produs : originalList) {

                        if (produs.getPret() <= Integer.parseInt((pret_maxim_TextField.getText())) && produs.getPret() >= Integer.parseInt((pret_minim_TextField.getText()))) {
                            filteredList.add(produs);
                        }
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


        //cerinta 3

        VBox cumparaturiBox = new VBox(5);

        GridPane cumparaturiPane = new GridPane();
        cumparaturiPane.setVgap(3.5);
        cumparaturiPane.setHgap(3.5);

        Label idLabel = new Label("ID-ul produsului de cumparat:");

        TextField idTextField = new TextField();

        cumparaturiPane.add(idLabel, 0, 0);
        cumparaturiPane.add(idTextField, 1, 0);

        GridPane pret_totalPane = new GridPane();
        pret_totalPane.setVgap(3.5);
        pret_totalPane.setHgap(3.5);

        Label pret_totalLabel = new Label("Pretul total = ");

        TextField pret_totalTextField = new TextField();
        pret_totalTextField.setText(String.valueOf(0));

        pret_totalPane.add(pret_totalLabel, 0, 0);
        pret_totalPane.add(pret_totalTextField, 1, 0);

        Button cumparaturiButton = new Button("Cumpara");

        // Butonul pentru filtrare
        cumparaturiButton.setOnMouseClicked(mouseEvent -> {
            try {
                String idText = idTextField.getText();

                if (produsService.getProdusById(Integer.parseInt(idText)) == null ) {
                    Alert alert = new Alert(Alert.AlertType.WARNING);
                    alert.setTitle("EROARE filtrare");
                    alert.setHeaderText(null);
                    alert.setContentText("Produsul cu id-ul = " + Integer.parseInt(idText) + " NU exista!");
                    alert.showAndWait();
                    return;
                }

                if (produsService.getProdusById(Integer.parseInt(idText)).getCantitate() == 0){
                    Alert alert = new Alert(Alert.AlertType.WARNING);
                    alert.setTitle("EROARE filtrare");
                    alert.setHeaderText(null);
                    alert.setContentText("Produsul cu id-ul = " + Integer.parseInt(idText) + " NU mai are stoc!");
                    alert.showAndWait();
                    return;
                }

                Produs produs_cautat =produsService.getProdusById(Integer.parseInt(idText));

                int pret_produs = produs_cautat.getPret();

                produsService.updateProdus(produs_cautat.getId(), produs_cautat.getMarca(), produs_cautat.getNume(),
                        pret_produs, produs_cautat.getCantitate());

                ObservableList<Produs> newList = FXCollections.observableArrayList(produsService.getProduse());
                produseObservableList.setAll(newList);

                int pret_actual = Integer.parseInt(pret_totalTextField.getText());

                pret_actual += pret_produs;
                pret_totalTextField.setText(String.valueOf(pret_actual));

                idTextField.clear();

            } catch (Exception e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Eroare");
                alert.setHeaderText(null);
                alert.setContentText("A apărut o eroare: " + e.getMessage());
                alert.showAndWait();
            }
        });

        cumparaturiBox.getChildren().addAll(cumparaturiPane,cumparaturiButton, pret_totalPane);

        mainBox.getChildren().addAll(produsTable, rightSideBox, cumparaturiBox);

        Scene scene = new Scene(mainBox, 1340, 820);
        stage.setTitle("My Shop Management System!");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    public void addEntities(SQLProdusRepository produsRepo) {
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
}