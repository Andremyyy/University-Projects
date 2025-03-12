package Domain;

public abstract class EntityConvertor <T extends Entity> {
    // Variabila pentru stocarea clasei entității
    private final Class<T> entityClass;

    // Constructor pentru a seta tipul clasei
    public EntityConvertor(Class<T> entityClass) {
        this.entityClass = entityClass;
    }

    public abstract String toString(T entity);

    public abstract T fromString(String string);

    // Metoda pentru a obține tipul clasei entității
    public Class<T> getEntityClass() {
        return entityClass;
    }
}
