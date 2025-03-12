//
// Created by ema_a on 6/1/2024.
//

#ifndef MODEL_ACTIVITATI_GREVA_SERVICWE_H
#define MODEL_ACTIVITATI_GREVA_SERVICWE_H


#include "Repo.h"
#include "Profesor.h"
#include "vector"
using namespace std;



class Service {
private:
    Repo<Profesor> elemRepo;
public:
    Service(Repo<Profesor> bacterii);
    ~Service() = default;

    // Funcgtia calculeaza numarul de profesori care sunt in greva
    // nu primeste nimic
    // return:int
    // arunca exceptie daca nu exista profesori in baza de date

    int calcNrProfesoriGreva();

    // Functia returneaza un vector care contine disciplina/disciplinele unde sunt cei mai multi profesori in greva
    // nu primeste nimic
    // returneaza un vector de string
    // arunca exceptie daca nu exista profesori in baza de date

    vector<string >calcDisciplinaMaxGreva();

    // Functia determina clasa cu cei mai multi profesori in greva
    // nu primeste nimic
    // returneaza un string
    // arunca exceptie daca nu exista profesori in baza de date

    string calcClasaMaxGreva();

    // Functia returneaza disciplinele care se pot preda de profesorii care nu sunt in greva
    // un vector care contine disciplinele din ziua curenta pt o anumita clasa
    // returneaza vector de string
    // arunca exceptie daca nu se poate preda nicio disciplina
    // arunca exceptie daca nu exista profesori in baza de date

    vector<string> calcDisciplineValabile(string clasa, string orar[], int nr);


    ////in plus

    void addProfesor(string nume, string disciplina, vector<string> clase, bool inGreva);

    vector<Profesor> afiseazaProfesori();

};


#endif //MODEL_ACTIVITATI_GREVA_SERVICWE_H
