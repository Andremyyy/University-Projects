//
// Created by ema_a on 4/8/2024.
//

#ifndef GESTIUNE_APARTAMENTE_REPO_H
#define GESTIUNE_APARTAMENTE_REPO_H

#include "Cheltuieli.h"
#include <vector>
using namespace std;

class Repo {
private:
    static const int MAX_SIZE = 1000; // Dimensiunea maximă a repo-ului
    int size;
    Cheltuieli elems[MAX_SIZE]; // Tabloul de cheltuieli
public:
    Repo();
    Repo(int, Repo []);
    Repo(Repo&r);
    void addElem(Cheltuieli &c);
    vector <Cheltuieli> getAll();
    void deleteElem(int i);
    void updateElem(int, Cheltuieli);
    int dim();
    Cheltuieli getElem(int poz);
    ~Repo();

    Repo& operator=(const Repo&r){
        this -> size = r.size;
        for ( int i = 0; i < r.size; i++ )
            this -> elems[i] = r.elems[i];
        return *this;
    }

};


#endif //GESTIUNE_APARTAMENTE_REPO_H
