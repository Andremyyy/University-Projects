package Domain;//Comandă (ID : int, torturi : List<Tort>, data : Date)

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serial;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;

public class Order extends Entity implements Serializable {
    // Adaugă un serialVersionUID pentru a evita erorile de compatibilitate între versiunile clasei
    @Serial
    private static final long serialVersionUID = 1L;
    private ArrayList<Cake> cakes;
    private Date date;

    // Constructor cu parametri pentru Order
    @JsonCreator
    public Order(@JsonProperty("id") int id, @JsonProperty("cakes") ArrayList<Cake> cakes, @JsonProperty("date") Date date) {
        super(id);
        this.cakes = cakes;
        this.date = date;
    }

    public ArrayList<Cake> getCakes() {
        return cakes;
    }
    public void setCakes(ArrayList<Cake> cakes) {
        this.cakes = cakes;
    }
    public Date getDate() {
        return date;
    }
    public void setDate(Date date) {
        this.date = date;
    }

    @Override
    public String toString() {
        StringBuilder orderDetails = new StringBuilder("Order ID: " + id + ", Date: " + date + ", Cakes: ");

        // Iterăm prin lista de torturi și construim stringul cu formatul id-nume
        for (int i = 0; i < cakes.size(); i++) {
            Cake cake = cakes.get(i);
            orderDetails.append(cake.getId()).append("-").append(cake.getTypeOfCake());

            // Adăugăm separatorul ";" între torturi, dar nu după ultimul element
            if (i < cakes.size() - 1) {
                orderDetails.append(", ");
            }
        }

        return orderDetails.toString();
    }

}
