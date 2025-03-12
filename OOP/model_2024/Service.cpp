//
// Created by ema_a on 5/28/2024.
//

#include "Service.h"

Service::Service(Repo<Bacterie> bacterii) : elemRepo(bacterii)  {

}

void Service::add(string nume, int varsta, int tip) {
    Bacterie b(nume, varsta, tip);
    elemRepo.addElem(b);
}

vector<Bacterie> Service::getAll() {
    return elemRepo.getAll();
}



double Service::calcMedieBacterii(int timp) {
    int curr = 0; // iterația de timp curentă
    int varsteb1 = 0; // calculează varsta bacteriilor de tip 1
    int varsteb2 = 0; // calculează varsta bacteriilor de tip 2
    float contor = 0; // calculează numărul de bacterii

    Repo<Bacterie> copie = this->elemRepo;

    while (curr < timp) {
        varsteb1 = 0;
        varsteb2 = 0;
        contor = 0;
        for (auto &b : copie.getAll()) {
            // Verifică tipul bacteriei și ajustează varsta corespunzător
            if (b.getTip() == 1) {
                // Ștergeți bacteriile de tip 1
                copie.deleteElem(b);
            } else { // tipul 2
                varsteb2 += b.getVarsta();
            }

            // Simulați adăugarea de două noi bacterii cu vârsta 0
            if (b.getTip() == 1 && (curr % 1 == 0 || curr == 0)) {
                Bacterie baby1(b.getNume(), 0, 1);
                Bacterie baby2(b.getNume(), 0, 1);
                copie.addElem(baby1);
                copie.addElem(baby2);
                // Actualizați contorul pentru cei doi bebeluși adăugați
                contor += 2;
            }

            // Simulați reproducerea bacteriilor de tipul 2
            if (b.getTip() == 2 && (curr % 3 == 0)) {
                Bacterie baby1(b.getNume(), 0, 1);
                copie.addElem(baby1);
                contor++; // Actualizați contorul pentru bebelușul adăugat
            }

            // Creșteți vârsta bacteriilor de tipul 2
            if (b.getTip() == 2) {
                contor++;
                Bacterie bNew(b.getNume(), b.getVarsta() + 1, b.getTip());
                varsteb2++;
                copie.updateElem(b, bNew);
            }
        }

        curr++;
    }

    // Actualizați repo-ul original cu modificările făcute
    elemRepo = copie;

    // Calculați media și returnați-o
//    cout << varsteb1 + varsteb2<< " " << contor << endl;
    return (varsteb2 + varsteb1) / contor;
}



