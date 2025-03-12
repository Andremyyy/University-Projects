package util;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class Settings {

    private String repoType;

    private String cakeFileName;
    private String orderFileName;

    public String getAppMode() {
        return appMode;
    }

    public void setAppMode(String appMode) {
        this.appMode = appMode;
    }

    private String appMode;

    private Settings(){

    }

    public String getRepoType() {
        return repoType;
    }

    public String getCakeFileName() {
        return cakeFileName;
    }
    public String getOrderFileName() {
        return orderFileName;
    }

    private static Settings instance;

    public static Settings getInstance() {
        if (instance == null) {
            // Citim fisierul de setari -- asta ruleaza o singura data
            Properties settings = new Properties();
            try {
                settings.load(new FileReader("settings.properties"));
            } catch (IOException e) {
                throw new RuntimeException("Error loading settings.properties" + e.getMessage());
            }

            instance = new Settings();
            instance.repoType = settings.getProperty("repo_type");
            instance.cakeFileName = settings.getProperty("cake_file_name");
            instance.orderFileName = settings.getProperty("order_file_name");
            instance.appMode = settings.getProperty("app_mode");

            // Verificăm setările
            if (instance.repoType == null || instance.repoType.isEmpty()) {
                throw new RuntimeException("Repository type is not set in settings.properties!");
            }
            if (instance.appMode == null || instance.appMode.isEmpty()) {
                throw new RuntimeException("Application mode (app_mode) is not set in settings.properties!");
            }
        }
        return instance;
    }
}
