package org.example.a4javafx;

import Domain.*;
import Exceptions.RepositoryException;
import Repository.*;
import Service.CakeService;
import Service.OrderService;
import UI.MainMenu;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import util.Settings;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

//Add table, labels, text fields, buttons
//Use: HBox, VBox, GridPane

//Puteti citi mai mult la: https://jenkov.com/tutorials/javafx/tableview.html
//(un exemplu de documentatie+exemple, se pot folosi si altele)

//Horizontal box: layout in care asezam componentele
//pe o linie, pe orizontala

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException, RepositoryException {

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

        addEntities(cakeRepo, orderRepo, idGenerator);




        //layout-ul principal
        HBox mainBox = new HBox(5);

        //cream un tabel in care vom afisa datele torturilor
        TableView<Cake> cakeTable = new TableView<>();

        cakeTable.setPrefWidth(150);
        cakeTable.setPrefHeight(500);

        //cream cate o coloana pe rand
        //textul din paranteze este header-ul
        TableColumn<Cake, Integer> idColumn = new TableColumn<>("ID");
        TableColumn<Cake, String> typeColumn = new TableColumn<>("Type");

        //specificam cum se vor completa coloanele - ce camp dintr-un
        //obiect Cake vine pe fiecare coloana

        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        typeColumn.setCellValueFactory(new PropertyValueFactory<>("typeOfCake"));

        //adaugam coloanele la tabel
        cakeTable.getColumns().add(idColumn);
        cakeTable.getColumns().add(typeColumn);

        //cream o lista de cakes care se vor afisa in tabel
        //https://docs.oracle.com/javase/8/javafx/api/javafx/collections/ObservableList.html
        ObservableList<Cake> cakeList = FXCollections.observableArrayList(cakeService.getCakes());
        cakeTable.setItems(cakeList);


        //Vertical Box
        //https://openjfx.io/javadoc/13/javafx.graphics/javafx/scene/layout/VBox.html
        //componentele sunt aranjate pe o coloana, pe verticala
        //rightSideBox este unde vom pune label-urile si text field-urile
        //si butoanele

        VBox rightSideBox = new VBox(5);
        GridPane labelsAndFieldsPane = new GridPane();
        labelsAndFieldsPane.setVgap(3.5);
        labelsAndFieldsPane.setHgap(3.5);

        Label idLabel = new Label("ID Cake:");
        Label typeLabel = new Label("Type");
        TextField idTextField = new TextField();
        // Setăm câmpul de ID ca readonly (nu mai poate fi modificat)
        idTextField.setEditable(false);
        TextField typeTextField = new TextField();

        labelsAndFieldsPane.add(idLabel, 0, 0);
        labelsAndFieldsPane.add(idTextField, 1, 0);
        labelsAndFieldsPane.add(typeLabel, 0, 1);
        labelsAndFieldsPane.add(typeTextField, 1, 1);

        rightSideBox.getChildren().add(labelsAndFieldsPane);

        //new HBox pentru butoane
        HBox buttonBox = new HBox();
        Button addCakeButton = new Button("Add\nCake");
        Button deleteCakeButton = new Button("Delete\nCake");
        Button updateCakeButton = new Button("Update\nCake");

//        addCakeButton.setPrefHeight(80);
//        addCakeButton.setPrefWidth(80);

        buttonBox.getChildren().add(addCakeButton);
        buttonBox.getChildren().add(deleteCakeButton);
        buttonBox.getChildren().add(updateCakeButton);

        //aranjam butoanele in HBox sa fie centrate
        //https://openjfx.io/javadoc/13/javafx.graphics/javafx/geometry/Pos.html#BASELINE_CENTER
        buttonBox.setAlignment(Pos.BASELINE_CENTER);
        buttonBox.setSpacing(10);

        rightSideBox.getChildren().add(buttonBox);

        //set some space in between rightSideBox components
        //which are the grid pane and the buttonBox
        rightSideBox.setSpacing(15);

//        mainBox.getChildren().add(cakeTable);
//        mainBox.getChildren().add(rightSideBox);

        //cand apasam butonul addButon, se executa metoda handle
        //care preia continutul din textField-uri
        //si se foloseste de service ca sa adauge un Musician
        //cu datele din textField-uri (la fel cum vechiul ui se folosea de service
        //sa adauge ce se citea de la tastatura)
        //schimbam continutul musicianList prin setAll la noua lista, cu musician adaugat
        //daca se arunca o eroare (fie la conversia in int, fie
        //pentru ID duplicat, se afiseaza mesaj de eroare - Alert)

        addCakeButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                try{
                    // incerc sa folosesc idGenerator
                    String type = typeTextField.getText();
                    if (type.isEmpty())
                        throw new Exception("Type cannot be empty!");
                    cakeService.addCake(type);
                    cakeList.setAll(cakeService.getCakes());
                    System.out.println("Cake added succesfully");
                } catch (Exception e ){
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error");
                    alert.setContentText("An error has occurred: "+e.getMessage());
                    alert.show();
                }
                // Resetăm câmpurile după actualizare
                idTextField.clear();
                typeTextField.clear();
            }
        });

//        //permite selectarea simultana a mai multe randuri din tabel
//        //spre exemplu, CTRL+click mai multe randuri
//        cakeTable.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
//
//        cakeTable.setOnMouseClicked(new EventHandler<MouseEvent>() {
//            @Override
//            public void handle(MouseEvent mouseEvent) {
//                //luam din tabel lista de cakes selectati, afisam informatii despre torturi (in consola)
//                ObservableList<Cake> selectedCakes = cakeTable.getSelectionModel().getSelectedItems();
//                System.out.println("Selected cakes are:");
//                for (Cake c: selectedCakes) {
//                    System.out.println(c);
//                }
//            }
//        });

        //cu aceasta setare, putem selecta o singura linie din tabel
        cakeTable.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);

        //vrem ca atunci cand dam click e o linie din tabel, text field-urile
        //sa se populeze cu informatiil despre musician-ul din linia respectiva
        cakeTable.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                Cake selectedCake = cakeTable.getSelectionModel().getSelectedItem();
                idTextField.setText(String.valueOf(selectedCake.getId()));
                typeTextField.setText(selectedCake.getTypeOfCake());
            }
        });

        deleteCakeButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                try {
                    Cake selectedCake = cakeTable.getSelectionModel().getSelectedItem();
                    if (selectedCake == null ) {
                        throw new Exception("Please select a cake!");
                    }
                    int idToDelete = selectedCake.getId();
                    cakeService.deleteCake(idToDelete);
                    cakeList.setAll(cakeService.getCakes());
                    System.out.println("Cake deleted successfully");
                } catch (Exception e){
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error");
                    alert.setContentText("An error has occurred: "+e.getMessage());
                    alert.show();
                }
                // Resetăm câmpurile după actualizare
                idTextField.clear();
                typeTextField.clear();
            }
        });

        updateCakeButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                try {
                    // Obține tortul selectat din tabel
                    Cake selectedCake = cakeTable.getSelectionModel().getSelectedItem();
                    if (selectedCake == null) {
                        throw new Exception("Please select a cake!");
                    }

                    // Obține noul tip din TextField-ul "typeTextField"
                    String newType = typeTextField.getText();
                    if (newType == null || newType.isBlank()) {
                        throw new Exception("Type cannot be empty!");
                    }

                    // Apelăm metoda de actualizare din CakeService
                    cakeService.updateCake(selectedCake.getId(), newType);

                    // Reîmprospătăm lista de torturi din tabel
                    cakeList.setAll(cakeService.getCakes());

                    // Resetăm câmpurile după actualizare
                    idTextField.clear();
                    typeTextField.clear();
                    System.out.println("Cake updated successfully");
                } catch (Exception e) {
                    // Afișăm un mesaj de eroare în cazul unei probleme
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error:");
                    alert.setContentText("An error has occurred: " + e.getMessage());
                    alert.show();
                }
            }
        });


        // TableView pt Orders
        TableView<Order> orderTable = new TableView<>();

        orderTable.setPrefWidth(400);
        orderTable.setPrefHeight(800);

        // coloane
        TableColumn<Order, Integer> orderIdColumn = new TableColumn<>("ID");
        TableColumn<Order, String> orderCakesColumn = new TableColumn<>("Cakes");
        TableColumn<Order, Date> orderDateColumn = new TableColumn<>("Date");


        //specificam cum se vor completa coloanele - ce camp dintr-un
        //obiect Order vine pe fiecare coloana
        orderIdColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        orderCakesColumn.setCellValueFactory(data -> {
            ArrayList<Cake> cakes = data.getValue().getCakes();
            String cakesString = cakes.stream()
                    .map(c -> c.getId() + "-" + c.getTypeOfCake())
                    .reduce((s1, s2) -> s1 + ", " + s2)
                    .orElse("None");
            return new javafx.beans.property.SimpleStringProperty(cakesString);
        });
        orderDateColumn.setCellValueFactory(new PropertyValueFactory<>("date"));

        orderTable.getColumns().addAll(orderIdColumn, orderCakesColumn, orderDateColumn);

        //cream o lista de orders care se vor afisa in tabel
        ObservableList<Order> orderList = FXCollections.observableArrayList(orderService.getOrders());
        orderTable.setItems(orderList);

        // Right-side box for Order controls
        VBox orderBox = new VBox();

        GridPane orderForm = new GridPane();
        orderForm.setVgap(5);
        orderForm.setHgap(5);

        Label orderIdLabel = new Label("ID Order:");
        Label orderCakesLabel = new Label("Cakes:");
        Label orderDateLabel = new Label("Date:");


        TextField orderIdField = new TextField();
        orderIdField.setEditable(false); // nu se poate modifca
        TextField orderCakesField = new TextField(); // IDs of cakes, separate din virgula
        TextField orderDateField = new TextField(); // yyyy-MM-dd

        orderForm.add(orderIdLabel, 0, 0);
        orderForm.add(orderIdField, 1, 0);
        orderForm.add(orderCakesLabel, 0, 1);
        orderForm.add(orderCakesField, 1, 1);
        orderForm.add(orderDateLabel, 0, 2);
        orderForm.add(orderDateField, 1, 2);

        HBox orderButtons = new HBox(10);
        Button addOrderButton = new Button("Add\nOrder");
        Button updateOrderButton = new Button("Update\nOrder");
        Button deleteOrderButton = new Button("Delete\nOrder");
        orderButtons.getChildren().addAll(addOrderButton, updateOrderButton, deleteOrderButton);
        orderButtons.setAlignment(Pos.BASELINE_CENTER);
        orderButtons.setSpacing(10);

        // HBox pentru a plasa tabelul Orders și controalele pe orizontală
        HBox tableAndForm = new HBox(15);

        tableAndForm.getChildren().add(orderTable);

        // Vertical Box pentru butoane și text fields, aranjate vertical
        VBox orderControls = new VBox(10);
        orderControls.getChildren().addAll(orderForm, orderButtons);

        tableAndForm.getChildren().add(orderControls);

        orderBox.getChildren().add(tableAndForm); // Adăugăm noul layout în Order Box


        // Event handling for Order Table
        orderTable.setOnMouseClicked(event -> {
            Order selected = orderTable.getSelectionModel().getSelectedItem();
            if (selected != null) {
                orderIdField.setText(String.valueOf(selected.getId()));
                orderCakesField.setText(
                        selected.getCakes().stream()
                                .map(c -> String.valueOf(c.getId()))
                                .reduce((s1, s2) -> s1 + "," + s2)
                                .orElse("")
                );
                orderDateField.setText(new SimpleDateFormat("yyyy-MM-dd").format(selected.getDate()));
            }
        });


        addOrderButton.setOnMouseClicked(event -> {
            try {
                String[] cakeIds = orderCakesField.getText().split(",");
                ArrayList<Cake> cakes = new ArrayList<>();
                for (String id : cakeIds) {
                    if (cakeService.getCakeById(Integer.parseInt(id.trim())) == null ) {
                        throw new Exception("There is no cake with the id = " + id);
                    }
                    cakes.add(cakeService.getCakeById(Integer.parseInt(id.trim())));
                }
                Date date = new SimpleDateFormat("yyyy-MM-dd").parse(orderDateField.getText());
                orderService.addOrder(cakes, date);
                orderList.setAll(orderService.getOrders());
                orderIdField.clear();
                orderCakesField.clear();
                orderDateField.clear();
            } catch (Exception e) {
                showError("Add Order Error", e.getMessage());
            }
        });


        updateOrderButton.setOnMouseClicked(event -> {
            try {
                Order selected = orderTable.getSelectionModel().getSelectedItem();
                if (selected == null) {
                    throw new Exception("Please select an order first!");
                }
                String[] cakeIds = orderCakesField.getText().split(",");
                ArrayList<Cake> cakes = new ArrayList<>();
                for (String id : cakeIds) {
                    if (cakeService.getCakeById(Integer.parseInt(id.trim())) == null ) {
                        throw new Exception("There is no cake with the id = " + id);
                    }
                    cakes.add(cakeService.getCakeById(Integer.parseInt(id.trim())));
                }
                Date date = new SimpleDateFormat("yyyy-MM-dd").parse(orderDateField.getText());
                orderService.updateOrder(selected.getId(), cakes, date);
                orderList.setAll(orderService.getOrders());
                orderIdField.clear();
                orderCakesField.clear();
                orderDateField.clear();
            } catch (Exception e) {
                showError("Update Order Error", e.getMessage());
            }
        });


        deleteOrderButton.setOnMouseClicked(event -> {
            try {
                Order selected = orderTable.getSelectionModel().getSelectedItem();
                if (selected == null) {
                    throw new Exception("Select an order first!");
                }
                orderService.deleteOrder(selected.getId());
                orderList.setAll(orderService.getOrders());
                orderIdField.clear();
                orderCakesField.clear();
                orderDateField.clear();
            } catch (Exception e) {
                showError("Delete Order Error", e.getMessage());
            }
        });


        // PENTRU RAPOARTE:

        Button getCakesOrderedPerDayButton = new Button ("Cakes per DAY");
        Button getCakesOrderedPerMonthButton = new Button ("Cakes per MONTH");
        Button getMostOrderedCakesButton =  new Button ("Most ordered cakes");

        // Creăm un ListView pentru a arăta comenzile generate
        ListView<String> generatedOrdersListView = new ListView<>();
        generatedOrdersListView.setPrefHeight(200);

        // HBox pentru butoane de generare
        HBox generateButtonsBox = new HBox(10);
        generateButtonsBox.setAlignment(Pos.BASELINE_CENTER);
        generateButtonsBox.getChildren().addAll(getCakesOrderedPerDayButton, getCakesOrderedPerMonthButton, getMostOrderedCakesButton);

        // Adăugăm butoanele și lista
        VBox orderControlsBox = new VBox(10);
        orderControlsBox.getChildren().addAll( generateButtonsBox, generatedOrdersListView);

        getCakesOrderedPerDayButton.setOnAction(event -> {
            try {

                List<Map.Entry<Date, Integer>> cakesPerDay = orderService.getCakesOrderedPerDay();

                generatedOrdersListView.getItems().clear();

                for (Map.Entry<Date, Integer> entry : cakesPerDay) {
                    String entryText = entry.getKey() + " : " + entry.getValue() + " orders";
                    generatedOrdersListView.getItems().add(entryText);
                }

            } catch (Exception e) {
                showError("Error", "Failed to fetch cakes ordered per day: " + e.getMessage());
            }
        });

        getCakesOrderedPerMonthButton.setOnAction(event -> {
            try {

                List<Map.Entry<String, Integer>> cakesPerMonth = orderService.getCakesOrderedPerMonth();

                generatedOrdersListView.getItems().clear();

                for (Map.Entry<String, Integer> entry : cakesPerMonth) {
                    String entryText = entry.getKey() + " : " + entry.getValue() + " orders";
                    generatedOrdersListView.getItems().add(entryText);
                }
            } catch (Exception e) {
                showError("Error", "Failed to fetch cakes ordered per month: " + e.getMessage());
            }
        });

        getMostOrderedCakesButton.setOnAction(event -> {
            try {
                List<Map.Entry<Cake, Integer>> mostOrderedCakes = orderService.getMostOrderedCakes();

                generatedOrdersListView.getItems().clear();

                for (Map.Entry<Cake, Integer> entry : mostOrderedCakes) {
                    Cake cake = entry.getKey();
                    String entryText = "Cake " + cake.getId() + " : " + entry.getValue() + " orders";
                    generatedOrdersListView.getItems().add(entryText);
                }

            } catch (Exception e) {
                showError("Error", "Failed to fetch most ordered cakes: " + e.getMessage());
            }
        });

        mainBox.getChildren().addAll(cakeTable, rightSideBox, orderBox, orderControlsBox);

        Scene scene = new Scene(mainBox, 1340, 820);
        stage.setTitle("My pastry's cake order management system!");
        stage.setScene(scene);
        stage.show();

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

    public static void main(String[] args)  {
//        launch();
        String appMode = Settings.getInstance().getAppMode();

        switch (appMode.toLowerCase()) {
            case "cli" -> {
                // consola
                try {
                    MainMenu.runCli();
                } catch (Exception e) {
                    System.out.println("Error running CLI: " + e.getMessage());
                }
            }
            case "gui" -> {
                //  interfața grafică
                launch();
                break;
            }
            default -> {
                System.out.println("Invalid application mode specified in settings.properties: " + appMode);
                System.out.println("Valid options are 'cli' or 'gui'.");
            }
        }

    }

    private void showError(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setContentText(message);
        alert.show();
    }
}