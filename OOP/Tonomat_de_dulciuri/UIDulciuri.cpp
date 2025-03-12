//
// Created by Asus on 4/23/2024.
//

#include "UIDulciuri.h"
#include "ATM.h"
#include "Dulciuri.h"
#include "Colectie.h"
#include "Pereche.h"
#include "MyException.h"
#include "ValidatorException.h"
#include "Validator.h"


UIDulciuri::~UIDulciuri() = default;



void UIDulciuri::addDulce() {


    string nume;
    cout << "Introduceti numele dulcelui: " << endl;
    cin >> nume;

    try{
        validator.validateNume(nume);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    bool ok = false;

    int pret;
    while (!ok) {
        cout << "Introduceti pretul dulcelui: " << endl;
        cin.clear();
        cin >> pret;


        try {
            validator.validatePret(pret);
            ok = true;
        }
        catch (ValidatorException &vaex) {
            cout << vaex.getMessage() << endl;
            ok = false;
        }
        catch (...){
            cout << "Eroare" << endl;
            ok = false;
        }
    }


    service.add(nume, pret);

    cout << "Adaugare cu succes!" << endl;



}

void UIDulciuri::deleteDulce() {
    int cod;
    cout << "Introduceti codul dulcelui de sters: " << endl;
    cin >> cod;

    try{
        validator.validateCod(cod);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    string nume;
    cout <<"Introduceti numele dulcelui: " << endl;
    cin >> nume;

    try{
        validator.validateNume(nume);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    int pret;
    cout << "Introduceti pretul dulcelui: " << endl;
    cin >> pret;

    try{
        validator.validatePret(pret);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    try {
        // Verificăm dacă dulcele există în baza codului
        int index = service.find(cod, nume, pret); // căutăm folosind codul
        if (index != -1) { // Dacă a fost găsit
            service.remove(cod, nume, pret); // Eliminăm folosind codul
            cout << "Stergere cu succes!" << endl;
        } else {
            cout << "NU s-a putut sterge, pentru ca nu exista!" << endl; // Gestionare eroare
        }
    }
    catch (MyException &myex) {
        cout << myex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }
}


void UIDulciuri::updateDulce() {
    int cod;
    cout << "Introduceti codul dulcelui de sters: " << endl;
    cin >> cod;

    try{
        validator.validateCod(cod);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    string nume;
    cout <<"Introduceti numele dulcelui: " << endl;
    cin >> nume;

    try{
        validator.validateNume(nume);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    int pret;
    cout << "Introduceti pretul dulcelui: " << endl;
    cin >> pret;

    try{
        validator.validatePret(pret);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }



    int codNou;
    cout << "Introduceti noul cod al dulcelui: " << endl;
    cin >> codNou;

    try{
        validator.validateCod(codNou);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    string numeNou;
    cout <<"Introduceti noul nume al dulcelui: " << endl;
    cin >> numeNou;

    try{
        validator.validateNume(numeNou);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    int pretNou;
    cout << "Introduceti noul pret al dulcelui: " << endl;
    cin >> pretNou;

    try{
        validator.validatePret(pretNou);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    try {


        if (service.find(cod, nume, pret) != -1) {
            Dulciuri dulceNou(codNou, numeNou, pretNou);
            service.update(cod, nume, pret, dulceNou);
            cout << "Modificare cu succes!" << endl;
        } else
            cout << "NU s-a putut modifica, pentru ca nu exista!" << endl;

    }
    catch (MyException &myex){
        cout << myex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

}

void UIDulciuri::findDulce() {
    int cod;
    cout << "Introduceti codul dulcelui pe care doriti sa il cautati: " << endl;
    cin >> cod;

    try{
        validator.validateCod(cod);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    bool ok = false;
    vector<Dulciuri> elems = service.getAll();
    for (auto dulce:elems)
        if (dulce.getCod() == cod) {
            ok = true;
            cout << dulce.getCod() <<  " " << dulce.getNume() << " " << dulce.getPret() << endl;
        }
    if (!ok)
        cout << "Nu exista acest dulce!"<< endl;
}


void UIDulciuri::getAll() {
    vector<Dulciuri> elems = service.getAll();
    for (auto dulce:elems)
        cout << dulce.getCod() <<  " " << dulce.getNume() << " " << dulce.getPret() << endl;
}


void UIDulciuri::showMenu() {
    bool ok = true;
    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1. Adauga dulce \n"
                "2. Afiseaza dulciuri \n"
                "3. Sterge dulce \n"
                "4. Modifica dulce \n"
                "5. Gaseste dulce dupa cod \n"
                "6. Adauga monede \n"
                "7. Incearca sa cumperi un produs \n"
                "8. Afiseaza monede \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: " << endl;
        cin >> optiune;

        if (!cin)
            throw MyException("Optiunea trebuie sa fie de tip int!");

        switch (optiune) {
            case 1: addDulce(); break;
            case 2: getAll(); break;
            case 3: deleteDulce(); break;
            case 4: updateDulce(); break;
            case 5: findDulce(); break;
            case 6: addMoneda(); break;
            case 7: addCerere(); break;
            case 8: showMonede(); break;
            case 0: ok = false; break;
            default: break;
        }
    }
}


void UIDulciuri::addMoneda() {
    int valoare, numar;
    cout << endl;
    cout << "Introduceti valoarea de adaugat: " << endl;
    cin >> valoare;

    try{
        validator.validateBancota(valoare);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    cout << "Introduceti numarul de monezi de adaugat: " << endl;
    cin >>  numar;

    try{
        validator.validateValoare(numar);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

    atm.adauga_bancnote(Pereche(valoare, numar)); // Adăugați moneda
    cout << "Monezile au fost adaugate.\n";
    cout << endl << endl << endl;
}


void UIDulciuri::addCerere() {

        int idTranzactie, suma;
        cout << endl;
        cout << "Introduceti ID-ul tranzactiei platit: " << endl;
        cin >> idTranzactie;

    try{
        validator.validateCod(idTranzactie);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

        cout << "Introduceti suma de platit: "<< endl;
        cin >> suma;

    try{
        validator.validatePret(suma);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

        int cod;
        cout << "Introduceti codul dulcelui de sters: " << endl;
        cin >> cod;

    try{
        validator.validateCod(cod);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

        string nume;
        cout <<"Introduceti numele dulcelui: " << endl;
        cin >> nume;

    try{
        validator.validateNume(nume);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }

        int pret;
        cout << "Introduceti pretul dulcelui: " << endl;
        cin >> pret;

    try{
        validator.validatePret(pret);
    }
    catch (ValidatorException &vaex){
        cout << vaex.getMessage() << endl;
        return; // Oprește execuția în caz de eroare
    }


        bool confirmat = atm.confirmare_tranzactie(idTranzactie, suma, cod, nume, pret);  // Efectuează tranzacția

        if (confirmat) {
            cout << "Tranzactia a fost efectuata.\n";
        } else {
            cout << "Tranzactia a fost anulata sau a esuat.\n";
        }
    cout << endl << endl << endl;
}


void UIDulciuri::showMonede() {
    Colectie bancnote_disponibile = atm.getBancnoteDisponibile(); // Afișează bancnotele disponibile
    cout << endl;
    cout << "Bancnotele disponibile in bancomat:\n";
    for (int i = 0; i < bancnote_disponibile.getSize(); i++) {
        Pereche p = bancnote_disponibile.getAt(i);
        cout << "Bancnote de " << p.element << " a cate " << p.frecventa << "\n";
    }
    cout << endl << endl << endl;
}

