package Service;

import Domain.Radio;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;

import java.util.ArrayList;

public class RadioService {
    private final AbstractRepository<Radio> radioRepo;

    public RadioService(AbstractRepository<Radio> radioRepo) {
        this.radioRepo = radioRepo;
    }

    public void addRadio(int id, String formatie, String titlu, String gen_muzical, String durata) throws RepositoryException {

        if (radioRepo.findById(id))
            throw new RepositoryException("Exista deja un Radio cu id-ul = " + id);

        Radio newRadio = new Radio(id, formatie, titlu, gen_muzical, durata);

        radioRepo.add(newRadio);
    }

    public ArrayList<Radio> getRadios() throws NullPointerException{
        ArrayList<Radio> radios;
        radios = radioRepo.getEntities();
        if (radios.isEmpty()) {
            throw new NullPointerException( "There are no radios yet!");
        }
        return radios;
    }

    public void deleteRadio(int id) throws RepositoryException {
        radioRepo.removeById(id);
    }

    public void updateRadio(int id, String formatie, String titlu, String gen_muzical, String durata) throws RepositoryException {

        Radio existingRadio = radioRepo.getEntityById(id);
        if (existingRadio == null) {
            throw new RepositoryException("Radio with id = " + id + " does not exist!");
        }

        Radio updatedRadio = new Radio(id, formatie, titlu, gen_muzical, durata);
        radioRepo.update(updatedRadio);
    }

    public Radio getRadioById(int id) {

        return radioRepo.getEntityById(id);
    }
}
