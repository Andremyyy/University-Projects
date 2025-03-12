//
// Created by ema_a on 6/1/2024.
//

#ifndef MODEL_ACTIVITATI_GREVA_REPO_H
#define MODEL_ACTIVITATI_GREVA_REPO_H


#include <vector>
#include <algorithm>
#include "Profesor.h"
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



    Profesor elemAtPos(int poz) {
        return this->elems[poz];
    }

    // Operator de egalitate
    bool operator==(const Repo& other) const {
        return elems == other.elems; // compară listele de elemente
    }



};


#endif //MODEL_ACTIVITATI_GREVA_REPO_H
