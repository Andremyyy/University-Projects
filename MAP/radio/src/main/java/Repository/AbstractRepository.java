package Repository;

import Domain.Radio;
import Exceptions.RepositoryException;

import java.util.ArrayList;
import java.util.Iterator;

public abstract class AbstractRepository<T extends Radio> implements Iterable<T> {
    protected ArrayList<T> entities = new ArrayList<>();

    public abstract void add(T elem) throws RepositoryException;

    public abstract void removeById(int id) throws RepositoryException;

    public abstract T getEntityById(int id);

    public abstract boolean findById(int id) throws RepositoryException;

    public int size() {
        return this.entities.size();
    }

    public abstract void update (T elem) throws RepositoryException;

    public ArrayList<T> getEntities() {
        return new ArrayList<>(entities);
    }

    @Override
    public Iterator<T> iterator() {
        // The iterator of the repository is a Java iterator.
        // The implementation uses the internal iterator of the repository's backing list.
        return entities.iterator();
    }
}
