import Domain.Entity;
import Exceptions.RepositoryException;
import Repository.JsonFileRepository;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class JsonFileRepositoryTest {

    static class DummyEntity extends Entity {
        private final String name;

        @JsonCreator
        public DummyEntity(@JsonProperty("id") int id, @JsonProperty("name") String name) {
            super(id);
            this.name = name;
        }


        public String getName() {
            return name;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            DummyEntity that = (DummyEntity) obj;
            return this.getId() == that.getId() && this.name.equals(that.name);
        }
    }

    private static final String testFileName = "test_data.json";
    private JsonFileRepository<DummyEntity> repository;

    @BeforeEach
    void setUp() {
        try {
            repository = new JsonFileRepository<>(testFileName, DummyEntity.class);
        } catch (RepositoryException e) {
            fail("Initialization failed: " + e.getMessage());
        }
    }

    @AfterEach
    void tearDown() {
        File file = new File(testFileName);
        if (file.exists()) {
            file.setWritable(true);
            assertTrue(file.delete(), "Failed to delete test file.");
        }
    }

    @Test
    void testInitialization_FileDoesNotExist() {
        File file = new File(testFileName);

        // Asigurăm că fișierul de test nu există înainte de testare
        if (file.exists()) {
            assertTrue(file.delete(), "Failed to delete existing test file before initialization.");
        }

        // Inițializăm repository-ul și verificăm dacă nu aruncă excepții
        assertDoesNotThrow(() -> {
            new JsonFileRepository<>(testFileName, DummyEntity.class);
        }, "Initializing with a non-existent file should not throw an exception.");

        // Verificăm dacă fișierul este creat după inițializare
        assertTrue(file.exists(), "The file should be created after initialization.");
    }

    @Test
    void testSaveAndLoadData_Success() {
        try {
            DummyEntity entity1 = new DummyEntity(1, "Entity1");
            DummyEntity entity2 = new DummyEntity(2, "Entity2");

            repository.add(entity1);
            repository.add(entity2);
            repository.saveFile();

            // Creăm un nou repository pentru a încărca datele
            JsonFileRepository<DummyEntity> newRepository = new JsonFileRepository<>(testFileName, DummyEntity.class);
            List<DummyEntity> entities = newRepository.getEntities();

            assertEquals(2, entities.size(), "Repository should contain 2 entities after loading.");
            assertTrue(entities.contains(entity1), "Loaded data should contain Entity1.");
            assertTrue(entities.contains(entity2), "Loaded data should contain Entity2.");
        } catch (RepositoryException e) {
            fail("Exception during save and load test: " + e.getMessage());
        }
    }

    @Test
    void testLoadFile_FileIsEmpty() {
        File file = new File(testFileName);

        // Creăm directorul părinte dacă nu există
        File parentDir = file.getParentFile();
        if (parentDir != null && !parentDir.exists()) {
            assertTrue(parentDir.mkdirs(), "Failed to create parent directory for test file.");
        }

        // Ștergem fișierul dacă există deja
        if (file.exists()) {
            assertTrue(file.delete(), "Failed to delete existing test file before creating a new one.");
        }

        // Creăm fișierul gol
        try {
            assertTrue(file.createNewFile(), "Failed to create an empty test file.");
        } catch (IOException e) {
            fail("IOException occurred while creating an empty test file: " + e.getMessage());
        }

        // Inițializăm repository-ul și verificăm încărcarea
        JsonFileRepository<DummyEntity> repository = assertDoesNotThrow(() ->
                        new JsonFileRepository<>(testFileName, DummyEntity.class),
                "Repository initialization failed with an empty file."
        );

        // Verificăm că lista este goală după încărcarea fișierului gol
        assertTrue(repository.getEntities().isEmpty(), "The repository should be empty after loading from an empty file.");
    }

    @Test
    void testLoadFile_FileIsCorrupted() {
        try (FileWriter writer = new FileWriter(testFileName)) {
            writer.write("{ invalid_json: true }"); // Scriem date JSON corupte
        } catch (IOException e) {
            fail("Failed to create a corrupted file for testing.");
        }

        assertThrows(RepositoryException.class,
                () -> new JsonFileRepository<>(testFileName, DummyEntity.class),
                "Loading from a corrupted file should throw a RepositoryException.");
    }

    @Test
    void testLoadFile_InvalidDataType() {
        try (FileWriter writer = new FileWriter(testFileName)) {
            writer.write("[{\"id\":\"invalid_id\", \"name\":\"Entity\"}]"); // JSON cu tipuri de date invalide
        } catch (IOException e) {
            fail("Failed to write invalid data type to test file.");
        }

        assertThrows(RepositoryException.class,
                () -> new JsonFileRepository<>(testFileName, DummyEntity.class),
                "Loading from a file with invalid data type should throw a RepositoryException.");
    }

}
