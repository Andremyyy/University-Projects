import Domain.Cake;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;


public class EntityTest {
    @Test
    public void testEntityId() {
        Cake cake = new Cake(1, "Chocolate");

        // Verificăm că ID-ul este corect
        Assertions.assertEquals(1, cake.getId(), "The ID should be 1");
    }
}
