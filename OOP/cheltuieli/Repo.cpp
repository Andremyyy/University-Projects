//
// Created by ema_a on 4/8/2024.
//

#include "Repo.h"

Repo::Repo() {
    this -> size = 0;
}

Repo::~Repo(){

}

Cheltuieli Repo::getElem(int pozitie) {
    return elems[pozitie];
}

void Repo::addElem(Cheltuieli &c) {
    if (size < MAX_SIZE)

        this -> elems[this->size++] = c;
    else{
        //throw exception
    }
}

vector <Cheltuieli> Repo::getAll() {
    vector <Cheltuieli> allElements;
    for ( int i = 0; i < size; i++)
        allElements.push_back(elems[i]);
    return allElements;
}

int Repo:: dim(){
    return this -> size;
}

Repo::Repo(int size, Repo * r) {
    this->size = size;
    for ( int i = 0; i < r->size; i++ )
        this -> elems[i] = r->elems[i];
}

Repo::Repo(Repo &r) {
    this -> size = r.size;
    for ( int i = 0; i < r.size; i++ )
        this -> elems[i] = r.elems[i];
}

void Repo::deleteElem(int i) {
    if ( i >= 0 && i < size) {
        for (int j = i; j < size - 1; j++)
            elems[j] = elems[j + 1];
        size--;
    }
}

void Repo::updateElem(int poz, Cheltuieli c) {
    if ( poz >= 0 && poz < size)
        elems[poz] = c;
}




