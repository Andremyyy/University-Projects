//
// Created by ema_a on 4/292024.
//

#ifndef ATM_LAB2_VECTORDINAMIC_H
#define ATM_LAB2_VECTORDINAMIC_H


#include <stdexcept>
#include "Pereche.h"
using namespace std;
template <typename TElem >


class VectorDinamic{
private:

    int capacity;
    int size;
    TElem* elements;   //vectorul de elemente

    void resize() {
        if (size >= capacity) {
            capacity *= 2;
            TElem *new_elements = new TElem[capacity];
            // copiem vechile elemente în noul vector
            for (int i = 0; i < size; i++) {
                new_elements[i] = elements[i];
            }
            delete[] elements; // eliberăm memoria vechiului vector
            elements = new_elements; // actualizăm pointerul
        }
    }

public:
    /// Constructor cu parametri

    explicit VectorDinamic (int initial_capacity = 1000)
            : capacity(initial_capacity), size(0), elements(new TElem [initial_capacity]) {}

    VectorDinamic<TElem>& operator=(const VectorDinamic<TElem>& other) {
        if (this == &other) { // Verifică auto-atribuirea
            return *this; // Dacă este auto-atribuire, întoarce instanța curentă
        }

        // Eliberează resursele vechi
        if (elements != nullptr) {
            delete[] elements;
        }

        // Setează capacitatea și dimensiunea
        capacity = other.capacity;
        size = other.size;

        // Alocă un nou vector și copiază elementele
        elements = new TElem[capacity];
        for (int i = 0; i < size; ++i) {
            elements[i] = other.elements[i];
        }

        return *this; // Returnează instanța curentă pentru a permite atribuirea în lanț
    }

    bool operator==(const VectorDinamic<TElem>& other) const {
        if (this->size != other.size) { // Verifică dimensiunea
            return false; // Dacă dimensiunile sunt diferite, nu sunt egale
        }

        // Compară elementele unul câte unul
        for (int i = 0; i < this->size; ++i) {
            if (this->elements[i] != other.elements[i]) { // Dacă un element este diferit
                return false; // Vectorii nu sunt egali
            }
        }

        return true; // Dacă toate elementele sunt la fel, vectorii sunt egali
    }

    int getSize() const{
        return size;
    }

    TElem & getAt(int index) const {
        if (index < 0 || index >= size) {
            throw out_of_range("Index invalid");
        }
        return elements[index];
    }

    // Functie pentru actualizarea unui element la un index specificat
    TElem update(int i, TElem e) {
        if (i < 0 || i >= size) {
            throw out_of_range("Index invalid");
        }
        TElem old_value = elements[i];  // păstrăm valoarea veche pentru returnare
        elements[i] = e;  // actualizăm cu noua valoare
        return old_value;  // returnăm valoarea veche
    }

    void push_back(const TElem & element) {
        if (size >= capacity)
            resize();
        elements[size++] = element;
    }

    // Adăugare la un index specificat
    void addAt(int index, const TElem& e) {
        if (index < 0 || index > size) {  // Indexul poate fi la sfârșit pentru a adăuga
            throw out_of_range("Index invalid");
        }

        if (size >= capacity) {  // Asigurarea că există suficient spațiu
            resize();
        }

        // Mutarea elementelor existente pentru a face loc noului element
        for (int i = size; i > index; i--) {
            elements[i] = elements[i - 1];
        }

        elements[index] = e;  // Adăugați noul element
        size++;  // Incrementați dimensiunea
    }

    // Ștergere la un index specificat
    TElem sterge(int index) {
        if (index < 0 || index >= size) {
            throw out_of_range("Index invalid");
        }

        TElem removed_element = elements[index];  // Păstrați elementul eliminat

        // Mutarea elementelor pentru a umple spațiul gol
        for (int i = index; i < size - 1; i++) {
            elements[i] = elements[i + 1];
        }

        size--;  // Decrementați dimensiunea
        return removed_element;  // Returnați elementul șters
    }

    // destructor - dealoca memoria
    ~VectorDinamic(){
//        if (elements != nullptr) { // Asigură-te că nu este nullptr
//            delete[] elements;
//            elements = nullptr; // Setați la nullptr după eliberare
//        }
    }

};


#endif //ATM_LAB2_VECTORDINAMIC_H
