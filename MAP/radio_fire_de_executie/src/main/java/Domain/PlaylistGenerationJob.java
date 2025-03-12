package Domain;

import Exceptions.RepositoryException;
import Service.RadioService;
import javafx.application.Platform;
import javafx.collections.ObservableList;

import java.util.ArrayList;
import java.util.List;

public class PlaylistGenerationJob implements Runnable {
    private ObservableList<Radio> playlist;
    private RadioService radioService;
    private int startIndex;
    private int endIndex;

    public PlaylistGenerationJob(ObservableList<Radio> playlist, RadioService radioService, int startIndex, int endIndex) {
        this.playlist = playlist;
        this.radioService = radioService;
        this.startIndex = startIndex;
        this.endIndex = endIndex;
    }

    @Override
    public void run() {
        try {
            for (int i = startIndex; i < endIndex; i++) {
                Radio randomSong = getRandomSong(radioService);
                Platform.runLater(() -> playlist.add(randomSong)); // Update UI thread safely
            }
        } catch (RepositoryException e) {
            e.printStackTrace();
        }
    }

    private Radio getRandomSong(RadioService radioService) throws RepositoryException {
        List<Radio> allRadios = new ArrayList<>(radioService.getRadios());
        int randomIndex = (int) (Math.random() * allRadios.size());
        return allRadios.get(randomIndex);
    }
}
