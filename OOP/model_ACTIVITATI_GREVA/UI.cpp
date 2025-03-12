//
// Created by ema_a on 6/1/2024.
//

#include "UI.h"
using namespace std;



void UI::showMenu() {
        bool ok = true;

        service.addProfesor("Popescu", "Matematica", {"11C", "12B"}, true);
        service.addProfesor("Ion", "Romana", {"10A", "12B"}, false);
        service.addProfesor("Dicu", "Informatica", {"10A", "12B"}, false);
        service.addProfesor("Georgescu", "Istorie", {"11C"}, true);
        service.addProfesor("Popa", "Biologie", {"11C", "12B", "10A"}, false);
        service.addProfesor("Alexandrescu", "Geografie", { "11C", "12B","10A"}, true);
        while (ok) {
            cout << "-----------Meniu:-----------" << endl;
            cout << "1. Afiseaza numarul de profesori in greva. \n"
                    "2. Afiseaza disciplina/disciplinele cu cei mai multi profesori in greva. \n"
                    "3. Afiseaza clasa unde sunt cei mai multi profesori in greva care ar trebui sa predea. \n"
                    "4. Afiseaza disciplinele unde se poate preda in functie de orarul dat de la tastatura. \n"
                    "5. Adauga profesor. \n"
                    "6. Afiseaza profesorii. \n"
                    "0. EXIT \n\n\n";
            int optiune;
            cout << "Alege o optiune: " << endl;
            cin >> optiune;


            switch (optiune) {
                case 1: statisticaProfGreva(); break;
                case 2: statisticaDisciplinaMaxGreva();break;
                case 3: calcClasaMaxGreva(); break;
                case 4: afiseazaOre(); break;
                case 5: addProfesor(); break;
                case 6: afiseazaProfesori(); break;
                case 0: ok = false; break;
                default: break;
            }
        }
    }

void UI::statisticaProfGreva() {
    try {
        int nr = service.calcNrProfesoriGreva();
        cout << "Numarul de profesori in greva este: " << nr << endl;
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }
}

void UI::statisticaDisciplinaMaxGreva() {

    try {
        vector<string> discipline = service.calcDisciplinaMaxGreva();
        cout << "Disciplina/disciplinelele cu cei mai multi profesori in greva este/sunt: " << endl;
        for (string disciplina : discipline) {
            cout << disciplina << endl;
        }
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }

}

void UI::calcClasaMaxGreva() {
    try {
        string clasa = service.calcClasaMaxGreva();
        cout << "Clasa cu cei mai multi profesori in greva este : " << clasa << endl;
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }
}
//- Cunoscându-se orarul unei clase pentru o zi anume,
// să se identifice disciplinele care se pot preda de
//profesorii care nu sunt în grevă
// (de ex. clasa a 6-a, ar avea Matematică. Română, Istorie, Biologie, dar
//pentru că profesorii de Matematică și Română sunt în grevă,
// doar orele de Istorie și Biologie se pot
//desfășura). (2p)
void UI::afiseazaOre() {
    try {
        string clasa;
        cout << "Dati clasa pentru care doriti sa vedeti orele: " << endl;
        cin >> clasa;
        cout << "Dati orarul clasei: (introduceti <stop> cand ati terminat)" << endl;
        string orarul[20];
        int nr=0;
        string ora;

        while (true) {
            cin >> ora;
            if (ora == "stop") {
                break;
            }
            orarul[nr] = ora;
            nr++;
            if(nr == 19)
                break;
        }

        vector < string > discipline = service.calcDisciplineValabile(clasa, orarul, nr);
        cout << "Disciplinele care se pot preda sunt: "<< endl;
        for (string disciplina : discipline) {
            cout << disciplina << endl;
        }
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }

}

void UI::addProfesor() {
    string nume;
    string disciplina;
    vector<string> clase;
    bool inGreva;
    cout << "Dati numele profesorului: " << endl;
    cin >> nume;
    cout << "Dati disciplina pe care o preda: " << endl;
    cin >> disciplina;
    cout << "Dati clasele la care preda: (introduceti <<stop>> cand ati terminat) " << endl;
    string clasa;
    while (clasa!="stop") {
        cin >> clasa;
        if (clasa == "stop") {
            break;
        }
        clase.push_back(clasa);
    }
    cout << "Este in greva? 1/0 " << endl;
    cin >> inGreva;
    service.addProfesor(nume, disciplina, clase, inGreva);
}

void UI::afiseazaProfesori() {
    vector<Profesor> profesori = service.afiseazaProfesori();
    for (Profesor profesor : profesori) {
        cout << profesor.getNume() << " " << profesor.getDisciplina() << " ";
        for (string clasa : profesor.getClase()) {
            cout << clasa << " ";
        }
        cout << profesor.getInGreva() << endl;
    }

}
