package Exceptions;

public class RepositoryException extends Exception{

    public RepositoryException(String s){

        super(s);

    }

    public RepositoryException(String message, Throwable cause) {
        super(message, cause);
    }
}
