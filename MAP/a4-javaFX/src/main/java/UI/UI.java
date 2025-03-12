package UI;

import Domain.Cake;
import Domain.Order;
import Exceptions.RepositoryException;
import Service.CakeService;
import Service.OrderService;

import java.sql.SQLOutput;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;


public class UI {
    private static OrderService orderService;
    private static CakeService cakeService;

    public UI(OrderService orderService, CakeService cakeService) {

        UI.orderService = orderService;
        UI.cakeService = cakeService;
    }

    public static void placeOrder(Scanner scanner)  {
        viewCakes(scanner);

        ArrayList<Cake> selectedCakes = new ArrayList<>();
        boolean running = true;
        int count = 0;

        while (running) {
            System.out.print("Enter cake ID (or type 'stop' to finish): ");
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("stop")) {
                running = false;

            } else {
                try {
                    int cakeId = Integer.parseInt(input);

                    Cake cake = cakeService.getCakeById(cakeId);
                    if (cake != null) {
                        selectedCakes.add(cake);
                        System.out.println("Cake added: " + cake.getTypeOfCake());
                        count++;
                    } else {
                        System.out.println("No cake found with ID: " + cakeId);
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Please enter a valid ID or type 'stop'.");
                } catch (Exception e) {
                    System.out.println("Exception: " + e.getMessage());
                }
            }
        }

        if (count != 0) {
            System.out.println("Enter the date of the oder: yyyy-mm-dd");
            String date = scanner.nextLine();
            Date orderDate = parseDate(date);

            try {
                orderService.addOrder(selectedCakes, orderDate);
                System.out.println("Order placed successfully!");
            } catch (RepositoryException e) {
                System.out.println("Failed to place the order: " + e.getMessage());
            }
        }
        else {
            System.out.println("Each order must have at least one cake assigned!");
        }

        }

        public static void viewOrders (Scanner scanner) {
            try {
                ArrayList<Order> listOfOrders = orderService.getOrders();
                System.out.println("The placed orders at this moment are: ");
                for (Order order : orderService.getOrders()) {
                    System.out.println(order);
                }
                orderService.getOrders();
            } catch (NullPointerException e) {
                System.out.println(e.getMessage());
            }

        }
        public static void cancelOrder (Scanner scanner){
            System.out.println("Please enter the id of the order that you want to cancel: ");
            int id = scanner.nextInt();

            try {
                orderService.deleteOrder(id);
                System.out.println("The delete was successful!");
            } catch (RepositoryException e) {

                System.out.println(e.getMessage());
                System.out.println("Try again please!");
            }

        }
        public static void updateOrder(Scanner scanner) {
            System.out.println("Please enter the ID of the order you want to update: ");
            int id = scanner.nextInt();
            scanner.nextLine();

            viewCakes(scanner);


            ArrayList<Cake> newCakes = new ArrayList<>();
            boolean addingCakes = true;
            System.out.println("Enter the IDs of the cakes you want to add to the order (type 'stop' to finish): ");
            while (addingCakes) {
                String cakeInput = scanner.nextLine();
                if (cakeInput.equalsIgnoreCase("stop")) {
                    addingCakes = false;
                } else {
                    try {
                        int cakeId = Integer.parseInt(cakeInput);
                        Cake cake = cakeService.getCakeById(cakeId);
                        if (cake != null) {
                            newCakes.add(cake);
                            System.out.println("Added cake: " + cake.getTypeOfCake());
                        } else {
                            System.out.println("No cake found with ID: " + cakeId);
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Please enter a valid cake ID or 'stop' to finish.");
                    }
                }
            }


            System.out.println("Enter the new order date (yyyy-MM-dd): ");
            String dateInput = scanner.nextLine();
            Date newDate = parseDate(dateInput);

            if (newDate == null) {
                System.out.println("Invalid date format. Update cancelled.");
                return;
            }


            try {
                orderService.updateOrder(id, newCakes, newDate);
                System.out.println("The order was updated successfully!");
            } catch (RepositoryException e) {
                System.out.println("Failed to update the order: " + e.getMessage());
            }
        }


        private static Date parseDate(String dateInput) {
            try {
                return new SimpleDateFormat("yyyy-MM-dd").parse(dateInput);
            } catch (ParseException e) {
                System.out.println("Invalid date format! Please use YYYY-MM-DD.");
                return null;
            }
        }

    public static void addNewCake (Scanner scanner){
            System.out.println("Please enter the type of the cake: ");
            String type = scanner.nextLine();
            try {
                cakeService.addCake(type);
                System.out.println("The cake has been added successfully!");
            } catch (RepositoryException e) {
                System.out.println(e.getMessage());
                System.out.println("Try again please!");
            }

        }
        public static void viewCakes(Scanner scanner){

            try {
                ArrayList<Cake> listOfCakes = cakeService.getCakes();
                System.out.println("The available cakes at this moment are: ");
                for (Cake cake : cakeService.getCakes()) {
                    System.out.println(cake);
                }
                cakeService.getCakes();
            } catch (NullPointerException e) {
                System.out.println(e.getMessage());
            }


        }
        public static void deleteCake (Scanner scanner){
            System.out.println("Please enter the id of the cake that you want to delete: ");
            int id = scanner.nextInt();

            try {
                cakeService.deleteCake(id);
                System.out.println("The delete was successful!");
            } catch (RepositoryException e) {

                System.out.println(e.getMessage());
                System.out.println("Try again please!");
            }


        }
        public static void updateCake (Scanner scanner){
            System.out.println("Please enter the id of the cake that you want to update: ");
            int id = scanner.nextInt();
            scanner.nextLine();
            System.out.println("Please enter the new type of the cake: ");
            String type = scanner.nextLine();

            try {
                cakeService.updateCake(id, type);
                System.out.println("The update was successful!");
            } catch (RepositoryException e) {

                System.out.println(e.getMessage());
                System.out.println("Try again please!");
            }
        }

    public static void getCakesOrderedPerDay(Scanner scanner) {
        System.out.println("The number of cakes ordered on each DAY in descending order:");
        try {
            List<Map.Entry<Date, Integer>> listCakes = orderService.getCakesOrderedPerDay();
            for (Map.Entry<Date, Integer> entry : listCakes) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }
        catch (RepositoryException e) {
            System.out.println("Error:" + e.getMessage());

        }
    }

    public static void getCakesOrderedPerMonth(Scanner scanner) {
        System.out.println("The number of cakes ordered on each MONTH in descending order:");
        try {
            List<Map.Entry<String, Integer>> listCakes = orderService.getCakesOrderedPerMonth();
            for (Map.Entry<String, Integer> entry : listCakes) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }
        catch (RepositoryException e) {
            System.out.println("Error:" + e.getMessage());

        }
    }

    public static void getMostOrderedCakes(Scanner scanner) {
        System.out.println("Most ordered cakes ordered in descending order:");
        try {
            List<Map.Entry<Cake, Integer>> mostOrderedCakes = orderService.getMostOrderedCakes();

            for (Map.Entry<Cake, Integer> entry : mostOrderedCakes) {
                Cake cake = entry.getKey();
                int orderCount = entry.getValue();
                System.out.println("Cake: " + cake.getId() + " - Total orders: " + orderCount);
            }
        }
        catch (RepositoryException e) {
            System.out.println("Error:" + e.getMessage());

        }
    }
}
