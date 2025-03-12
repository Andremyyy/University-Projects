#include <iostream>
using namespace std;
#include "UIDulciuri.h"
#include "Service.h"
#include "Dulciuri.h"
#include "teste.h"
#include "Pereche.h"
#include "Tranzactie.h"
#include "ATM.h"
#include "Colectie.h"
#include "FileRepoDulciuri.h"
#include "MyException.h"
#include "Validator.h"
#include "ValidatorException.h"

int main() {

    try {
        testDulciuri();
        testRepo();
        testService();
        testATM();

        cout << "teste functioneaza!" << endl << endl << endl;
    }
    catch (MyException &myex) {
        cout << "Erori la teste: " << myex.getMessage() << endl;
    }
    catch (ValidatorException &vaex){
        cout << "Erori la teste: " << vaex.getMessage() << endl;
    }
    catch (...) {
        cout << "Alte exceptii... " << endl;
    }

    try {
        RepoDulciuri<Dulciuri> repo;
        FileRepoDulciuri<Dulciuri> frepo("dulciuri.txt");
        Service service(frepo);
        Validator validator1;
        UIDulciuri ui(service, ATM(Colectie(), service), validator1);

        Colectie bancnote_initiale;
//    bancnote_initiale.add(Pereche(100, 50)); // 50 de bancnote de 100
//    bancnote_initiale.add(Pereche(50, 45));  // 45 de bancnote de 50
//    bancnote_initiale.add(Pereche(10, 100)); // 100 de bancnote de 10

        ATM atm(bancnote_initiale, service);

        ui.showMenu();
    }

    catch (ValidatorException &vaex){
        cout << "Erori validate date de intrare: " << vaex.getMessage() << endl;
  } catch(MyException &ex){
        cout << "!!!!ATENTIE: " << ex.getMessage() << endl;
    }    catch(...){
        cout << " Alte probleme: ..." << endl;
    }
    return 0;
}
