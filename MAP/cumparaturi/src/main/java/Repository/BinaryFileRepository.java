package Repository;

import Domain.Produs;
import Exceptions.RepositoryException;

import java.io.*;
import java.util.ArrayList;

public class BinaryFileRepository<T extends Produs> extends AbstractFileRepository<T> {

    public BinaryFileRepository(String filename) throws RepositoryException {
        super(filename);
        loadFile();
    }
    @Override
    public void saveFile() throws RepositoryException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(entities);
        } catch (IOException e) {
            throw new RepositoryException("Error saving data to file: " + e.getMessage(), e);
        }
    }

    @Override
    public void loadFile() throws RepositoryException {
        File file = new File(fileName);

        // Verifică dacă fișierul există
        if (!file.exists()) {
            System.out.println("File not found. It will be initialized.");
            this.entities = new ArrayList<>();
            return; // Nu mai continuăm citirea fișierului dacă nu există
        }

        // Verificare permisiuni
        if (!file.canRead()) {
            throw new RepositoryException("File exists but cannot be read: " + fileName);
        }

        // Dacă fișierul există, încearc să-l citesc
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            Object obj = ois.readObject();
            // Verificare suplimentară pentru tipul obiectului citit
            if (obj instanceof ArrayList<?>) {
                try {
                    this.entities = (ArrayList<T>) obj;
                } catch (ClassCastException e) {
                    throw new RepositoryException("Failed to cast data from file to the expected type: " + e.getMessage(), e);
                }
            } else {
                throw new RepositoryException("Data from file is not of the expected type (ArrayList).");
            }
        } catch (EOFException e) {
            // Fișierul este gol, inițializează lista de entități
            System.out.println("Empty file detected. Initializing empty entity list.");
            this.entities = new ArrayList<>();
        } catch (IOException | ClassNotFoundException e) {
            throw new RepositoryException("Error while loading the file: " + e.getMessage(), e);
        }


    }
}
