package Domain;

//clasa abstracta: nu putem crea obiecte de tip Domain.Entity

//Entity este clasa "mama" <=> toate clasele din Domain (in afara de IDGenerator)
//sunt derivate din Entity (toate au id)


import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serial;
import java.io.Serializable;

public abstract class Entity implements Serializable{
    protected int id;
    @Serial
    private static final long serialVersionUID = 1L;  // Change '1L' to your consistent serialVersionUID
    public Entity() {

    }

    // Constructor pentru cazurile în care primim un ID specific
    @JsonCreator
    public Entity(@JsonProperty("id") int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }
}
