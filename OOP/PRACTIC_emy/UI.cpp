//
// Created by ema_a on 6/3/2024.
//

#include "UI.h"

void UI::showMenu() {
    bool ok = true;

    service.addManuscris("Luceafarul", 1883, "Eminescu", 100);
    service.addManuscris("Maxton", 2012, "julia", 45);
    service.addManuscris("AlbaPoveste", 1892, "Caragiale", 251);
    service.addManuscris("Moara", 1881, "Slavici", 200);
    service.addManuscris("TSITP", 2020, "Jenny", 200);

    service.addManuscris("Ion", 1880, "Rebreanu", 300);
    service.addManuscris("MaraEpilog", 1882, "SMO", 15);
    service.addManuscris("story", 2000, "Camelia", 25);

    service.addManuscris("Enigma", 1882, "Sadoveanu", 50);
    service.addManuscris("POVESTIRE_Usoara", 1925, "Paula", 27);


    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1. Afiseaza toate manuscrisele \n"
                "2. Afiseaza toate manuscrisele care au mai putin de 50 de pagini \n"
                "3. Modifica manuscrisele care contin <<poveste>> , << story>> , <<povestire>>"
                " in nume schimbadu-le anul in anul curent.\n"
                "4. Transformarea manuscriselor de peste 200 de pagini in 2 volume \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: " << endl;
        cin >> optiune;


        switch (optiune) {
            //// APELEZ FUNCTIILE DIN UI.H
            case 1: getAll(); break;
            case 2: getAllLessThan50Pag();break;
            case 3: updateManuscrisDupaNume(); break;
            case 4: premiumUpdate(); break;
            case 0: ok = false; break;
            default: break;
        }
    }
}

void UI::getAll() {
    vector<Manuscris> manuscrise = service.afiseazaManuscrise();
    for (const auto &manuscris : manuscrise) {
        cout << manuscris << endl;
    }
}

void UI::getAllLessThan50Pag() {

    try {
        vector < Manuscris > manuscrise = service.afiseazaLessThan50Pag();

        cout << "Manuscrisele cu mai putin de 50 de pagini sunt: " << endl;
        for (const auto &manuscris: manuscrise) {
            cout << manuscris << endl;
        }
    }
    catch (invalid_argument & e) {
        cout << e.what() << endl;
    }
}

void UI::updateManuscrisDupaNume() {


    try {
        service.updateManuscris();
    }
    catch (invalid_argument & e) {
        cout << e.what() << endl;
    }
}

void UI::premiumUpdate() {
    service.updateVolume();
    try {
        vector < Manuscris > manuscrise = service.afiseazaManuscrise();
        if (manuscrise.empty())
            cout << "Nu exista manuscrise in repo!" << endl;
        else {
            cout << "Manuscrisele cu peste 200 de pagini au fost transformate in 2 volume, dar si cele nemodificate sunt: " << endl;
            for (const auto &manuscris : manuscrise) {
                cout << manuscris << endl;
            }
        }
    }
    catch (invalid_argument & e) {
        cout << e.what() << endl;
    }


}
