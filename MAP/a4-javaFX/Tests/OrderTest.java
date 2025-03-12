import Domain.Cake;
import Domain.Order;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Date;

public class OrderTest {
    Cake cake1 = new Cake(1, "Chocolate");
    Cake cake2 = new Cake(2, "Vanilla");
    Date date = new Date();

    @Test
    public void testOrderCreation() {
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake1);
        cakes.add(cake2);

        Order order = new Order(1, cakes, date);

        Assertions.assertEquals(1, order.getId(), "The order ID should be 1");
        Assertions.assertEquals(2, order.getCakes().size(), "The order should contain 2 cakes");
        Assertions.assertEquals("Chocolate", order.getCakes().get(0).getTypeOfCake(), "The first cake type should be 'Chocolate'");
        Assertions.assertEquals("Vanilla", order.getCakes().get(1).getTypeOfCake(), "The second cake type should be 'Vanilla'");
        Assertions.assertNotNull(order.getDate(), "The order date should not be null");
    }

    @Test
    public void testToString() {
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake1);
        cakes.add(cake2);

        Order order = new Order(1, cakes, date);

        // Verificăm dacă metoda toString returnează un format corect
        String expectedString = "Order ID: 1, Date: " + date + ", Cakes: 1-Chocolate; 2-Vanilla";
        Assertions.assertTrue(order.toString().contains("Order ID: 1"), "The toString method should include the order ID");
        Assertions.assertTrue(order.toString().contains("1-Chocolate"), "The toString method should correctly format the first cake");
        Assertions.assertTrue(order.toString().contains("2-Vanilla"), "The toString method should correctly format the second cake");
    }

    @Test
    public void testGetAndSetCakes() {
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake1);
        cakes.add(cake2);

        Order order = new Order(1, cakes, new Date());

        Assertions.assertEquals(2, order.getCakes().size(), "The order should contain 2 cakes");
        Assertions.assertEquals("Chocolate", order.getCakes().get(0).getTypeOfCake(), "The first cake should be Chocolate");
        Assertions.assertEquals("Vanilla", order.getCakes().get(1).getTypeOfCake(), "The second cake should be Vanilla");

        // Adăugăm un nou tort și verificăm actualizarea
        Cake cake3 = new Cake(3, "Strawberry");
        ArrayList<Cake> newCakes = new ArrayList<>();
        newCakes.add(cake3);
        order.setCakes(newCakes);

        Assertions.assertEquals(1, order.getCakes().size(), "The order should contain 1 cake after update");
        Assertions.assertEquals("Strawberry", order.getCakes().get(0).getTypeOfCake(), "The cake type should be Strawberry after update");
    }

    @Test
    public void testGetAndSetDate() {
        Date date1 = new Date();
        Date date2 = new Date(date1.getTime() + 1000000);

        Order order = new Order(1, new ArrayList<>(), date1);

        Assertions.assertEquals(date1, order.getDate(), "The order date should be the initial date");

        order.setDate(date2);

        Assertions.assertEquals(date2, order.getDate(), "The order date should be updated to the new date");
    }
}