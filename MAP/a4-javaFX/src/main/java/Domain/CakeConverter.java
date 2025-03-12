package Domain;

public class CakeConverter extends EntityConvertor<Cake>{

    public CakeConverter(Class<Cake> entityClass) {
        super(entityClass);
    }

    @Override
    public String toString(Cake cake) {
        return cake.getId() + ";" + cake.getTypeOfCake();
    }

    @Override
    public Cake fromString(String string) {
        String[] tokens = string.split(";");
        try {
            // verific dacă avem exact două părți (id și tipul tortului)
            if (tokens.length != 2) {
                throw new RuntimeException("Invalid input format for Cake. Expected format: 'id;typeOfCake'");
            }

            // .trim() elimină spațiile albe înainte și după tokeni

            int id = Integer.parseInt(tokens[0].trim());
            String typeOfCake = tokens[1].trim();
            return new Cake(id, typeOfCake);
        } catch (Exception e){
            System.out.println("Error parsing line: " + string);
            throw new RuntimeException("Invalid input format for Cake. Expected format: 'id;typeOfCake'" + e.getMessage());
        }

    }
}
