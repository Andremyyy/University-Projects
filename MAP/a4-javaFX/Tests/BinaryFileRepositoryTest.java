

import Domain.Entity;
import Exceptions.RepositoryException;
import Repository.BinaryFileRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

public class BinaryFileRepositoryTest {

    static class DummyEntity extends Entity {
        private final String name;

        public DummyEntity(int id, String name) {
            super(id);
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    private static final String testFileName = "test_data.bin";
    private BinaryFileRepository<DummyEntity> repository;

    @BeforeEach
    void setUp() {
        try {
            repository = new BinaryFileRepository<>(testFileName);
        } catch (RepositoryException e) {
            fail("Initialization failed: " + e.getMessage());
        }
    }

    @AfterEach
    void tearDown() {
        // Forțăm colectarea gunoiului pentru a elibera resursele de fișier
        System.gc();
        File file = new File(testFileName);
        if (file.exists()) {
            file.setWritable(true); // Asigură permisiunea de scriere înainte de ștergere
            assertTrue(file.delete(), "Failed to delete test file.");
        }
    }

    @Test
    void testInitialization_FileDoesNotExist() {
        File file = new File(testFileName);
        assertFalse(file.exists(), "The file should not exist before initialization.");

        try {
            BinaryFileRepository<Entity> repository = new BinaryFileRepository<>(testFileName);
            assertNotNull(repository, "The repository should be initialized.");
        } catch (RepositoryException e) {
            fail("Should not throw exception when initializing without an existing file.");
        }

        // În loc să verificăm dacă fișierul există, putem verifica lista de entități
        try {
            BinaryFileRepository<Entity> repository = new BinaryFileRepository<>(testFileName);
            assertEquals(0, repository.getEntities().size(), "The list of entities should be initialized as empty.");
        } catch (RepositoryException e) {
            fail("Error during reinitialization check.");
        }
    }

    @Test
    void testSaveAndLoadData_Success() {
        try {
            DummyEntity entity1 = new DummyEntity(1, "Entity1");
            DummyEntity entity2 = new DummyEntity(2, "Entity2");

            repository.add(entity1);
            repository.add(entity2);
            repository.saveFile();

            BinaryFileRepository<DummyEntity> newRepository = new BinaryFileRepository<>(testFileName);
            assertEquals(2, newRepository.getEntities().size(),
                    "Repository should contain 2 entities after loading.");
        } catch (RepositoryException e) {
            fail("Exception during save and load test: " + e.getMessage());
        }
    }

    @Test
    void testLoadFile_FileNotFound() {
        File file = new File(testFileName);
        if (file.exists()) {
            assertFalse(file.delete(), "Failed to delete test file before the test.");
        }

        assertDoesNotThrow(() -> new BinaryFileRepository<>(testFileName),
                "Initializing with a non-existent file should not throw an exception.");
    }

    @Test
    void testLoadFile_FileIsEmpty() {
        try {
            File file = new File(testFileName);
            if (file.exists()) {
                assertTrue(file.delete(), "Failed to delete existing test file.");
            }

            boolean created = file.createNewFile();
            assertTrue(created, "Failed to create an empty test file.");
            assertTrue(file.exists() && file.canWrite(), "The file should be writable.");

            BinaryFileRepository<DummyEntity> newRepository = new BinaryFileRepository<>(testFileName);
            assertEquals(0, newRepository.getEntities().size(),
                    "Repository should be empty for an empty file.");
        } catch (IOException | RepositoryException e) {
            fail("Exception during empty file test: " + e.getMessage());
        }
    }

    @Test
    void testLoadFile_FileIsCorrupted() {
        try (FileOutputStream fos = new FileOutputStream(testFileName)) {
            fos.write(new byte[]{0, 1, 2, 3}); // Scriem date corupte
        } catch (IOException e) {
            fail("Failed to create a corrupted file for testing.");
        }

        assertThrows(RepositoryException.class,
                () -> new BinaryFileRepository<>(testFileName),
                "Loading from a corrupted file should throw a RepositoryException.");
    }

    @Test
    void testLoadFile_InvalidDataType() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(testFileName))) {
            oos.writeObject("invalid_data_type"); // Scriem un string în loc de ArrayList
        } catch (IOException e) {
            fail("Failed to write invalid data type to test file.");
        }

        assertThrows(RepositoryException.class,
                () -> new BinaryFileRepository<>(testFileName),
                "Loading from a file with invalid data type should throw a RepositoryException.");
    }

//    @Test
//    void testSaveFile_ErrorWriting() {
//        File file = new File(testFileName);
//        try {
//            if (file.exists()) {
//                assertTrue(file.delete(), "Failed to delete existing test file.");
//            }
//            boolean created = file.createNewFile();
//            assertTrue(created, "Failed to create test file.");
//
//            assertTrue(file.setWritable(false), "Failed to make the file read-only.");
//
//            DummyEntity entity = new DummyEntity(1, "TestEntity");
//            repository.add(entity);
//
//            assertThrows(RepositoryException.class,
//                    () -> repository.saveFile(),
//                    "Saving to a read-only file should throw a RepositoryException.");
//        } catch (IOException | RepositoryException e) {
//            fail("IOException occurred during save file error test: " + e.getMessage());
//        } finally {
//            file.setWritable(true); // Resetăm permisiunea de scriere
//        }
//    }
}
