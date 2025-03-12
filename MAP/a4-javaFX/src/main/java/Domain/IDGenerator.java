package Domain;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class IDGenerator {

    //fisierul unde regasim ultimul id folosit
    private static String fileName;
    // id-ul de inceput
    private static final int startingId = 100;
    private int currentId;

    // incarca ultimul ID din fisier SAU folosește id-ul de inceput dacă nu există fișierul/fisierul este gol
    public IDGenerator( String fileName) {
        IDGenerator.fileName = fileName;
        this.currentId = loadLastId();
    }

    // metoda care genereaza un nou ID
    public int generateId() {
        currentId++;
        saveCurrentId();
        return currentId;
    }

    // metoda care salveaza ultimul ID generat în fisier
    private void saveCurrentId() {
        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write(String.valueOf(currentId));
        } catch (IOException ignored) {
        }
    }

    // metoda care încărca ultimul ID din fișier
    private int loadLastId() {
        try {
            // citesc conținutul fișierului (dacă acesta există)
            Path path = Paths.get(fileName);
            //verific daca exista fisierul
            if (Files.exists(path)) {
                //citesc tot continutul fisierului intr-un string
                String content = new String(Files.readAllBytes(path));
                // conversie la int
                //content.trim() pentru a elima spatiile "albe" de la inceput sau de la sfarsit
                return Integer.parseInt(content.trim());
            }
            //prind orice exceptie (probleme cu fisierul si/sau numar nevalid)
        } catch (IOException | NumberFormatException e) {
            System.out.println("Error reading ID from file. Starting with default ID.");
        }
        // valoarea va fi incrementată la primul apel (in metoda generateId)
        // deci incep cu -1 (daca am avut probleme cu fisierul si/sau numar nevalid)
        return startingId - 1;
    }


}

