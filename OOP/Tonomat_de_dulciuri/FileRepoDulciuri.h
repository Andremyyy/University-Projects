//
// Created by ema_a on 5/11/2024.
//

#ifndef TONOMAT_DE_DULCIURI_FILEREPODULCIURI_H
#define TONOMAT_DE_DULCIURI_FILEREPODULCIURI_H

#include "RepoDulciuri.h"
#include <fstream>
using namespace std;
#include "Dulciuri.h"

template <typename T>

class FileRepoDulciuri : public RepoDulciuri<T> {
private:
    char *fileName;
public:
    FileRepoDulciuri (const char *);
    void saveToFile();

    ~FileRepoDulciuri();
};

template<typename T>
FileRepoDulciuri<T>::FileRepoDulciuri(const char* file) : RepoDulciuri<T>() {
    fileName = new char[strlen(file) + 1]; // Alocare memorie pentru fileName
    strcpy(fileName, file); // Copierea numelui fișierului

    ifstream f(fileName);
    if (!f.is_open()) {
        // Dacă fișierul nu poate fi deschis, afișăm un mesaj de eroare și ieșim
        cerr << "Eroare: Nu s-a putut deschide fisierul: " << fileName << endl;
        delete[] fileName; // Eliberăm memoria alocată pentru fileName
        return;
    }

    int nr, pret;
    char nume[15]; // Nu mai este nevoie de alocare dinamică
    while (f >> nr >> nume >> pret) {
        Dulciuri dulce(nr, nume, pret);
        this -> addElem(dulce);
    }

    f.close();
}

template <typename T>
void FileRepoDulciuri<T>::saveToFile() {
    ofstream fout(fileName);
    if (!fout.is_open()) {
    // Dacă fișierul nu poate fi deschis, afișăm un mesaj de eroare și ieșim
    cerr << "Eroare: Nu s-a putut deschide fisierul: " << fileName << endl;
    return;
    }

    for (int i = 0; i < this -> getSize(); i++) {
        fout << this -> elemAtPos(i); // Folosim suprascrierea operatorului de afișare <<
        fout << endl;
    }

    fout.close();
}

template <typename T>
FileRepoDulciuri<T>::~FileRepoDulciuri() {
    delete[] fileName; // Eliberăm memoria alocată pentru fileName
}


#endif //TONOMAT_DE_DULCIURI_FILEREPODULCIURI_H
