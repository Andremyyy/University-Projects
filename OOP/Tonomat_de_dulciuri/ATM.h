//
// Created by ema_a on 4/21/2024.
//

#ifndef ATM_LAB2_ATM_H
#define ATM_LAB2_ATM_H

#include "Colectie.h"
#include "Tranzactie.h"
#include <iostream>
#include "RepoDulciuri.h"
#include "Service.h"
using namespace std;

class ATM {

private:
    Colectie bancnote_disponibile;
    Service service;

public:

    // Constructor pentru inițializarea bancomatului cu bancnote
    ATM(const Colectie& bancnote, const Service &service)
            : bancnote_disponibile(bancnote), service(service) {
    }

    // Constructor de copiere
    ATM(const ATM& other, const Service &service) : bancnote_disponibile(other.bancnote_disponibile), service(service) {}

    // Operator de atribuire
    ATM& operator=(const ATM& other) {
        if (this != &other) {
            bancnote_disponibile = other.bancnote_disponibile;
            service = other.service;
        }
        return *this;
    }

    // Operator de egalitate
    bool operator==(const ATM& other) const {
        return bancnote_disponibile == other.bancnote_disponibile && service == other.service;
    }


    // Destructor pentru eliberarea resurselor
    ~ATM();

    // Confirmare a tranzacției
    bool confirmare_tranzactie(int idTranzactie, int suma, int cod, string nume, int pret);

    // Metode pentru a adăuga sau actualiza bancnotele disponibile
    void adauga_bancnote(const Pereche& p);

    void elimina_bancnote(int valoare, int numar);

    // Obține colecția actuală de bancnote disponibile
    Colectie getBancnoteDisponibile() const;

    // Setter pentru colecția de bancnote disponibile
    void setBancnoteDisponibile(const Colectie& noi_bancnote);

};


#endif //ATM_LAB2_ATM_H
