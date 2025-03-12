package Domain;

//Tort (ID : int, tipul tortului : String)
//"Cake" is an "Entity"

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serial;
import java.io.Serializable;
import java.util.Objects;

public class Cake extends Entity implements Serializable {
    // Adaugă un serialVersionUID pentru a evita erorile de compatibilitate între versiunile clasei
    @Serial
    private static final long serialVersionUID = 1L;
    private String typeOfCake;

    /// Constructor implicit pentru Cake (necesar pentru deserializare)
    public Cake() {
        super(); // Apelăm constructorul clasei de bază Entity
    }

    // Constructor cu parametri
    @JsonCreator
    public Cake(@JsonProperty("id") int id, @JsonProperty("typeOfCake") String typeOfCake) {
        super(id);
        this.typeOfCake = typeOfCake;
    }

    public String getTypeOfCake(){
        return typeOfCake;
    }
    public void setTypeOfCake(String typeOfCake){
        this.typeOfCake = typeOfCake;
    }

    public String toString(){
        return "Cake " + id + " {type = " + typeOfCake + "}";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Cake cake = (Cake) obj;
        return id == cake.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

}
