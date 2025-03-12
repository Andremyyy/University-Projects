//
// Created by ema_a on 6/2/2024.
//

#ifndef MODEL_BIBLIOTECA_SERVICE_H
#define MODEL_BIBLIOTECA_SERVICE_H


#include "Repo.h"
#include "Carte.h"
#include "vector"
#include "FileRepo.h"
using namespace std;



class Service {
private:
    Repo<Carte> repo;
public:
    Service(Repo<Carte> repo ) {
        this->repo = repo;
    }

    ~Service() = default;

    // Functia adauga o carte in repo
    // autor, nume - string
    // an, bucati - int
    // return: nimic
    // arunca exceptie daca exista deja cartea in biblioteca

    void addCarte(string nume, int an, string autor, int bucati);

    // Functia sterge din biblioteca o carte
    // autor, nume - string
    // an, bucati - int
    // nu returneaza nimic
    // arunca exceptie daca nu exista cartea in biblioteca

    void deleteCarte(string nume, int an, string autor, int bucati);

    // Functia modifica o carte din biblioteca
    // autor, nume - string
    // an, bucati - int
    // carteNoua - Carte
    // nu returneaza nimic
    // arunca exceptie daca nu exista cartea in biblioteca

    void updateCarte(string nume, int an, string autor, int bucati, Carte& carteNoua);

    // Functia returneaza toate cartile din biblioteca
    // nu primeste nimic
    // returneaza vector de string

    vector<Carte> afiseazaCarti();

    // Functia returneaza toate cartile din biblioteca sortate crescatoar dupa nume, si daca sunt egale dpdv al numelui, descrescator dupa autor
    // nu primeste nimic
    // returneaza vector de string

    vector <Carte> sortNumeAutor();

    // Functia returneaza cartile care sunt conform cerintei explicate mai incolo si sterge cartile din biblioteca care nu au anul mai mare decat cel dat si numarul de bucati mai mic sau egal decat cel dat
    // ant, bucati - int
    // returneaza vector de string

    vector<Carte> filtrareCarti(int ant, int bucati);

};


#endif //MODEL_BIBLIOTECA_SERVICE_H
