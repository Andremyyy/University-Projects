//
// Created by ema_a on 6/3/2024.
//

#ifndef PRACTIC_SERVICE_H
#define PRACTIC_SERVICE_H


#include "Manuscris.h"
#include "Repo.h"

class Service {
private:

    Repo<Manuscris> repo;
public:

    Service(Repo<Manuscris> repo ) {
        this->repo = repo;
    }

    ~Service() = default;



    // Functia adauga UN manuscris in biblioteca
    // nume, autor - string
    // nrPagini, an - int
    // return: nimic
    // arunca exceptie daca exista deja OBIECTUL in REPO


    void addManuscris(string nume, int an, string autor, int nrPagini);

    // Functia sterge din REPO UN manuscris
    // nume, autor - string
    // nrPagini, an - int
    // return: nimic
    // arunca exceptie daca nu exista deja OBIECTUL in REPO


    void deleteManuscris(string nume, int an, string autor, int nrPagini);

    // Functia modifica UN manuscris din biblioteca
    // nu primeste nimic
    // nu returneaza nimic
    // arunca exceptie daca nu exista OBIECTUL in REPO

     void updateManuscris();

    // Functia modifica manuscrisele cu peste 200 de oagini, modifcandu-le numele si nr pagini
    // nu primeste nimic
    // nu returneaza nimic
    // arunca eroare daca nu exista manuscrise cu peste 200 de pagini
     void updateVolume();


    // Functia returneaza toate OBIECTELE din REPO
    // nu primeste nimic
    // returneaza vector de string

     vector<Manuscris> afiseazaManuscrise();

     // Functia returneaza toate manuscrisele cu mai putin de 50 de pagini
        // nu primeste nimic
        // returneaza vector de string
     vector<Manuscris> afiseazaLessThan50Pag();




};

#endif //PRACTIC_SERVICE_H
