import Domain.Cake;
import Domain.IDGenerator;
import Exceptions.RepositoryException;
import Repository.MemoryRepository;
import Service.CakeService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

public class CakeServiceTest {

    private static final String TEST_FILE = "testIdFile.txt";  // File used by IDGenerator
    private MemoryRepository<Cake> cakeRepo;
    private IDGenerator idGenerator;
    private CakeService cakeService;

    @BeforeEach
    public void setup() {
        // Clean up the test file before each test
        try {
            Files.deleteIfExists(Paths.get(TEST_FILE));  // Delete if the file exists
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Create the repository and IDGenerator for each test
        cakeRepo = new MemoryRepository<>();
        idGenerator = new IDGenerator(TEST_FILE);
        cakeService = new CakeService(cakeRepo, idGenerator);
    }

    @Test
    public void testAddCake_Success() throws RepositoryException {
        // Act
        cakeService.addCake("Chocolate Cake");

        // Assert: Verify that the cake has been added to the repository
        ArrayList<Cake> cakes = cakeService.getCakes();
        assertEquals(1, cakes.size());
        assertEquals("Chocolate Cake", cakes.get(0).getTypeOfCake());
    }

    @Test
    public void testAddCake_GenerateUniqueId() throws RepositoryException {
        // Act: Add cakes and verify the unique ID generation
        cakeService.addCake("Chocolate Cake");
        cakeService.addCake("Vanilla Cake");

        // Assert: Check if the generated IDs are unique and correctly incremented
        ArrayList<Cake> cakes = cakeService.getCakes();
        assertEquals(2, cakes.size());
        assertEquals(100, cakes.get(0).getId());
        assertEquals(101, cakes.get(1).getId());
    }

    @Test
    public void testGetCakes_EmptyRepo() {
        // Act & Assert: Trying to get cakes when no cakes have been added should throw an exception
        NullPointerException exception = assertThrows(NullPointerException.class, () -> {
            cakeService.getCakes();
        });
        assertEquals("There are no cakes yet!", exception.getMessage());
    }

    @Test
    public void testUpdateCake_Success() throws RepositoryException {
        // Arrange: Add a cake
        cakeService.addCake("Chocolate Cake");
        ArrayList<Cake> cakes = cakeService.getCakes();
        int cakeId = cakes.get(0).getId();

        // Act: Update the cake type
        cakeService.updateCake(cakeId, "Strawberry Cake");

        // Assert: Verify that the cake was updated
        Cake updatedCake = cakeService.getCakeById(cakeId);
        assertEquals("Strawberry Cake", updatedCake.getTypeOfCake());
    }

    @Test
    public void testUpdateCake_CakeNotFound() {
        // Act & Assert: Trying to update a non-existing cake should throw an exception
        RepositoryException exception = assertThrows(RepositoryException.class, () -> {
            cakeService.updateCake(999, "Chocolate Cake");  // Using a non-existent ID
        });
        assertTrue(exception.getMessage().contains("Cake with id = 999 does not exist"));
    }

    @Test
    public void testDeleteCake_Success() throws RepositoryException {
        // Arrange: Add a cake
        cakeService.addCake("Chocolate Cake");
        cakeService.addCake("Vanilla Cake");
        ArrayList<Cake> cakes = cakeService.getCakes();
        int cakeId = cakes.get(0).getId();

        // Act: Delete the cake
        cakeService.deleteCake(cakeId);

        // Assert: Verify that the cake is deleted
        assertEquals(1, cakeService.getCakes().size());
    }

    @Test
    public void testDeleteCake_CakeNotFound() {
        // Act & Assert: Trying to delete a non-existing cake should throw an exception
        RepositoryException exception = assertThrows(RepositoryException.class, () -> {
            cakeService.deleteCake(999);  // Using a non-existent ID
        });
        assertTrue(exception.getMessage().contains("There is no entity with this id = 999"));
    }

    @Test
    public void testSaveCurrentId_AfterMultipleCakes() throws RepositoryException {
        // Act: Add some cakes
        cakeService.addCake("Chocolate Cake");
        cakeService.addCake("Vanilla Cake");

        // Assert: The file should contain the last used ID (101)
        try {
            String content = new String(Files.readAllBytes(Paths.get(TEST_FILE)));
            assertEquals("101", content.trim());  // The last ID used should be 102
        } catch (IOException e) {
            fail("Failed to read ID from file.");
        }
    }
}
