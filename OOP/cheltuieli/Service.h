//
// Created by ema_a on 4/19/2024.
//

#ifndef GESTIUNE_APARTAMENTE_SERVICE_H
#define GESTIUNE_APARTAMENTE_SERVICE_H

#include "Repo.h"
#include <vector>
#include <stack>
using namespace std;

struct Operation {
    string type;  // "add", "delete", "update"
    vector<Cheltuieli> deleted;
    Cheltuieli previous;  // Cheltuiala inițială pentru "update" și "delete"
    Cheltuieli current;   // Cheltuiala finală pentru "add" și "update"
    int index;  // Indexul pentru operațiunile care necesită poziție specifică
};


class Service {

private:
    Repo r;
    stack<Operation> history;  // Stiva pentru istoria operațiilor
public:

    //constructor implicit:
    Service();

    //deconstructor:
    ~Service();

    //determina ziua actuala
    static int today();

    //returneaza obiectul Cheltuiala de pe pozitia pozitie
    Cheltuieli getElem(int pozitie);

    //adauga un  obiect Cheltuiala cu ziua actuala (foflosind functia today), suma si tipul date
    void addElem(int suma, char *tip);

    //insereaza la sfarsit un obiect Cheltuiala cu ziua, suma si tipul date
    void insertElem(int zi, int suma, char *tip);

    // sterge  obiectul Cheltuiala cu ziua, suma si tipul date si returneaza True daca s-a efectuat stergerea, iar False altfel(nu exosta obiectul Cheltuiala cu datele date)
    bool deleteElem(int zi, int suma, char * tip);

    // modifica  obiectul Cheltuiala cu ziua, suma, tipul date in  obiectul Cheltuiala cu ziua_noua, suma_noua, tipul_nou date si returneaza True daca s-a efectuat modificarea, iar False altfel(nu exosta obiectul Cheltuiala cu datele date)
    bool updateElem(int zi, int suma, char *tip, int zi_noua, int suma_noua, char * tip_nou);

    // retuneaza vectorul cu toate cheltuielile
    vector <Cheltuieli> getAll();

    //returneaza marimea vectorului care contine toate cheltuielile
    int getsize();

    // sterge  obiectele Cheltuiala din ziua data si returneaza numarul de stergeri efectuate
    int deleteCheltZi(int zi);

    // sterge  obiectele Cheltuiala din intervalul inchis dat si returneaza numarul de stergeri efectuate
    int deleteCheltInterval(int zi1, int zi2);

    // sterge  obiectele Cheltuiala de tipul dat si returneaza numarul de stergeri efectuate
    int deleteCheltTip(char * tip);

    //returneaza marimea vectorului care contine toate cheltuielile de tipul dat
    int getSizeTip(char *tip);

    // retuneaza vectorul cu toate cheltuielile de tipul dat
    vector <Cheltuieli> getAllTip(char * tip);

    //returneaza marimea vectorului care contine toate cheltuielile de tipul dat cu suma strict mai mare decat suma data
    int getSizeTipBiggerThanSuma( char * tip, int suma);

    // retuneaza vectorul care contine toate cheltuielile de tipul dat cu suma strict mai mare decat suma data
    vector <Cheltuieli> getAllTipBiggerThanSuma(char *tip,int suma);

    //returneaza marimea vectorului care contine toate cheltuielile de tipul dat care au suma egala cu suma data
    int getSizeTipEqualSuma( char * tip, int suma);

    //returneaza vectorului care contine toate cheltuielile de tipul dat care au suma egala cu suma data
    vector <Cheltuieli> getAllTipEqualSuma(char *tip,int suma);

    // returneaza suma cheltuilelilor de tipul dat
    int detSumaTip(char * tip);

    // determina ziua in care s-au efectuat cele mai multe cheltuieli in functie de suma cheltuita
    int detZiMaxSuma();

    //returneaza marimea vectorului care contine toate cheltuielile din ziua data
    int getSizeZi(int zi);

    // returneaza un vector care contine toate sumele cheltuile in ziua data ordonate descrescator
    void getAllZiDescr(int zi, int solutie[1000]);

    //returneaza un vector care contine toate sumele cheltuile de tipul dat ordonate crescator
    void getAllTipCresc(char * tip, int solutie[1000], int &lung);

    //returneaza marimea vectorului care contine toate cheltuielile din ziua data de tipul dat
    int getSizeTipZi(char *tip, int zi);

    //returneaza un vector care contine toate sumele cheltuile de tipul dat in ziua data ordonate crescator
    void getAllTipZiCresc(char *tip, int zi, int solutie[1000]);

    //returneaza marimea vectorului care contine toate cheltuielile de tipul dat cu suma mai mica strict decat suma data
    int getSizeTipLessThanSuma(char *tip, int suma);

    //returneaza un vector care contine toate cheltuielile de tipul dat cu suma mai mica strict decat suma data
    vector <Cheltuieli> getAllTipLessThanSuma (char *tip, int suma);


    //returneaza True daca s-a facut undo, altfel False
    bool undo();


//    friend ostream &operator<<(ostream &output, Service & service);


};

//ostream& operator<<(ostream& output, Service& service);


#endif //GESTIUNE_APARTAMENTE_SERVICE_H
