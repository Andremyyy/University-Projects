//
// Created by ema_a on 6/2/2024.
//

#include "Service.h"
#include "Carte.h"
#include "vector"
using namespace std;
#include "stdexcept"


void Service::addCarte(string nume, int an, string autor, int bucati) {

    Carte carte(nume, an, autor, bucati);

    if (this->repo.findElem(carte) != -1) {
        throw invalid_argument("Cartea exista deja in biblioteca!");
    }
    this->repo.addElem(carte);

}

void Service::deleteCarte(string nume, int an, string autor, int bucati) {
    bool ok = 0;
    Carte de_sters(nume, an, autor, bucati);
    if (this->repo.findElem(de_sters) == -1) {
        throw invalid_argument("Cartea nu exista in repo!");
    }


    this->repo.deleteElem(de_sters);

}

void Service::updateCarte(string nume, int an, string autor, int bucati, Carte &carteNoua) {
    Carte de_updatat(nume, an, autor, bucati);
    if (this->repo.findElem(de_updatat) == -1) {
        throw invalid_argument("Cartea nu exista in repo!");
    }


    this->repo.updateElem(de_updatat, carteNoua);
}

vector<Carte> Service::afiseazaCarti() {
    return this->repo.getAll();
}

vector<Carte> Service::sortNumeAutor() {
    vector<Carte> carti = this->repo.getAll();
    // sortez cartile crescator dupa nume si daca sunt egale, descrescator dupa autor
    for (int i = 0; i < carti.size() - 1; i++) {
        for (int j = i + 1; j < carti.size(); j++) {
            if (carti[i].getNume() > carti[j].getNume()) {
                Carte aux = carti[i];
                carti[i] = carti[j];
                carti[j] = aux;
            }
            if (carti[i].getNume() == carti[j].getNume() && carti[i].getAutor() < carti[j].getAutor()) {
                Carte aux = carti[i];
                carti[i] = carti[j];
                carti[j] = aux;
            }
        }
    }
    return carti;
}

vector<Carte> Service::filtrareCarti(int ant, int bucati) {
    vector<Carte> carti = this->repo.getAll();
    vector<Carte> cartiFiltrate;
    for (Carte carte: carti) {
        if (carte.getAn() > ant && carte.getBucati() <= bucati) {
            cartiFiltrate.push_back(carte);
        }
        else
            this->repo.deleteElem(carte);
    }
    return cartiFiltrate;
}
