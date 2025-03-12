//
// Created by ema_a on 6/2/2024.
//

#ifndef MODEL_BIBLIOTECA_FILEREPO_H
#define MODEL_BIBLIOTECA_FILEREPO_H


#include "Repo.h"
#include <fstream>
#include <cstring>
using namespace std;
#include "Carte.h"

template <typename T>

class FileRepo : public Repo<T> {
private:
    char *fileName;
public:
    FileRepo (const char *);
    void saveToFile();

    ~FileRepo();
};

template<typename T>
FileRepo<T>::FileRepo(const char* file) : Repo<T>() {
    fileName = new char[strlen(file) + 1]; // Alocare memorie pentru fileName
    strcpy(fileName, file); // Copierea numelui fișierului

    ifstream f(fileName);
    if (!f.is_open()) {
        // Dacă fișierul nu poate fi deschis, afișăm un mesaj de eroare și ieșim
        cerr << "Eroare: Nu s-a putut deschide fisierul: " << fileName << endl;
        delete[] fileName; // Eliberăm memoria alocată pentru fileName
        return;
    }

    string nume, autor;
    int an, bucati;
    while (f >> nume >> an >> autor >> bucati) {
        Carte carte(nume, an, autor, bucati);
        this -> addElem(carte);
    }

    f.close();
}

template <typename T>
void FileRepo<T>::saveToFile() {
    ofstream fout(fileName);
    if (!fout.is_open()) {
        // Dacă fișierul nu poate fi deschis, afișăm un mesaj de eroare și ieșim
        cerr << "Eroare: Nu s-a putut deschide fisierul: " << fileName << endl;
        return;
    }

    for (int i = 0; i < this -> getSize(); i++) {
        fout << this->elemAtPos(i); // Folosim suprascrierea operatorului de afișare <<
        fout << endl;
    }

    fout.close();
}

template <typename T>
FileRepo<T>::~FileRepo() {
    delete[] fileName; // Eliberăm memoria alocată pentru fileName
}


#endif //MODEL_BIBLIOTECA_FILEREPO_H
