//
// Created by Asus on 4/23/2024.
//

#include "Service.h"

Service::Service(RepoDulciuri<Dulciuri> repo) : elemRepo(repo) {
    // Constructorul trebuie să initializeze elemRepo
}


void Service::add(string nume, int pret) {
    Dulciuri dulce(nume, pret);
    elemRepo.addElem(dulce);
}

void Service::remove(int cod, string nume, int pret) {
    Dulciuri dulce(cod, nume, pret); // Căutăm după cod
    int index = elemRepo.findElem(dulce);
    if (index == -1) {
        throw MyException("Nu există dulcele dat");
    }
    elemRepo.deleteElem(dulce);
}


void Service::update(int cod, string nume, int pret,  Dulciuri& dulceNou) {
    Dulciuri dulce(cod, nume, pret); // Căutăm după cod
    int index = elemRepo.findElem(dulce);
    if (index == -1) {
        throw MyException("Nu există dulcele dat");
    }
    try {
        elemRepo.updateElem(dulce, dulceNou);
    }
    catch (MyException &myex) {
        throw myex;
    }
}


int Service::find(int cod, string nume, int pret) {
    Dulciuri dulce(cod, nume, pret); // Căutăm după cod
    return elemRepo.findElem(dulce); // Returnează indexul sau -1 dacă nu găsește
}


vector<Dulciuri> Service::getAll() {
    return elemRepo.getAll(); // Returnează toți elementii
}

