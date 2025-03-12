import Domain.Cake;
import Domain.Order;
import Domain.OrderConvertor;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class OrderConvertorTest {

    private final OrderConvertor orderConvertor = new OrderConvertor(Order.class);
    private final SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

    @Test
    void testToString() {
        // Creăm obiecte de tip Cake
        Cake cake1 = new Cake(1, "Chocolate");
        Cake cake2 = new Cake(2, "Vanilla");

        // Creăm obiectul Order
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake1);
        cakes.add(cake2);
        Order order = new Order(101, cakes, new Date());

        // Converim Order la String
        String orderString = orderConvertor.toString(order);

        // Formatul așteptat: "101;1-Chocolate,2-Vanilla;yyyy-MM-dd"
        String expectedString = "101;1-Chocolate,2-Vanilla;" + dateFormat.format(order.getDate());
        assertEquals(expectedString, orderString);
    }

    @Test
    void testFromString_Valid() {
        // String valid de input
        String input = "101;1-Chocolate,2-Vanilla;2024-11-12";

        // Converim String la Order
        Order order = orderConvertor.fromString(input);

        // Verificăm valorile obiectului Order
        assertEquals(101, order.getId());
        assertEquals(2, order.getCakes().size());
        assertEquals("Chocolate", order.getCakes().get(0).getTypeOfCake());
        assertEquals("Vanilla", order.getCakes().get(1).getTypeOfCake());

        try {
            Date expectedDate = dateFormat.parse("2024-11-12");
            assertEquals(expectedDate, order.getDate());
        } catch (Exception e) {
            fail("Date parsing failed");
        }
    }

    @Test
    void testFromString_InvalidOrderFormat() {
        // String invalid de input (lipsă câmpuri)
        String input = "101;1-Chocolate,2-Vanilla";

        // Ar trebui să arunce o excepție
        assertThrows(RuntimeException.class, () -> orderConvertor.fromString(input),
                "Expected RuntimeException due to invalid input format");
    }

    @Test
    void testFromString_InvalidCakeFormat() {
        // String invalid de input (format incorect pentru torturi)
        String input = "101;1Chocolate,2Vanilla;2024-11-12";

        // Ar trebui să arunce o excepție
        assertThrows(RuntimeException.class, () -> orderConvertor.fromString(input),
                "Expected RuntimeException due to invalid cake format");
    }

    @Test
    void testFromString_InvalidDateFormat() {
        // String invalid de input (format incorect pentru dată)
        String input = "101;1-Chocolate,2-Vanilla;2024,11-31";

        // Ar trebui să arunce o excepție (data nu există)
        assertThrows(RuntimeException.class, () -> orderConvertor.fromString(input),
                "Expected RuntimeException due to invalid date format");
    }

    @Test
    void testFromString_InvalidOrderIdFormat() {
        // String invalid de input (ID-ul comenzii nu este un număr valid)
        String input = "abc;1-Chocolate,2-Vanilla;2024-11-12";

        // Ar trebui să arunce o excepție
        assertThrows(RuntimeException.class, () -> orderConvertor.fromString(input),
                "Expected RuntimeException due to invalid order ID format");
    }

    @Test
    void testFromString_EmptyCakes() {
        // String valid cu nicio prăjitură
        String input = "101;;2024-11-12";

        // Converim String la Order
        Order order = orderConvertor.fromString(input);

        // Verificăm valorile obiectului Order
        assertEquals(101, order.getId());
        assertTrue(order.getCakes().isEmpty(), "The cakes list should be empty.");
    }

    @Test
    void testToString_EmptyCakes() {
        // Creăm un Order cu o listă de torturi goală
        Order order = new Order(102, new ArrayList<>(), new Date());

        // Converim Order la String
        String orderString = orderConvertor.toString(order);

        // Formatul așteptat ar trebui să fie "102;;yyyy-MM-dd"
        String expectedString = "102;;" + dateFormat.format(order.getDate());
        assertEquals(expectedString, orderString);
    }
}
