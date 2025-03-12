package Service;

import Domain.Cake;
import Domain.IDGenerator;
import Domain.Order;
import Exceptions.ObjectNotFoundException;
import Exceptions.RepositoryException;
import Repository.AbstractRepository;

import java.util.*;
import java.util.stream.Collectors;


public class OrderService {
    private final AbstractRepository<Order> orderRepo;
    private final IDGenerator idGenerator;

    public OrderService(AbstractRepository<Order> orderRepo, IDGenerator idGenerator) {

        this.orderRepo = orderRepo;
        this.idGenerator = idGenerator;
    }

    public void addOrder(ArrayList<Cake> cakes, Date date) throws RepositoryException {
        int nextID = idGenerator.generateId();
        Order order = new Order(nextID, cakes, date);

        orderRepo.add(order);
    }


    public ArrayList<Order> getOrders() throws NullPointerException{
        ArrayList<Order> orders;
        orders = orderRepo.getEntities();
        if (orders.isEmpty()) {
            throw new NullPointerException( "There are no orders yet!");
        }
        return orders;
    }

    public void deleteOrder(int id) throws RepositoryException {
        orderRepo.removeById(id);
    }

    public void updateOrder(int id, ArrayList<Cake> cakes, Date date) throws RepositoryException{
        Order existingOrder = orderRepo.getEntityById(id);
        if (existingOrder == null) {
            throw new ObjectNotFoundException("Order with id = " + id + " does not exist!");
        }

        Order updatedOrder = new Order(id, cakes, date);
        orderRepo.update(updatedOrder);
    }


    // metoda pentru a obține raportul:
        //Numărul de torturi comandate în fiecare zi (o comandă poate avea unul sau mai multe torturi).
        // Se vor afișa doar acele date pentru care au fost înregistrate comenzi,
        // precum și numărul de torturi comandate în fiecare zi.
        // Afișarea se va realiza în ordine descrescătoare a numărului de torturi comandate în fiecare zi.

    public List<Map.Entry<Date, Integer>> getCakesOrderedPerDay() throws RepositoryException {

        ArrayList<Order> orders = orderRepo.getEntities();

        Map<Date, Integer> cakesPerDay = orders.stream().collect(Collectors.toMap(
                        Order::getDate,
                        order -> order.getCakes().size(),
                        (existing, newValue) -> {
                            return existing + newValue;
                }
                ));

        return cakesPerDay.entrySet().stream()
                .sorted((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()))
                .collect(Collectors.toList());
    }


//    public List<Map.Entry<Date, Integer>> getCakesOrderedPerDay() throws RepositoryException {
//        // toate comenzile
//        ArrayList<Order> orders = orderRepo.getEntities();
//
//        // grupez comenzile pe zi si adun nr de torturi intr-un dictionar
//        Map<Date, Integer> cakesPerDay = new HashMap<>();
//
//        for (Order order : orders) {
//
//            Date orderDate = order.getDate();
//
//            int numberOfCakes = order.getCakes().size();
//
//            // Dacă data comenzii există deja în hartă, adăugăm torturile comandate
//            cakesPerDay.put(orderDate, cakesPerDay.getOrDefault(orderDate, 0) + numberOfCakes);
//        }
//
//        // dictionarul in transform într-o listă de entry-uri (perechi de tipul cheie-valoare)
//        List<Map.Entry<Date, Integer>> cakesList = new ArrayList<>(cakesPerDay.entrySet());
//
//        // sertez lista descrescător după numărul de torturi comandate
//        cakesList.sort(
//                (entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue())
//        );
//
//        return cakesList;
//    }


    // metoda pentru a obține raportul:
        //Numărul de torturi comandate în fiecare lună a anului.
        // Se vor afișa lunile anului, precum și numărul de torturi comandate în fiecare lună.
        // Afișarea se va face în ordine descrescătoare a numărului de torturi comandate.

    public List<Map.Entry<String, Integer>> getCakesOrderedPerMonth() throws RepositoryException {
        ArrayList<Order> orders = orderRepo.getEntities();

        Map<String, Integer> cakesPerMonth = orders.stream()
                .collect(Collectors.toMap(
                        order -> {
                            Calendar calendar = Calendar.getInstance();
                            calendar.setTime(order.getDate());
                            int month = calendar.get(Calendar.MONTH) + 1; // Calendar.MONTH starts at 0
                            int year = calendar.get(Calendar.YEAR);
                            return year + "-" + String.format("%02d", month);
                        },
                        order -> order.getCakes().size(),
                        (existing, newValue) -> {
                            return existing + newValue;
                        }
                ));

        return cakesPerMonth.entrySet().stream()
                .sorted((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()))
                .collect(Collectors.toList());
    }


//    public List<Map.Entry<String, Integer>> getCakesOrderedPerMonth() throws RepositoryException {
//
//        ArrayList<Order> orders = orderRepo.getEntities();
//
//        //  grupez comenzile pe luni si adun nr de torturi intr-un dictionar
//        Map<String, Integer> cakesPerMonth = new HashMap<>();
//
//        for (Order order : orders) {
//
//            Date orderDate = order.getDate();
//
//            // luna și anul din data comenzii
//            Calendar calendar = Calendar.getInstance();
//            calendar.setTime(orderDate);
//            int month = calendar.get(Calendar.MONTH) + 1;  // Calendar.MONTH începe de la 0 = ianuarie
//            int year = calendar.get(Calendar.YEAR);
//
//
//            String monthYear = year + "-" + String.format("%02d", month);
//
//            int numberOfCakes = order.getCakes().size();
//
//            cakesPerMonth.put(monthYear, cakesPerMonth.getOrDefault(monthYear, 0) + numberOfCakes);
//        }
//
//        // dictionarul in transform într-o listă de entry-uri (perechi de tipul cheie-valoare)
//        List<Map.Entry<String, Integer>> cakesList = new ArrayList<>(cakesPerMonth.entrySet());
//
//        // sortez lista descrescător după numărul de torturi comandate
//        cakesList.sort(
//                (entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue())
//        );
//
//        return cakesList;
//    }


    // metoda pentru a obține raportul:
        // Cele mai des comandate torturi.
        // Se vor afișa toate informațiile despre fiecare tort,
        // împreună cu numărul total de comenzi pentru fiecare.
        // Țineți cont că o comandă poate include mai multe torturi de tipuri diferite.
        // Afișarea se va face în ordine descrescătoare a numărului de comenzi pentru fiecare tort.

    public List<Map.Entry<Cake, Integer>> getMostOrderedCakes() throws RepositoryException {

        ArrayList<Order> orders = orderRepo.getEntities();

        // numar de cate ori apare fiecare tort intr-un dictionar
        Map<Cake, Integer> cakeOrderCount = new HashMap<>();

        for (Order order : orders) {
            for (Cake cake : order.getCakes()) {
                // dacă tortul există deja în dictionar, incrementăm contorul
                cakeOrderCount.put(cake, cakeOrderCount.getOrDefault(cake, 0) + 1);
            }
        }

        // transform dicionarul într-o listă de perechi (tort, număr de comenzi)
        List<Map.Entry<Cake, Integer>> sortedCakes = new ArrayList<>(cakeOrderCount.entrySet());

        // sortez lista descrescător după numărul de comenzi
        sortedCakes.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));

        return sortedCakes;
    }
}
