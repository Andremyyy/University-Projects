
//Activități în timpul grevei

//inc: 5.39 pm
//fin : 6.49 pm


//Datorită situației curente, coordonatorul unei școli
// generale are nevoie de ajutor în re-planificarea orelor, având
//în vedere că anumiți profesori sunt în grevă.
//
//Pentru început, coordonatorul școlii are nevoie de următoarele statistici:



//Statisticile solicitate se vor afișa pe ecran.
//Dezvoltarea corectă a entităților necesare (1p).
//Stil: specificare sub-algoritmi, claritate cod, etc. (1p).
//Notă1: Aplicația trebuie să fie una stratificată. În cazul în care nu este, se va aplica o depunctare de 2p din nota
//finală.
//Notă2: Aplicația trebuie testată prin aserțiuni; în caz contrar, se va aplica o depunctare de 2p din nota finală.
//Timp de lucru: 70 minute

#include <iostream>
using namespace std;
#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "Profesor.h"

int main() {
//    Teste teste;
//    teste.testService();
//    teste.testRepo();
//    teste.testObiectArta();
//    cout <<"Testele functioneaza!" << endl << endl;
//
    try{
        Repo<Profesor> repo;

        Service service(repo);

        UI ui(service);

        ui.showMenu();
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }
}
