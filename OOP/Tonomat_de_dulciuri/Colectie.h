//
// Created by ema_a on 4/21/2024.
//

#ifndef ATM_LAB2_COLECTIE_H
#define ATM_LAB2_COLECTIE_H

#include "VectorDinamic.h"
#include "Pereche.h"
#include "MyException.h"

class Colectie {
private:
    VectorDinamic<Pereche> elements;

public:
    // Constructor implicit
    Colectie(int capacity = 1000) : elements(capacity) {}

    // Constructor de copiere
    Colectie(const Colectie& other) : elements(other.elements) {}


    // Operator de atribuire
    Colectie& operator=(const Colectie& other) {
        if (this != &other) { // Verificăm că nu atribuiți același obiect
            elements = other.elements;
        }
        return *this;
    }

    // Operatorul de egalitate
    bool operator==(const Colectie& other) const {
        if (this->elements.getSize() != other.elements.getSize()) {
            return false; // Dacă dimensiunile sunt diferite, nu sunt egale
        }

        for (int i = 0; i < this->elements.getSize(); i++) {
            Pereche p1 = this->elements.getAt(i);
            Pereche p2 = other.elements.getAt(i);

            if (p1.element != p2.element || p1.frecventa != p2.frecventa) {
                return false; // Dacă oricare dintre perechi este diferit, colecțiile nu sunt egale
            }
        }

        return true; // Dacă toate perechile sunt egale, colecțiile sunt egale
    }

    // Setteri
    void setElementAt(int index, const Pereche& p) {
        if (index < 0 || index >= elements.getSize()) {
            throw MyException("Index invalid");
        }
        elements.getAt(index) = p;
    }

    void setCollection(const VectorDinamic<Pereche>& elements_nou) {
        this->elements = elements_nou;
    }

    // Adăugare element în colecție
    void add(Pereche pereche){
        for (int i = 0; i < elements.getSize(); i++) {
            if (elements.getAt(i).element == pereche.element) {
                elements.getAt(i).frecventa += pereche.frecventa;
                return;
            }
        }

        elements.push_back(pereche);
    }

    // Șterge un element din colecție (după valoare)
    bool remove(TElem elem){
        int index = -1;

        // Găsește indexul elementului de șters
        for (int i = 0; i < elements.getSize(); i++) {
            if (elements.getAt(i).element == elem) {
                index = i;
                break;
            }
        }

        if (index == -1) {
//            throw invalid_argument("Position invalid");
            return false; // Elementul nu a fost găsit
        }

        if (elements.getAt(index).frecventa > 1) {
            elements.getAt(index).frecventa--;  // Decrementează frecvența
            return true;
        } else {
            // Mută elementele pentru a umple spațiul gol
            for (int i = index; i < elements.getSize() - 1; i++) {
                elements.getAt(i) = elements.getAt(i + 1);
            }

            elements.sterge(elements.getSize() - 1);  // Șterge ultimul element
            return true;
        }
    }

    // Căutare element
    bool search(TElem elem) {
        for (int i = 0; i < elements.getSize(); i++) {
            if (elements.getAt(i).element == elem) {
                return true;
            }
        }
        return false;
    }

    // Obține numărul de elemente distincte
    int getSize() {
        return elements.getSize(); // Number of distinct elements
    };

    // Obține o listă de elemente (ca vector dinamic)
    VectorDinamic<Pereche> getElements() const {
        return elements; // Returnează întregul vector dinamic de elemente
    }

    // Obține frecvența unei anumite valori
    int getFrecventa(TElem valoare) const {
        for (int i = 0; i < elements.getSize(); i++) {
            if (elements.getAt(i).element == valoare) {
                return elements.getAt(i).frecventa;
            }
        }
        return 0;
    }


    // Obține elementul de la o anumită poziție (numai pentru testare sau verificare)
    Pereche getAt(int position) const{
        if (position < 0 || position >= elements.getSize()) {
            throw MyException("Pozitie invalida");
        }
        return elements.getAt(position);
    }

    // Destructor - eliberează resursele
    ~Colectie() {

//        if (elements.getSize() > 0) {
//            elements = VectorDinamic<Pereche>(1000); // Reset to initial capacity
//        }
    }


    // Numără de câte ori apare un element
    int nroccurrences(TElem elem) const {
        for (int i = 0; i < elements.getSize(); i++) {
            if (elements.getAt(i).element == elem) {
                return elements.getAt(i).frecventa;
            }
        }
        return 0;
    };

    // Funcție pentru actualizarea colecției cu bancnote utilizate
    // Funcție pentru a scădea numărul de bancnote
    void scade_bancnote(int valoare, int cantitate) {
        bool found = false; // Flag pentru a verifica dacă am găsit valoarea
        for (int i = 0; i < elements.getSize(); i++) {
            Pereche& b = elements.getAt(i); // Explicit Pereche&
            if (b.element == valoare) {
                if (b.frecventa < cantitate) {
                    throw MyException("Nu sunt suficiente bancnote."); // Excepție dacă frecvența este prea mică
                }
                b.frecventa -= cantitate; // Scade frecvența
                found = true; // Indică faptul că am găsit bancnota
                break;
            }
        }
        if (!found) {
            throw MyException("Bancnota nu a fost găsită."); // Excepție dacă bancnota nu este găsită
        }
    }

};


#endif //ATM_LAB2_COLECTIE_H
