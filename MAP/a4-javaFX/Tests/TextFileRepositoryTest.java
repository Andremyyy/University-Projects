import Domain.Cake;
import Domain.EntityConvertor;
import Domain.Order;
import Domain.OrderConvertor;
import Exceptions.RepositoryException;
import Repository.TextFileRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.Date;
import static org.junit.jupiter.api.Assertions.*;

public class TextFileRepositoryTest {

    private static final String TEST_FILE_NAME = "test_orders.txt";
    private TextFileRepository<Order> repository;
    private EntityConvertor<Order> orderConvertor;

    @BeforeEach
    void setUp() {
        // Initialize the converter and repository before each test
        orderConvertor = new OrderConvertor(Order.class);
        repository = new TextFileRepository<>(TEST_FILE_NAME, orderConvertor);
    }

    @AfterEach
    void tearDown() {
        // Delete the test file after each test
        File file = new File(TEST_FILE_NAME);
        if (file.exists()) {
            file.delete();
        }
    }

    @Test
    void testAddEntity() throws RepositoryException {
        // Create a new Cake object
        Cake cake = new Cake(1, "Chocolate");

        // Create an ArrayList of cakes (it should be ArrayList, not List.of)
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake);

        // Create an Order object
        Order order = new Order(1, cakes, new Date());

        // Add the entity to the repository
        repository.add(order);

        // Check if the file was saved correctly
        File file = new File(TEST_FILE_NAME);
        assertTrue(file.exists(), "File should exist after adding an entity.");

        // Check if the entity was correctly written to the file
        try (BufferedReader br = new BufferedReader(new FileReader(TEST_FILE_NAME))) {
            String line = br.readLine();
            assertNotNull(line, "File should contain data.");
            assertTrue(line.contains("1"), "Line should contain the order ID.");
        } catch (IOException e) {
            fail("IOException while reading saved file");
        }
    }

    @Test
    void testLoadFile_EmptyFile() throws RepositoryException {
        // Create a new empty file
        File file = new File(TEST_FILE_NAME);
        try {
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            }
        } catch (IOException e) {
            fail("IOException while creating the file");
        }

        // Test loading an empty file (it should not throw any errors)
        repository = new TextFileRepository<>(TEST_FILE_NAME, orderConvertor);

        // Verify that no entities are loaded from the file
        assertEquals(0, repository.getEntities().size(), "Repository should contain no entities when the file is empty.");
    }

    @Test
    void testLoadFile_InvalidData() throws RepositoryException {
        // Write some invalid data to the file
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(TEST_FILE_NAME))) {
            bw.write("Invalid data that cannot be parsed");
            bw.newLine();
            bw.write("1;1-InvalidCake;2024-12-01"); // A valid line, for comparison
        } catch (IOException e) {
            fail("IOException while writing invalid data to the file");
        }

        // Load the file, expecting it to ignore invalid lines
        repository = new TextFileRepository<>(TEST_FILE_NAME, orderConvertor);

        // Check that the repository contains only valid entities
        assertEquals(1, repository.getEntities().size(), "Repository should contain one valid entity after ignoring invalid lines.");
    }

    @Test
    void testSaveFile_IOError() {
        // Simulate a file IO error by using an invalid file path or permissions
        String invalidFileName = "/invalid/directory/test_orders.txt";
        repository = new TextFileRepository<>(invalidFileName, orderConvertor);

        // Try to save and expect a RepositoryException
        assertThrows(RepositoryException.class, () -> {
            repository.saveFile();
        }, "RepositoryException should be thrown when there is an IO error.");
    }

    @Test
    void testRemoveEntity() throws RepositoryException {
        // Add an order
        Cake cake = new Cake(1, "Chocolate");
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake);
        Order order = new Order(1, cakes, new Date());
        repository.add(order);

        // Remove the order by ID
        repository.removeById(1);

        // Check if the order has been removed
        assertEquals(0, repository.getEntities().size(), "Repository should be empty after removing the order.");
    }

    @Test
    void testUpdateEntity() throws RepositoryException {
        // Add an order
        Cake cake = new Cake(1, "Chocolate");
        ArrayList<Cake> cakes = new ArrayList<>();
        cakes.add(cake);
        Order order = new Order(1, cakes, new Date());
        repository.add(order);

        // Update the order
        Cake newCake = new Cake(2, "Vanilla");
        ArrayList<Cake> newCakes = new ArrayList<>();
        newCakes.add(newCake);
        Order updatedOrder = new Order(1, newCakes, new Date());
        repository.update(updatedOrder);

        // Check if the update was successful
        assertEquals("Vanilla", repository.getEntities().get(0).getCakes().get(0).getTypeOfCake(), "The cake type should be updated.");
    }
}
