package Repository;

import Domain.Entity;
import Domain.EntityConvertor;
import Exceptions.RepositoryException;

import java.io.*;

public class TextFileRepository<T extends Entity> extends AbstractFileRepository<T> {

    protected EntityConvertor<T> converter;
    private String fileName;

    public TextFileRepository(String fileName, EntityConvertor<T> converter) {
        super(fileName);
        this.converter = converter;
        this.fileName = fileName;
        try {
            loadFile();
        } catch (RepositoryException e) {
            throw new RuntimeException(e);
        }
    }
    @Override
    public void saveFile() throws RepositoryException {

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(this.fileName))) {
            for (var entity : this.entities) {
                String asString = converter.toString(entity);
                bw.write(asString);
                bw.newLine();
            }
        } catch (IOException e) {
            throw new RepositoryException("Error while saving the file:", e);
        }
    }

    @Override
    protected void loadFile() throws RepositoryException {
        File file = new File(this.fileName);
        if (file.length() == 0) {
            // Dacă fișierul este gol, nu mai încerc să-l citesc, doar îl ignor
//            System.out.println("File is empty, adding default entities.");
            return;
        }
        try (BufferedReader br = new BufferedReader(new FileReader(this.fileName))) {
            String line = br.readLine();
            while (line != null) {
                try {
                    entities.add(converter.fromString(line)); // încearcă să convertești fiecare linie
                } catch (RuntimeException e) {
                    System.out.println("Skipping invalid line: " + line); // Linia invalidă va fi sărită
                }
                line = br.readLine();
            }
        } catch (IOException e) {
            throw new RepositoryException("Error while loading the file:", e);
        }
    }
}
