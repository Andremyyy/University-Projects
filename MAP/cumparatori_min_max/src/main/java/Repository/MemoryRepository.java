package Repository;

import Domain.Produs;
import Exceptions.RepositoryException;

import java.util.ArrayList;

public class MemoryRepository<T extends Produs> extends AbstractRepository<T> {

    public boolean findById(int id) {
        for (T entity : entities) {
            if (entity.getId() == id) {
                return true;
            }
        }
        return false;
    }


    public void add(T elem) throws RepositoryException {
        if (findById(elem.getId())) {
            throw new RepositoryException("There is already an entity with this id = " + elem.getId());
        }
        entities.add(elem);
    }

    public void removeById(int id) throws RepositoryException{
        if (!findById(id)) {
            throw new RepositoryException("There is no entity with this id = " + id + " !");
        }
        entities.remove(getEntityById(id));
    }


    public T getEntityById(int id) {
        for (T e : entities)
            if (e.getId() == id)
                return e;
        return null;
    }

    public void update(T elem) throws RepositoryException {
        T existingEntity = getEntityById(elem.getId());
        if (existingEntity == null) {
            throw new RepositoryException("There is no entity with this id = " + elem.getId() + "!");
        }
        int index = entities.indexOf(existingEntity);
        entities.set(index, elem);
    }

    public ArrayList<T> getEntities() {
        return entities;
    }
}