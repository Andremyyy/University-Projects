import Domain.Cake;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertNull;

public class CakeTest {
    @Test
    public void testCakeCreation() {
        Cake cake = new Cake(1, "Chocolate");


        Assertions.assertEquals(1, cake.getId(), "The cake ID should be 1");

        Assertions.assertEquals("Chocolate", cake.getTypeOfCake(), "The cake type should be 'Chocolate'");
    }

    @Test
    void testConstructorWithParameters() {
        // Creăm un obiect Cake folosind constructorul cu parametri
        int id = 1;
        String typeOfCake = "Chocolate";

        Cake cake = new Cake(id, typeOfCake);

        // Verificăm dacă valorile au fost corect setate
        Assertions.assertEquals(id, cake.getId(), "The cake ID should be correctly set.");
        Assertions.assertEquals(typeOfCake, cake.getTypeOfCake(), "The cake type should be correctly set.");
    }

    @Test
    void testDefaultConstructor() {
        // Creăm un obiect Cake folosind constructorul implicit
        Cake cake = new Cake();

        // Verificăm dacă id-ul și tipul tortului sunt setate corect la valorile implicite
        Assertions.assertEquals(0, cake.getId(), "The default cake ID should be 0.");
        assertNull(cake.getTypeOfCake(), "The default cake type should be null.");
    }

    @Test
    public void testSetCakeType() {
        Cake cake = new Cake(2, "Vanilla");


        cake.setTypeOfCake("Strawberry");


        Assertions.assertEquals("Strawberry", cake.getTypeOfCake(), "The cake type should be updated to 'Strawberry'");
    }

    @Test
    public void testToString() {
        Cake cake = new Cake(3, "Mango");


        String expectedString = "Cake 3 {type = Mango}";
        Assertions.assertEquals(expectedString, cake.toString(), "The toString method should return the correct string representation");
    }
}
