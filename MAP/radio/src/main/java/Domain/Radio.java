package Domain;

import java.time.LocalTime;

public class Radio {
    private int id;
    private String formatie;
    private String titlu;
    private String genMuzical;
    private String durata; // Format doar mm:ss

    public Radio(int id, String formatie, String titlu, String genMuzical, String durata) {
        this.id = id;
        this.formatie = formatie;
        this.titlu = titlu;
        this.genMuzical = genMuzical;
        this.durata = durata;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFormatie() {
        return formatie;
    }

    public void setFormatie(String formatie) {
        this.formatie = formatie;
    }

    public String getTitlu() {
        return titlu;
    }

    public void setTitlu(String titlu) {
        this.titlu = titlu;
    }

    public String getGenMuzical() {
        return genMuzical;
    }

    public void setGenMuzical(String genMuzical) {
        this.genMuzical = genMuzical;
    }

    public String getDurata() {
        return durata;
    }

    public void setDurata(String durata) {
        this.durata =  durata;
    }

    @Override
    public String toString() {
        return "Radio { " +
                "id = " + id +
                ", formatie = ' " + formatie + '\'' +
                ", titlu = ' " + titlu + '\'' +
                ", genMuzical = ' " + genMuzical + '\'' +
                ", durata = " + getDurata() +
                " }";
    }
}
