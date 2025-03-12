package Service;

import Domain.Produs;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;

import java.util.ArrayList;

public class ProdusService {
    private final AbstractRepository<Produs> produsRepo;

    public ProdusService(AbstractRepository<Produs> radioRepo) {
        this.produsRepo = radioRepo;
    }

    public void addProdus(int id, String marca, String nume, int pret, int cantitate) throws RepositoryException {

        if (produsRepo.findById(id))
            throw new RepositoryException("Exista deja un Produs cu id-ul = " + id);

        Produs newProdus = new Produs(id, marca, nume, pret, cantitate);

        produsRepo.add(newProdus);
    }

    public ArrayList<Produs> getProduse() throws NullPointerException{
        ArrayList<Produs> produse;
        produse = produsRepo.getEntities();
        if (produse.isEmpty()) {
            throw new NullPointerException( "There are no products yet!");
        }
        return produse;
    }

    public void deleteProdus(int id) throws RepositoryException {
        produsRepo.removeById(id);
    }

    public void updateProdus(int id, String marca, String nume, int pret, int cantitate) throws RepositoryException {

        Produs existingProdus = produsRepo.getEntityById(id);
        if (existingProdus == null) {
            throw new RepositoryException("Produs with id = " + id + " does not exist!");
        }

        Produs updatedProdus = new Produs(id, marca, nume, pret, cantitate);
        produsRepo.update(updatedProdus);
    }

    public Produs getProdusById(int id) {

        return produsRepo.getEntityById(id);
    }
}
