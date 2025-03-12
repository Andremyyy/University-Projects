//
// Created by Asus on 4/23/2024.
//

#include "teste.h"
#include "Dulciuri.h"
#include "Service.h"
#include "RepoDulciuri.h"
#include <cassert>
#include "ATM.h"

void testRepo() {
    RepoDulciuri<Dulciuri> repo;

    // Adăugare de elemente
    Dulciuri ciocolata("Ciocolata", 10);
    Dulciuri bomboane("Bomboane", 5);

    repo.addElem(ciocolata);
    repo.addElem(bomboane);

    assert(repo.getSize() == 2); // Verificăm că repo-ul are două elemente

    // Testăm ștergerea unui element
    repo.deleteElem(bomboane); // Ștergem un element
    assert(repo.getSize() == 1); // Verificăm că dimensiunea repo-ului este acum 1

    // Testăm actualizarea unui element
    Dulciuri ciocolataNoua("Ciocolata Noua", 15); // Un obiect nou
    try {
        repo.updateElem(ciocolata, ciocolataNoua); // Actualizăm elementul
        assert(repo.findElem(ciocolataNoua) != -1); // Verificăm că elementul actualizat există
    } catch (MyException &myex) {
        cout << myex.getMessage()<< endl;
    }

    // Verificăm obținerea tuturor elementelor
    vector<Dulciuri> allDulciuri = repo.getAll(); // Obținem toate elementele
    assert(allDulciuri.size() == 1); // Verificăm că dimensiunea este 1
    assert(allDulciuri[0].getNume() == "Ciocolata Noua"); // Verificăm numele elementului rămas
}

void testDulciuri() {

    // Creare de obiecte Dulciuri
    Dulciuri ciocolata("Ciocolata", 10);
    Dulciuri bomboane("Bomboane", 5);

    // Testarea getter-elor
    assert(ciocolata.getPret() == 10);
    assert(bomboane.getNume() == "Bomboane");

    // Testarea setter-elor
    ciocolata.setPret(12); // Modificăm prețul
    assert(ciocolata.getPret() == 12); // Verificăm noul preț

    // Testarea operatorului de egalitate
    Dulciuri ciocolataCopie = ciocolata;
    assert(ciocolata == ciocolataCopie); // Ar trebui să fie egale

}

void testService() {
    RepoDulciuri<Dulciuri> repo;
    Service service(repo);

    // Adăugăm un element pentru a ne asigura că repo-ul nu este gol
    service.add("Ciocolata", 10);
    assert(service.getAll().size() == 1); // Verificăm că există cel puțin un element


    // Testăm actualizarea unui element
    try {
        Dulciuri ciocolataNoua(6, "Ciocolata Noua", 15);
        // Ne asigurăm că există cel puțin un element înainte de actualizare
        if (!service.getAll().empty()) {
            int cod = service.getAll()[0].getCod(); // Obținem codul
            assert( service.getAll()[0].getCod() == 6);
            service.update(cod, "Ciocolata", 10, ciocolataNoua); // Actualizăm
            assert(service.getAll()[0].getNume() == "Ciocolata Noua"); // Verificăm
        } else {
            cerr << "Nu există suficiente elemente pentru actualizare." << std::endl;
        }
    } catch (MyException &myex) {
        cout << myex.getMessage() << endl;
    }


    service.add("Bomboane", 5);
    // Testăm ștergerea unui element
    try {
        service.remove(6, "Ciocolata Noua", 15); // Ștergem dulcele cu cod 6
        assert(service.getAll().size() == 1); // Repo-ul ar trebui să aibă un singur element
    } catch (MyException &myex) {
        cout << myex.getMessage() << endl;
    }

    // Testăm căutarea unui element
    assert(service.find(7, "Bomboane", 5) != -1); // Ar trebui să existe
    assert(service.find(2, "Ciocolata Noua" , 15) == -1); // Nu ar trebui să existe
}


void testATM(){

    // Testăm constructorul implicit și constructorul de copiere
    Colectie colectie;
    colectie.add(Pereche(50, 10)); // 10 bancnote de 50
    colectie.add(Pereche(10, 20)); // 20 bancnote de 10

    RepoDulciuri<Dulciuri> repo;
    Service service(repo); // Asigură-te că Service este bine definit și utilizat
    ATM atm(colectie, service); // Inițializăm ATM cu colectia și serviciul

    // Testăm constructorul de copiere
    ATM atm_copiat(atm, service);
    assert(atm_copiat == atm );

    // Testăm operatorul de atribuire
    ATM atm_atribuire = atm;
    assert(atm_atribuire == atm);

    try {
        // Testăm confirmarea tranzacției
        bool tranzactie_confirmata = atm.confirmare_tranzactie(1, 100, 1, "Produs", 30);
        assert(tranzactie_confirmata);
    } catch (MyException &myex) {
    cout << myex.getMessage() << endl;
    }


    // Testăm adăugarea bancnotelor
    atm.adauga_bancnote(Pereche(100, 5)); // Adăugăm 5 bancnote de 100
    Colectie bancnote = atm.getBancnoteDisponibile();
    assert(bancnote.getFrecventa(100) == 5 );

    // Testăm eliminarea bancnotelor
    assert(bancnote.getFrecventa(10) == 18 );

    atm.elimina_bancnote(10, 5); // Eliminăm 5 bancnote de 10

    assert(bancnote.getFrecventa(10) == 13 );

    /// Testăm adăugarea de bancnote și setarea colecției de bancnote
    Colectie noi_bancnote;
    noi_bancnote.add(Pereche(200, 3)); // 3 bancnote de 200
    atm.setBancnoteDisponibile(noi_bancnote);

    Colectie nou_bancnote = atm.getBancnoteDisponibile();

    // Verificăm dimensiunea colecției
    assert(nou_bancnote.getSize() == 1); // Ar trebui să fie un singur tip de bancnote

    // Verificăm frecvența pentru bancnota de 200
    assert(nou_bancnote.getFrecventa(200) == 3); // Ar trebui să fie 3 bancnote de 200


}