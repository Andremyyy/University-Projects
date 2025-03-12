//
// Created by ema_a on 5/30/2024.
//

#ifndef MODEL_FEDERATIE_SPORTIVA_RESTANTA_SERVICE_H
#define MODEL_FEDERATIE_SPORTIVA_RESTANTA_SERVICE_H



#include "Repo.h"
#include "Meci.h"
#include "vector"
using namespace std;

struct Echipa{
    string nume;
    int punctaj;
    Echipa(string nume, int punctaj) : nume(nume), punctaj(punctaj) {}
    string getNume() const {
        return nume;
    }
    int getPunctaj() const {
        return punctaj;
    }
};

class Service {
private:
    Repo<Meci> elemRepo;
public:
    Service(Repo<Meci> bacterii);
    ~Service() = default;

    // Functia adauga un meci in lista de meciuri
    // echipa1, echipa2 - string
    // golEchipa1, golEchipa2 - int
    // nu returneaza nimic
    // arunca exceptie daca golEchipa1 sau golEchipa2 sunt negative sau echipele sunt identice dpdv lexical
    void addMeci(string echipa1, string echipa2, int golEchipa1, int golEchipa2);

    // Functia returneaza un vector de Echipe care contine pentru fiecare echipa punctajul sau in ordine descrescatoare dupa punctajul obtinut
    // nu primeste nimic
    // returneaza un vector de Echipe
    // arunca exceptie daca nu exista echipe in lista de meciuri
    vector<Echipa> getEchipe();

    // Functia returneaza un vector de Echipe care contine echipele castigatoare din punct de vedere al punctajului
    // nu primeste nimic
    // returneaza un vector de Echipe
    vector<Echipa> getCastigatori();
    // Functia calculeaza numarul de obiecte de arta care au categoria data si autorul dat
    // categorie, autor - string
    // returneaza un int
    // arunca exceptie daca nu exista obiecte de categoria si autorul date



};


#endif //MODEL_FEDERATIE_SPORTIVA_RESTANTA_SERVICE_H
