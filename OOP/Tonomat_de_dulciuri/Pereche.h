//
// Created by ema_a on 4/29/2024.
//

#ifndef ATM_LAB2_PERECHE_H
#define ATM_LAB2_PERECHE_H

typedef int TElem;

struct Pereche {
    TElem element; // Elementul de bază
    int frecventa; // Frecvența apariției

    // Constructor implicit care inițializează elementul și frecvența
    Pereche() : element(0), frecventa(0) {}

    // Constructor cu parametri pentru inițializare personalizată
    Pereche(TElem elem, int freq) : element(elem), frecventa(freq) {}

    // Operatorul de comparație `==`
    bool operator==(const Pereche& other) const {
        return this->element == other.element && this->frecventa == other.frecventa;
    }

    // Operatorul de atribuire `=`
    Pereche& operator=(const Pereche& other) {
        if (this != &other) { // Verificăm că nu atribuim același obiect
            this->element = other.element; // Atribuim câmpul `element`
            this->frecventa = other.frecventa; // Atribuim câmpul `frecventa`
        }
        return *this; // Returnăm obiectul curent
    }
};


#endif //ATM_LAB2_PERECHE_H
