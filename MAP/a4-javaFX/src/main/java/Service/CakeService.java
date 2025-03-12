package Service;

import Domain.Cake;
import Domain.IDGenerator;
import Exceptions.ObjectNotFoundException;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;

import java.util.ArrayList;

public class CakeService {
    private final AbstractRepository<Cake> cakeRepo;
    private final IDGenerator idGenerator;

    public CakeService(AbstractRepository<Cake> cakeRepo, IDGenerator idGenerator) {
        this.cakeRepo = cakeRepo;
        this.idGenerator = idGenerator;
    }

    public void addCake(String typeOfCake) throws RepositoryException {
        //incerc sa adaug in Repository tortul cu tipul din parametru
        // si folosesc clasa IDGenerator pt id
        int nextID = idGenerator.generateId();
        Cake newCake = new Cake(nextID, typeOfCake);

        cakeRepo.add(newCake);
    }

    public ArrayList<Cake> getCakes() throws NullPointerException{
        ArrayList<Cake> cakes;
        cakes = cakeRepo.getEntities();
        if (cakes.isEmpty()) {
            throw new NullPointerException( "There are no cakes yet!");
        }
        return cakes;
    }

    public void deleteCake(int id) throws RepositoryException {
        cakeRepo.removeById(id);
    }

    public void updateCake(int id, String typeOfCake) throws RepositoryException {

        Cake existingCake = cakeRepo.getEntityById(id);
        if (existingCake == null) {
            throw new ObjectNotFoundException("Cake with id = " + id + " does not exist!");
        }

        Cake updatedCake = new Cake(id, typeOfCake);
        cakeRepo.update(updatedCake);
    }

    public Cake getCakeById(int id) {

        return cakeRepo.getEntityById(id);
    }
}

