//
// Created by ema_a on 4/29/2024.
//

#include "Tranzactie.h"
#include <algorithm>
using namespace std;

// Funcție pentru calculul bancnotelor necesare pentru a plăti suma
void Tranzactie:: calculeaza_bancnote(Colectie& bancnote_disponibile) {
    int suma_ramas = suma;

    for (int i = 0; i < bancnote_disponibile.getSize() && suma_ramas > 0; i++) {
        Pereche bancnota = bancnote_disponibile.getAt(i);
        int valoare = bancnota.element;
        int numar_disponibil = bancnota.frecventa;

//        if (suma_ramas <= 0) {
//            break;
//        }

        int numar_folosite = min(suma_ramas / valoare, numar_disponibil);
        if (numar_folosite > 0) {
            detalii_bancnote.add(Pereche(valoare, numar_folosite));
            suma_ramas -= numar_folosite * valoare;
        }
    }

    if (suma_ramas > 0)
        throw invalid_argument("Nu sunt suficiente bancnote pentru a plati suma ceruta.");

}

// Metode de accesare
int Tranzactie::getId() const {
    return idTranzactie;
}

int Tranzactie::getSuma() const {
    return suma;
}

Colectie Tranzactie:: getDetaliiBancnote() const {
    return detalii_bancnote;
}


// Setteri
void Tranzactie::setId(int id) {
    this->idTranzactie = id;
}

void Tranzactie::setSuma(int suma_noua) {
    this->suma = suma_noua;
}

void Tranzactie::setDetaliiBancnote(const Colectie& noi_bancnote) {
    this->detalii_bancnote = noi_bancnote;
}