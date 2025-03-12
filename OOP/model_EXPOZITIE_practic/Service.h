//
// Created by ema_a on 5/29/2024.
//

#ifndef MODEL_EXPOZITIE_PRACTIC_SERVICE_H
#define MODEL_EXPOZITIE_PRACTIC_SERVICE_H


#include "Repo.h"
#include "ObiectArta.h"
#include "vector"
using namespace std;

struct StatisticaEntry {
    string categorie;
    int voturi;
};

class Service {
private:
    Repo<ObiectArta> elemRepo;
public:
    Service(Repo<ObiectArta> bacterii);
    ~Service() = default;

    // Funcgtia insereaza pe pozitie poz, un obiect de arta cu autor, denumire, categorie si voturi
    // categorie, denumire, autor - string
    // voturi - int
    // nu returneaza nimic
    // arunca exceptie daca poz nu este valid sau daca exista deja un obiect de arta cu aceleasi atribute
    void insertPoz(int pozitie, string autor, string denumire,string categorie, int voturi);

    // Functia returneaza un vector de StatisticaEntry care contine pentru fiecare categorie numarul total de voturi
    // nu primeste nimic
    // returneaza un vector de StatisticaEntry
    // arunca exceptie daca nu exista obiecte de arta in expozitie
    vector<StatisticaEntry> getStatistica();

    // Functia calculeaza numarul de obiecte de arta care au categoria data si autorul dat
    // categorie, autor - string
    // returneaza un int
    // arunca exceptie daca nu exista obiecte de categoria si autorul date
    int calcNr(string categorie,string artist);

    // Functia returneaza numarul de obiecte de arta din expozitie
    // nu primeste nimic
    // returneaza un int
    int getSize();

};

#endif //MODEL_EXPOZITIE_PRACTIC_SERVICE_H
