import Domain.Cake;
import Domain.CakeConverter;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class CakeConvertorTest {

    private final CakeConverter cakeConverter = new CakeConverter(Cake.class);

    @Test
    void testToString_ValidCake() {
        Cake cake = new Cake(1, "Chocolate");
        String result = cakeConverter.toString(cake);
        assertEquals("1;Chocolate", result, "The toString method did not return the expected format.");
    }

    @Test
    void testFromString_ValidString() {
        String input = "2;Vanilla";
        Cake cake = cakeConverter.fromString(input);

        assertNotNull(cake, "The returned Cake object should not be null.");
        assertEquals(2, cake.getId(), "The ID of the cake does not match the expected value.");
        assertEquals("Vanilla", cake.getTypeOfCake(), "The type of cake does not match the expected value.");
    }

    @Test
    void testFromString_ExtraSpaces() {
        String input = "  3  ;  Strawberry  ";
        Cake cake = cakeConverter.fromString(input);

        assertNotNull(cake, "The returned Cake object should not be null.");
        assertEquals(3, cake.getId(), "The ID of the cake does not match the expected value.");
        assertEquals("Strawberry", cake.getTypeOfCake(), "The type of cake does not match the expected value.");
    }

    @Test
    void testFromString_InvalidFormat_MissingId() {
        String input = ";Chocolate";

        Exception exception = assertThrows(RuntimeException.class, () -> cakeConverter.fromString(input));
        assertTrue(exception.getMessage().contains("Invalid input format for Cake"), "Expected exception message about invalid input format.");
    }

    @Test
    void testFromString_InvalidFormat_MissingType() {
        String input = "4;";

        Exception exception = assertThrows(RuntimeException.class, () -> cakeConverter.fromString(input));
        assertTrue(exception.getMessage().contains("Invalid input format for Cake"), "Expected exception message about invalid input format.");
    }

    @Test
    void testFromString_InvalidFormat_EmptyString() {
        String input = "";

        Exception exception = assertThrows(RuntimeException.class, () -> cakeConverter.fromString(input));
        assertTrue(exception.getMessage().contains("Invalid input format for Cake"), "Expected exception message about invalid input format.");
    }

    @Test
    void testFromString_InvalidFormat_NonNumericId() {
        String input = "abc;Chocolate";

        Exception exception = assertThrows(RuntimeException.class, () -> cakeConverter.fromString(input));
        assertTrue(exception.getMessage().contains("Invalid input format for Cake"), "Expected exception message about invalid input format.");
    }


    @Test
    void testFromString_TooManyTokens() {
        String input = "5;Cheesecake;Extra";

        Exception exception = assertThrows(RuntimeException.class, () -> cakeConverter.fromString(input));
        assertTrue(exception.getMessage().contains("Invalid input format for Cake"), "Expected exception message about invalid input format.");
    }
}
