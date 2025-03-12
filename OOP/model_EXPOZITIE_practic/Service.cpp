//
// Created by ema_a on 5/29/2024.
//

#include "Service.h"
#include <vector>
#include <algorithm>
#include <string>

Service::Service(Repo<ObiectArta> bacterii) {
    this->elemRepo = bacterii;
}

void Service::insertPoz(int pozitie, string autor, string denumire, string categorie, int voturi) {

    if (pozitie < 0 || pozitie > this->elemRepo.getSize()) {
        throw out_of_range("Pozitia nu este valida!");
    }



    ObiectArta obiectArta(autor, denumire, categorie, voturi);

    if (this->elemRepo.findElem(obiectArta) != -1) {
        throw invalid_argument("Obiectul exista deja in expozitie!");
    }

    this->elemRepo.insertPoz(pozitie, obiectArta);

}


// Function to get the index of the category in the vector, returns -1 if not found
int getCategoryIndex(const vector<StatisticaEntry>& statistica, const string& categorie) {
    for (int i = 0; i < statistica.size(); ++i) {
        if (statistica[i].categorie == categorie) {
            return i;
        }
    }
    return -1;
}

vector<StatisticaEntry> Service::getStatistica() {
    vector<StatisticaEntry> statistica;

    // Collecting the statistics
    for (int i = 0; i < this->elemRepo.getSize(); i++) {
        ObiectArta obiectArta = this->elemRepo.elemAtPos(i);
        int obiectArtaVoturi = obiectArta.getVoturi();
        string obiectArtaCategorie = obiectArta.getCategorie();

        int index = getCategoryIndex(statistica, obiectArtaCategorie);
        if (index == -1) {
            statistica.push_back({ obiectArtaCategorie, obiectArtaVoturi });
        } else {

            statistica[index].voturi += obiectArtaVoturi;
        }
    }

    if (statistica.empty()) {
        throw invalid_argument("Nu exista obiecte de arta in expozitie!");
    }
    for (int i = 0; i < statistica.size() - 1; i++) {
        for (int j = i + 1; j < statistica.size(); j++) {
            if (statistica[i].voturi < statistica[j].voturi) {
                swap(statistica[i], statistica[j]);
            }
        }
    }

    return statistica;
}

int Service::calcNr(string categorie, string artist) {
    vector <ObiectArta> obiecte = this->elemRepo.getAll();
    vector <ObiectArta> obiecteFiltrate;

    for (int i = 0; i < obiecte.size(); i++) {
        if (obiecte[i].getCategorie() == categorie && obiecte[i].getAutor() == artist) {
            obiecteFiltrate.push_back(obiecte[i]);
        }
    }

    if (obiecteFiltrate.size() == 0) {
        throw invalid_argument("NU exista obiecte cu artistul dat in categoria data!");
    }
    else
        return obiecteFiltrate.size();

}

int Service::getSize() {
    return this->elemRepo.getSize();
}



