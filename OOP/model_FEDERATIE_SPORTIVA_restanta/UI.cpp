//
// Created by ema_a on 5/30/2024.
//

#include "UI.h"
#include "Service.h"


void UI::showMenu() {
    bool ok = true;
    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1.  Adauga meci\n"
                "2.  Afiseaza clasament in functie de punctaj\n"
                "3. Simuleaza turneu \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: \n (1,2 sau 3 / 0- iesire) " << endl;
        cin >> optiune;


        switch (optiune) {
            case 1: addMeci(); break;
            case 2: afiseazaClasament();break;
            case 3: genereazaTurneu(); break;
            case 0: {
                ok = false;
                cout << endl <<"O zi buna!" << endl;
                break;
            }
            default: {
                cout << "Optiune invalida! Introduceti din nou o optiune valida! " << endl;
            } break;
        }
    }
}
//1. Adăugarea unui meci de la tastatură. Nu se pot introduce
// decât scoruri pozitive.
// De asemenea, o echipă nu poate concura împotriva ei însăși.
// Dacă aceste condiții nu sunt îndeplinite, se va afișa un mesaj de eroare.
void UI::addMeci() {
    string echipa1;
    string echipa2;
    int golEchipa1;
    int golEchipa2;

    cout<<"Introduceti echipa 1: " << endl;
    cin >> echipa1;
    cout<<"Introduceti echipa 2: " << endl;
    cin >> echipa2;
    cout<<"Introduceti golurile echipei 1: " << endl;
    cin >> golEchipa1;
    cout<<"Introduceti golurile echipei 2: " << endl;
    cin >> golEchipa2;


    try {

        service.addMeci(echipa1, echipa2, golEchipa1, golEchipa2);
        cout << "Meci adaugat cu succes!" << endl;
    }
    catch (invalid_argument& ex) {
        cout << ex.what() << endl;
    }
}

//2. Afișarea clasamentului în funcție de punctaj
//// (3p)
void UI::afiseazaClasament() {
    try {
        vector < Echipa > echipe = service.getEchipe();

        for (auto &e: echipe) {
            cout << e.getNume() << " " << e.getPunctaj() << endl;
        }
    }
    catch (invalid_argument& ex) {
        cout << ex.what() << endl;
    }
}
//3. Simularea unui întreg turneu,
// în cadrul căruia vor avea loc jocuri între toate combinațiile
// de echipe introduse la punctul 1, ignorându-se scorurile introduse anterior.
// Se vor afișa echipele din fiecare meci,
//scorul obținut de fiecare echipă în parte,
// precum și echipa cu cele mai multe puncte și punctajul ei.
// Dacă sunt mai multe echipe câstigătoare, se vor afișa toate.
// Numărul de goluri marcat de către fiecare echipă va fi un număr generat
// aleator între 0 și 5.
//// (2p)
//ex.: s-au citit echipele e1, e2 si e3. Se va afișa:
//e1 vs e2, scor 2-0
//e1 vs e3, scor 1-1
//e2 vs e3, scor 0-0
//echipa câștigătoare este e1 cu 4 puncte
//
void UI::genereazaTurneu() {
    try {
        vector < Echipa > echipe = service.getCastigatori();
        cout << "Echipele castigatoare sunt: " << endl;
        for (auto& e : echipe) {
            cout << e.getNume() << " cu  " << e.getPunctaj() << " puncte"<< endl;
        }
    }
    catch (invalid_argument& ex) {
        cout << ex.what() << endl;
    }
}


