package Repository;

import Domain.Entity;
import Exceptions.RepositoryException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.type.CollectionType;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class JsonFileRepository <T extends Entity> extends AbstractFileRepository<T> {

    private final Class<T> entityType;
    private final ObjectMapper objectMapper;

//    public JsonFileRepository(String fileName, Class<T> entityType) throws RepositoryException {
//        super(fileName);
//        this.entityType = entityType;
//        this.objectMapper = new ObjectMapper();
//        loadFile();
//    }
    public JsonFileRepository(String fileName, Class<T> entityType) throws RepositoryException {
        super(fileName);
        this.entityType = entityType;
        this.objectMapper = new ObjectMapper();

        // Creăm fișierul dacă nu există
        File file = new File(fileName);
        try {
            if (!file.exists()) {
                file.createNewFile(); // Creează fișierul gol
            }
        } catch (IOException e) {
            throw new RepositoryException("Error creating JSON file: " + e.getMessage());
        }

        loadFile();
    }

    @Override
    public void saveFile() throws RepositoryException {
        try {
            objectMapper.writeValue(new File(fileName), this.entities);
        } catch (IOException e) {
            throw new RepositoryException("Error saving JSON file: " + e.getMessage());
        }
    }

//    @Override
//    protected void loadFile() throws RepositoryException {
//        try {
//            File file = new File(fileName);
//            if (file.exists()) {
//                CollectionType listType = objectMapper.getTypeFactory().constructCollectionType(ArrayList.class, entityType);
//                this.entities = objectMapper.readValue(file, listType);
//            } else {
//                this.entities = new ArrayList<>();
//            }
//        } catch (IOException e) {
//            throw new RepositoryException("Error loading JSON file: " + e.getMessage());
//        }
//    }
    @Override
    protected void loadFile() throws RepositoryException {
        try {
            File file = new File(fileName);
            if (file.exists()) {
                // Verificăm dacă fișierul este gol
                if (file.length() == 0) {
                    this.entities = new ArrayList<>();
                } else {
                    CollectionType listType = objectMapper.getTypeFactory().constructCollectionType(ArrayList.class, entityType);
                    this.entities = objectMapper.readValue(file, listType);
                }
            } else {
                this.entities = new ArrayList<>();
            }
        } catch (IOException e) {
            throw new RepositoryException("Error loading JSON file: " + e.getMessage());
        }
    }
}
