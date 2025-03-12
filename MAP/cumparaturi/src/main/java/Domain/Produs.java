package Domain;

import java.io.Serial;
import java.io.Serializable;

public class Produs implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;


    private int id;
    private String marca;
    private String nume;
    private int pret;
    private int cantitate;

    public Produs(int id, String marca, String nume, int pret, int cantitate) {
        this.id = id;
        this.marca = marca;
        this.nume = nume;
        this.pret = pret;
        this.cantitate = cantitate;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public int getPret() {
        return pret;
    }

    public void setPret(int pret) {
        this.pret = pret;
    }

    public int getCantitate() {
        return cantitate;
    }

    public void setCantitate(int cantitate) {
        this.cantitate = cantitate;
    }

    @Override
    public String toString() {
        return "Produs { " +
                "id = " + id +
                ", marca = ' " + marca + '\'' +
                ", nume = ' " + nume + '\'' +
                ", pret = ' " + pret + '\'' +
                ", cantitate = " + cantitate +
                " }";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Produs produs = (Produs) o;
        return id == produs.id;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(id);
    }
}
