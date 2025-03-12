import Domain.Cake;
import Domain.Order;
import Domain.IDGenerator;
import Exceptions.RepositoryException;
import Repository.MemoryRepository;
import Service.OrderService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;

public class OrderServiceTest {

    private static final String TEST_FILE = "testOrderIdFile.txt"; // File used by IDGenerator
    private MemoryRepository<Order> orderRepo;
    private IDGenerator idGenerator;
    private OrderService orderService;

    @BeforeEach
    public void setup() {
        // Clean up the test file before each test
        try {
            Files.deleteIfExists(Paths.get(TEST_FILE));  // Delete if the file exists
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Create the repository and IDGenerator for each test
        orderRepo = new MemoryRepository<>();
        idGenerator = new IDGenerator(TEST_FILE);
        orderService = new OrderService(orderRepo, idGenerator);
    }

    @Test
    public void testAddOrder_Success() throws RepositoryException {
        // Arrange: Create cakes for the order
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(new Cake(1, "Chocolate Cake"));
        cakes.add(new Cake(2, "Vanilla Cake"));
        Date date = new Date();

        // Act: Add the order
        orderService.addOrder(cakes, date);

        // Assert: Verify that the order has been added to the repository
        ArrayList<Order> orders = orderService.getOrders();
        assertEquals(1, orders.size());
        assertEquals(cakes, orders.get(0).getCakes());
        assertEquals(date, orders.get(0).getDate());
    }

    @Test
    public void testAddOrder_GenerateUniqueId() throws RepositoryException {
        // Arrange: Create cakes for the orders
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(new Cake(1, "Chocolate Cake"));
        cakes.add(new Cake(2, "Vanilla Cake"));
        Date date = new Date();

        // Act: Add the first order
        orderService.addOrder(cakes, date);

        // Add another order to test ID generation
        cakes.clear();
        cakes.add(new Cake(3, "Strawberry Cake"));
        cakes.add(new Cake(4, "Lemon Cake"));
        orderService.addOrder(cakes, date);

        // Assert: Verify that the generated order IDs are unique
        ArrayList<Order> orders = orderService.getOrders();
        assertEquals(2, orders.size());
        assertEquals(100, orders.get(0).getId()); // First order
        assertEquals(101, orders.get(1).getId()); // Second order
    }

    @Test
    public void testGetOrders_EmptyRepo() {
        // Act & Assert: Trying to get orders when no orders have been added should throw an exception
        NullPointerException exception = assertThrows(NullPointerException.class, () -> {
            orderService.getOrders();
        });
        assertEquals("There are no orders yet!", exception.getMessage());
    }

    @Test
    public void testUpdateOrder_Success() throws RepositoryException {
        // Arrange: Create and add an order
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(new Cake(1, "Chocolate Cake"));
        Date date = new Date();
        orderService.addOrder(cakes, date);

        // Get the ID of the added order
        ArrayList<Order> orders = orderService.getOrders();
        int orderId = orders.get(0).getId();

        // Prepare updated cakes
        cakes.clear();
        cakes.add(new Cake(3, "Strawberry Cake"));
        cakes.add(new Cake(4, "Lemon Cake"));

        // Act: Update the order
        orderService.updateOrder(orderId, cakes, date);

        // Assert: Verify that the order has been updated
        Order updatedOrder = orderService.getOrders().get(0);
        assertEquals(cakes, updatedOrder.getCakes());
        assertEquals(date, updatedOrder.getDate());
    }

    @Test
    public void testUpdateOrder_OrderNotFound() {
        // Act & Assert: Trying to update a non-existing order should throw an exception
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(new Cake(1, "Chocolate Cake"));
        Date date = new Date();

        RepositoryException exception = assertThrows(RepositoryException.class, () -> {
            orderService.updateOrder(999, cakes, date);  // Using a non-existent ID
        });
        assertTrue(exception.getMessage().contains("Order with id = 999 does not exist"));
    }

    @Test
    public void testDeleteOrder_Success() throws RepositoryException {
        // Arrange: Create and add an order
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(new Cake(1, "Chocolate Cake"));
        Date date = new Date();
        orderService.addOrder(cakes, date);

        ArrayList<Cake> cakes2 = new ArrayList<>();
        cakes2.add(new Cake(1, "Chocolate Cake"));
        cakes2.add(new Cake(2, "Vanilla Cake"));
        orderService.addOrder(cakes2, date);

        // Get the ID of the added order
        ArrayList<Order> orders = orderService.getOrders();
        int orderId = orders.get(0).getId();

        // Act: Delete the order
        orderService.deleteOrder(orderId);

        // Assert: Verify that the order is deleted
        assertEquals(1, orderService.getOrders().size());
    }

    @Test
    public void testDeleteOrder_OrderNotFound() {
        // Act & Assert: Trying to delete a non-existing order should throw an exception
        RepositoryException exception = assertThrows(RepositoryException.class, () -> {
            orderService.deleteOrder(999);  // Using a non-existent ID
        });
        assertTrue(exception.getMessage().contains("There is no entity with this id = 999"));
    }

    @Test
    public void testSaveCurrentId_AfterMultipleOrders() throws RepositoryException {
        // Act: Add some orders
        ArrayList<Cake> cakes1 = new ArrayList<>();
        cakes1.add(new Cake(1, "Chocolate Cake"));
        Date date = new Date();
        orderService.addOrder(cakes1, date);

        ArrayList<Cake> cakes2 = new ArrayList<>();
        cakes2.add(new Cake(2, "Vanilla Cake"));
        orderService.addOrder(cakes2, date);

        // Assert: The file should contain the last used ID (102)
        try {
            String content = new String(Files.readAllBytes(Paths.get(TEST_FILE)));
            assertEquals("101", content.trim());  // The last ID used should be 102
        } catch (IOException e) {
            fail("Failed to read ID from file.");
        }
    }
}
