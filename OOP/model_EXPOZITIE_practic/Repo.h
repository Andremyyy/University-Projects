//
// Created by ema_a on 5/29/2024.
//

#ifndef MODEL_EXPOZITIE_PRACTIC_REPO_H
#define MODEL_EXPOZITIE_PRACTIC_REPO_H


#include <vector>
#include <algorithm>
#include "ObiectArta.h"
using namespace std;

template <typename T>

class Repo {
private:
    vector<T> elems;
public:
    Repo() = default;
    ~Repo() = default;

    void addElem(T& elem){
        elems.push_back(elem);
    }
    void deleteElem(T& elem){
        typename ::vector<T>:: iterator it;
        it = find(elems.begin(), elems.end(), elem);
        if (it != elems.end()) {
            elems.erase(it);
        }
    }
    // Actualizarea unui element
    void updateElem( T& elem,  T& newElem) { // Parametri const
        int index = findElem(elem); // Căutăm indexul elementului de actualizat
        if (index == -1) {
            cout<< "Elementul nu a fost găsit pentru actualizare." << endl;
            return;// Gestionare a erorii
        }
        elems[index] = newElem; // Actualizăm elementul
    }
    vector<T> getAll(){
        return elems;
    }
    int getSize(){
        return elems.size();
    }
    int findElem(T& elem){
        for (int i = 0; i < elems.size(); i++) {
            if ((elems[i]) == elem) {
                return i;
            }
        }
        return -1;
    }



    ObiectArta elemAtPos(int poz) {
        return this->elems[poz];
    }

    // Operator de egalitate
    bool operator==(const Repo& other) const {
        return elems == other.elems; // compară listele de elemente
    }

    // Functia insereaza pe pozitia p valida un element de tip T
    // poz - int
    // elem - T
    // nu returneaza nimic
    void insertPoz(int poz, T& elem) {
        elems.insert(elems.begin() + poz, elem);
    }


};


#endif //MODEL_EXPOZITIE_PRACTIC_REPO_H
