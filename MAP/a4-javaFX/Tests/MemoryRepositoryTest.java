import Domain.Cake;
import Exceptions.DuplicateIDException;
import Exceptions.ObjectNotFoundException;
import Exceptions.RepositoryException;
import Repository.MemoryRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class MemoryRepositoryTest {

    private MemoryRepository<Cake> cakeRepository;

    @BeforeEach
    public void setUp() {
        cakeRepository = new MemoryRepository<>();
    }


    @Test
    public void testAddEntity() throws RepositoryException {
        Cake cake = new Cake(1, "Chocolate Cake");

        cakeRepository.add(cake);


        assertTrue(cakeRepository.findById(1));
    }


    @Test
    public void testAddEntityDuplicateID() throws RepositoryException {
        Cake cake1 = new Cake(1, "Chocolate Cake");
        Cake cake2 = new Cake(1, "Vanilla Cake");

        cakeRepository.add(cake1);


        DuplicateIDException exception = assertThrows(DuplicateIDException.class, () -> {
            cakeRepository.add(cake2);
        });

        assertEquals("There is already an entity with this id = 1", exception.getMessage());
    }


    @Test
    public void testFindById() throws RepositoryException {
        Cake cake = new Cake(1, "Chocolate Cake");
        cakeRepository.add(cake);

        Cake foundCake = cakeRepository.getEntityById(1);

        assertNotNull(foundCake);
        assertEquals("Chocolate Cake", foundCake.getTypeOfCake());
    }


    @Test
    public void testFindByIdNotFound() {
        Cake foundCake = cakeRepository.getEntityById(999);

        assertNull(foundCake);
    }


    @Test
    public void testRemoveById() throws RepositoryException {
        Cake cake = new Cake(1, "Chocolate Cake");
        cakeRepository.add(cake);


        cakeRepository.removeById(1);


        assertFalse(cakeRepository.findById(1));
    }


    @Test
    public void testRemoveByIdNotFound() {
        ObjectNotFoundException exception = assertThrows(ObjectNotFoundException.class, () -> {
            cakeRepository.removeById(999);
        });

        assertEquals("There is no entity with this id = 999 !", exception.getMessage());
    }


    @Test
    public void testUpdateEntity() throws RepositoryException {
        Cake cake = new Cake(1, "Chocolate Cake");
        cakeRepository.add(cake);

        Cake updatedCake = new Cake(1, "Updated Chocolate Cake");
        cakeRepository.update(updatedCake);

        Cake foundCake = cakeRepository.getEntityById(1);
        assertEquals("Updated Chocolate Cake", foundCake.getTypeOfCake());
    }


    @Test
    public void testUpdateEntityNotFound() {
        Cake updatedCake = new Cake(999, "Non-Existent Cake");

        ObjectNotFoundException exception = assertThrows(ObjectNotFoundException.class, () -> {
            cakeRepository.update(updatedCake);
        });

        assertEquals("There is no entity with this id = 999!", exception.getMessage());
    }
}
