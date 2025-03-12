//
// Created by ema_a on 5/30/2024.
//

#include "Service.h"
#include <stdlib.h>


Service::Service(Repo<Meci> meciuri) {
    this->elemRepo = meciuri;

}

void Service::addMeci(string echipa1, string echipa2, int golEchipa1, int golEchipa2) {
    if (golEchipa1 < 0 || golEchipa2 < 0 || echipa1 == echipa2){
        throw invalid_argument("Date invalide!");
    }
    Meci meci(echipa1, echipa2, golEchipa1, golEchipa2);
    this->elemRepo.addElem(meci);
}

vector<Echipa> Service::getEchipe() {
    if (elemRepo.isEmpty()) {
        throw invalid_argument("Nu exista echipe in lista de meciuri!");
    }
    vector<Echipa> echipe;
    for (int i = 0; i < this->elemRepo.getSize(); i++) {
        Meci meci = this->elemRepo.elemAtPos(i);

        string echipa1 = meci.getEchipa1();
        string echipa2 = meci.getEchipa2();

        int golEchipa1 = meci.getGolEchipa1();
        int golEchipa2 = meci.getGolEchipa2();

        int index1 = -1; // pozitia in vectorul de echipe a echipei 1
        int index2 = -1; // pozitia in vectorul de echipe a echipei 2
        for (int j = 0; j < echipe.size(); j++) {
            if (echipe[j].getNume() == echipa1) {
                index1 = j;
            }
            if (echipe[j].getNume() == echipa2) {
                index2 = j;
            }
        }
        // adaug echipa1 in vectorul de echipe daca nu a mai participat la niciun meci
        if (index1 == -1) {
            echipe.push_back(Echipa(echipa1, 0));
            index1 = echipe.size() - 1;
        }
        // adaug echipa2 in vectorul de echipe daca nu a mai participat la niciun meci
        if (index2 == -1) {
            echipe.push_back(Echipa(echipa2, 0));
            index2 = echipe.size() - 1;
        }

        // calculez punctajul meciului pt fiecare echipa
        if (golEchipa1 > golEchipa2) {
            echipe[index1].punctaj += 3;
        } else if (golEchipa1 < golEchipa2) {
            echipe[index2].punctaj += 3;
        } else {
            echipe[index1].punctaj += 1;
            echipe[index2].punctaj += 1;
        }

    }

    // sortare descrescatoare dupa punctaj
    for (int i = 0; i < echipe.size() - 1; i++) {
        for (int j = i + 1; j < echipe.size(); j++) {
            if (echipe[i].getPunctaj() < echipe[j].getPunctaj()) {
                swap(echipe[i], echipe[j]);
            }
        }
    }

    return echipe;


}

vector<Echipa> Service::getCastigatori() {
    try {
        vector<Echipa> echipe = getEchipe();
        for (int i = 0; i < echipe.size() - 1; i++) {
            for (int j = i + 1; j < echipe.size(); j++) {
                //float randNr = rand() % (int)val;
                int golEchipa1 = rand() % 6;
                int golEchipa2 = rand() % 6;
                cout << echipe[i].getNume() << " vs " << echipe[j].getNume() << " scor: " << golEchipa1 << "-" << golEchipa2 << endl;
                if (golEchipa1 > golEchipa2) {
                    echipe[i].punctaj += 3;
                } else if (golEchipa1 < golEchipa2) {
                    echipe[j].punctaj += 3;
                } else {
                    echipe[i].punctaj += 1;
                    echipe[j].punctaj += 1;
                }
            }
        }
        int maxPunctaj = 0;
        for (auto& e : echipe) {
            if (e.getPunctaj() > maxPunctaj) {
                maxPunctaj = e.getPunctaj();
            }
        }
        int nrCastigatori = 0;
        vector <Echipa> castigatori;
        for (auto& e : echipe) {
            if (e.getPunctaj() == maxPunctaj) {
                castigatori.push_back(e);
            }
        }
        return castigatori;
    }
    catch (invalid_argument& ex) {
        throw invalid_argument(ex.what());
    }

}
