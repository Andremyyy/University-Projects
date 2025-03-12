import Domain.IDGenerator;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

public class IdGeneratorTest {
    private static final String testFileName = "test_last_id.txt";
    private IDGenerator idGenerator;

    @BeforeEach
    void setUp() throws IOException {
        // Sterge fisierul de text daca exista
        Files.deleteIfExists(Path.of(testFileName));
        idGenerator = new IDGenerator(testFileName);
    }

    @AfterEach
    void tearDown() throws IOException {
        // Șterge fișierul de test după fiecare test
        Files.deleteIfExists(Path.of(testFileName));
    }

    @Test
    void testGenerateId_FileDoesNotExist() {
        int id = idGenerator.generateId();
        assertEquals(100, id, "ID-ul generat ar trebui să fie 100 când fișierul de test nu există.");
    }

    @Test
    void testGenerateId_FileExistsWithValidId() throws IOException {
        try (FileWriter writer = new FileWriter(testFileName)) {
            writer.write("200");
        }

        idGenerator = new IDGenerator(testFileName);
        int id = idGenerator.generateId();
        assertEquals(201, id, "ID-ul generat ar trebui să fie 201 când fișierul conține ID-ul 200.");
    }

    @Test
    void testGenerateId_FileExistsWithInvalidId() throws IOException {
        try (FileWriter writer = new FileWriter(testFileName)) {
            writer.write("invalid_number");
        }

        idGenerator = new IDGenerator(testFileName);
        int id = idGenerator.generateId();
        assertEquals(100, id, "ID-ul generat ar trebui să fie 100 când fișierul de test conține un număr nevalid.");
    }

    @Test
    void testGenerateId_FileExistsWithEmptyContent() throws IOException {
        try (FileWriter writer = new FileWriter(testFileName)) {
            writer.write("");
        }

        idGenerator = new IDGenerator(testFileName);
        int id = idGenerator.generateId();
        assertEquals(100, id, "ID-ul generat ar trebui să fie 100 când fișierul de test este gol.");
    }

    @Test
    void testGenerateId_PersistenceCheck() {
        int id1 = idGenerator.generateId();
        assertEquals(100, id1, "ID-ul generat ar trebui să fie 100.");

        IDGenerator newGenerator = new IDGenerator(testFileName);
        int id2 = newGenerator.generateId();
        assertEquals(101, id2, "ID-ul generat ar trebui să fie 101 la următorul apel.");
    }

    @Test
    void testLoadLastId_FileReadingError() {
        File file = new File(testFileName);
        try {
            file.createNewFile();
            file.setReadable(false);
        } catch (IOException e) {
            fail("Nu s-a putut crea fișierul de test.");
        }

        idGenerator = new IDGenerator(testFileName);
        int id = idGenerator.generateId();
        assertEquals(100, id, "ID-ul generat ar trebui să fie 100 în caz de eroare la citirea fișierului.");

        file.setReadable(true); // Resetăm permisiunile pentru a putea șterge fișierul
    }
}
