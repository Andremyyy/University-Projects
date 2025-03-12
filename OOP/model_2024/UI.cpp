//
// Created by ema_a on 5/28/2024.
//

#include "UI.h"

void UI::addBacterie() {

    string nume;
    int varsta;
    int tip;

    cout<<"Introduceti numele: ";
    cin>>nume;
    cout<<"Introduceti varsta: ";
    cin>>varsta;
    cout<<"Introduceti tipul: ";
    cin>>tip;

    service.add(nume, varsta, tip);

    cout << "Bacterie adaugata cu succes!" << endl;
}

void UI::showMenu() {
    bool ok = true;
    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1. Adauga bacterie \n"
                "2. Afiseaza toate bacteriile \n"
                "3. Afiseaza bacterii dupa tip \n"
                "4. Calculeaza media varstelor bacteriilor la un timp dat \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: " << endl;
        cin >> optiune;


        switch (optiune) {
            case 1: addBacterie(); break;
            case 2: showAllBacterii(); break;
            case 3: showBacteriiTip(); break;
            case 4: CalculeazaBacteriiTimp(); break;
            case 0: ok = false; break;
            default: break;
        }
    }
}

void UI::showAllBacterii() {
    vector<Bacterie> elems = service.getAll();
    for (auto bacterie:elems)
        cout << bacterie.getNume() <<  " " << bacterie.getVarsta() << " " << bacterie.getTip() << endl;
}

void UI::showBacteriiTip() {

    int tip;
    cout<<"Introduceti tipul: ";
    cin>>tip;

    vector<Bacterie> elems = service.getAll();
    cout << "Bacteriile de tipul " << tip << " sunt: " << endl;
    for (auto bacterie:elems)
        if (bacterie.getTip() == tip)
            cout << bacterie.getNume() <<  " " << bacterie.getVarsta() << " " << bacterie.getTip() << endl;

}

void UI::CalculeazaBacteriiTimp() {

    int timp;
    cout<<"Introduceti timpul: ";
    cin >> timp;

    float medie = service.calcMedieBacterii(timp);


    cout << "Media varstelor bacteriilor la timpul  " << timp << " este: " << medie << endl;
}
