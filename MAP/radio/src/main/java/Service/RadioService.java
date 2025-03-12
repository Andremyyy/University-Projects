package Service;

import Domain.Radio;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;
import Repository.SQLRadioRepository;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class RadioService {
    private final AbstractRepository<Radio> radioRepo;

    public RadioService(AbstractRepository<Radio> radioRepo) {
        this.radioRepo = radioRepo;
    }

    public void addRadio(int id, String formatie, String titlu, String gen_muzical, String durata) throws RepositoryException {

        if (radioRepo.findById(id))
            throw new RepositoryException("Exista deja un Radio cu id-ul = " + id);

        Radio newRadio = new Radio(id, formatie, titlu, gen_muzical, durata);

        radioRepo.add(newRadio);
    }

    public ArrayList<Radio> getRadios() throws NullPointerException{
        ArrayList<Radio> radios;
        radios = radioRepo.getEntities();
        if (radios.isEmpty()) {
            throw new NullPointerException( "There are no radios yet!");
        }
        return radios;
    }

    public void deleteRadio(int id) throws RepositoryException {
        radioRepo.removeById(id);
    }

    public void updateRadio(int id, String formatie, String titlu, String gen_muzical, String durata) throws RepositoryException {

        Radio existingRadio = radioRepo.getEntityById(id);
        if (existingRadio == null) {
            throw new RepositoryException("Radio with id = " + id + " does not exist!");
        }

        Radio updatedRadio = new Radio(id, formatie, titlu, gen_muzical, durata);
        radioRepo.update(updatedRadio);
    }

    public Radio getRadioById(int id) {

        return radioRepo.getEntityById(id);
    }

    public List<Radio> getSortedItems() {
        // Preluăm toate radiourile
        List<Radio> radios = new ArrayList<>(getRadios());

        // Sortăm lista
        radios.sort((radio1, radio2) -> {
            int result = radio1.getFormatie().compareToIgnoreCase(radio2.getFormatie());
            if (result == 0) {
                result = radio1.getTitlu().compareToIgnoreCase(radio2.getTitlu());
            }
            return result;
        });

        return radios;
    }

    public List<Radio> getFilteredRadios(String filterText) throws RepositoryException {
        return getRadios().stream()
                .filter(radio -> radio.getFormatie().toLowerCase().contains(filterText.toLowerCase()) ||
                        radio.getTitlu().toLowerCase().contains(filterText.toLowerCase()) ||
                        radio.getGenMuzical().toLowerCase().contains(filterText.toLowerCase()) ||
                        radio.getDurata().toLowerCase().contains(filterText.toLowerCase()))
                .collect(Collectors.toList());
    }

    public List<Radio> generatePlaylist(String playlistName) throws ParseException, RepositoryException {
        List<Radio> allRadios = new ArrayList<>(getRadios());
        List<Radio> playlist = new ArrayList<>();

        int totalDuration = 0;
        String lastFormatie = "";
        String lastGen = "";
        Random random = new Random();

        while (true) {
            // Eliminăm piesele care nu respectă condițiile
            List<Radio> validRadios = new ArrayList<>();
            for (Radio radio : allRadios) {
                if ((!radio.getFormatie().equals(lastFormatie)) &&
                        (!radio.getGenMuzical().equals(lastGen))) {
                    validRadios.add(radio);
                }
            }

            // Dacă nu mai sunt piese valide, oprim generarea
            if (validRadios.isEmpty()) {
                if (playlist.isEmpty()) {
                    throw new RepositoryException("Nu există suficiente piese pentru a genera un playlist valid!");
                }
                break;
            }

            // Selectăm o piesă aleatorie dintre piesele valide
            Radio selectedRadio = validRadios.get(random.nextInt(validRadios.size()));

            // Calculăm durata piesei în secunde
            int songDurationInSeconds = convertDurationToSeconds(selectedRadio.getDurata());

            // Actualizăm playlist-ul și informațiile relevante
            playlist.add(selectedRadio);
            totalDuration += songDurationInSeconds;
            lastFormatie = selectedRadio.getFormatie();
            lastGen = selectedRadio.getGenMuzical();

            // Verificăm dacă adăugarea piesei depășește limita de 15 minute
            if (totalDuration  > 15 * 60) {
                break;
            }


        }

        if (playlist.isEmpty()) {
            throw new RepositoryException("Nu s-a putut genera un playlist valid!");
        }

        // Salvăm playlist-ul în baza de date (opțional)
        //savePlaylist(playlistName, playlist);

        return playlist;
    }

    private int convertDurationToSeconds(String durata) throws ParseException {
        // Transforma durata din formatul "mm:ss" în secunde
        String[] timeParts = durata.split(":");
        int minutes = Integer.parseInt(timeParts[0]);
        int seconds = Integer.parseInt(timeParts[1]);
        return minutes * 60 + seconds;
    }

    private void savePlaylist(String playlistName, List<Radio> playlist) throws RepositoryException {
        // Instanțiem repository-ul SQL
        SQLRadioRepository sqlRepo = new SQLRadioRepository();

        // Creăm playlistul în baza de date
        sqlRepo.createPlaylist(playlistName);  // Folosim metoda createPlaylist pentru a-l salva în DB

        // Obținem ID-ul playlistului proaspăt creat
        int playlistId = sqlRepo.getPlaylistIdByName(playlistName);

        // Adăugăm piesele la playlist în baza de date
        for (Radio radio : playlist) {
            // Adăugăm fiecare piesă la playlistul respectiv
            sqlRepo.addSongToPlaylist(playlistId, radio.getId(), radio.getDurata());
        }

        // Mesaj de confirmare
        System.out.println("Playlistul \"" + playlistName + "\" a fost generat și conține " + playlist.size() + " piese.");
    }


    public void createPlaylist(String playlistName) throws RepositoryException, ParseException {
        // Folosim repository-ul SQL pentru a salva playlistul în baza de date
        SQLRadioRepository sqlRepo = new SQLRadioRepository(); // instanțiem repository-ul SQL

        // Generează playlistul
        List<Radio> playlist = generatePlaylist(playlistName);

        // Adăugăm playlistul în baza de date
        sqlRepo.createPlaylist(playlistName);  // folosim metoda createPlaylist pentru a-l salva în DB

        // Mesaj de confirmare
        System.out.println("Playlistul \"" + playlistName + "\" a fost creat cu succes!");
    }

}
