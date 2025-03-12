package Domain;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class OrderConvertor extends EntityConvertor<Order> {


    private final SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

    public OrderConvertor(Class<Order> entityClass) {
        super(entityClass);
    }


    @Override
    public String toString(Order order) {
        StringBuilder cakesAsString = new StringBuilder();

        // Convertim lista de torturi în formatul dorit: "idTort1-numeTort1;idTort2-numeTort2;....;idTortN-numeTortN"
        for (int i = 0; i < order.getCakes().size(); i++) {
            Cake cake = order.getCakes().get(i);
            cakesAsString.append(cake.getId()).append("-").append(cake.getTypeOfCake());

            // Adăugăm separatorul ';' între torturi, dar nu după ultimul
            if (i < order.getCakes().size() - 1) {
                cakesAsString.append(",");
            }
        }

        // Formatăm data în "yyyy-MM-dd"
        String formattedDate = dateFormat.format(order.getDate());

        // Formatul va fi: "id;idTort1-numeTort1;idTort2-numeTort2;date"
        return order.getId() + ";" + cakesAsString + ";" + formattedDate;
    }

    @Override
    public Order fromString(String string) {
        String[] tokens = string.split(";");

        // Verificăm dacă formatul este corect: id, lista de torturi și data
        if (tokens.length != 3) {
            throw new RuntimeException("Invalid input format for Order. Expected format: 'id;idTort1-numeTort1;idTort2-numeTort2;date'");
        }

        try {
            // Extragem și convertim ID-ul comenzii
            int id = Integer.parseInt(tokens[0].trim());

            // Extragem lista de torturi folosind metoda getCakes
            ArrayList<Cake> cakes = getCakes(tokens);

            // Extragem și convertim data
            String dateString = tokens[2].trim();
            Date date = dateFormat.parse(dateString);

            // Returnăm un nou obiect Order
            return new Order(id, cakes, date);

        } catch (NumberFormatException e) {
            throw new RuntimeException("Order ID and Cake ID must be integer values!");
        } catch (ParseException e) {
            throw new RuntimeException("Invalid date format! Expected format: yyyy-MM-dd");
        }
    }

    private static ArrayList<Cake> getCakes(String[] tokens) {
        String cakesString = tokens[1].trim();
        ArrayList<Cake> cakes = new ArrayList<>();
        if (!cakesString.isEmpty()) {
            String[] cakesArray = cakesString.split(",");
            for (String cakeData : cakesArray) {
                // Extragem id-ul și numele tortului din formatul "id-numeTort"
                String[] cakeTokens = cakeData.split("-");
                if (cakeTokens.length != 2) {
                    throw new RuntimeException("Invalid cake format! Expected format: 'id-numeTort'");
                }

                int cakeId = Integer.parseInt(cakeTokens[0].trim());
                String cakeName = cakeTokens[1].trim();

                // Cream obiectul Cake
                Cake cake = new Cake(cakeId, cakeName);
                cakes.add(cake);
            }
        }
        return cakes;
    }

}

