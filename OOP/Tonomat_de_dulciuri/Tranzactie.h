//
// Created by ema_a on 4/29/2024.
//

#ifndef ATM_LAB2_TRANZACTIE_H
#define ATM_LAB2_TRANZACTIE_H

#include "Colectie.h"
#include "Pereche.h"


class Tranzactie {

private:
    int idTranzactie;
    int suma;
    Colectie detalii_bancnote;

public:

    // Constructor
    Tranzactie(int id, int suma, Colectie& bancnote_disponibile)
            : idTranzactie(id), suma(suma) {
        calculeaza_bancnote(bancnote_disponibile);
    }

    // Funcție pentru calculul bancnotelor necesare pentru a plăti suma
    void calculeaza_bancnote( Colectie& bancnote_disponibile);


    // Metode de accesare
    int getId() const;

    int getSuma() const;

    Colectie getDetaliiBancnote() const;

    // Setteri
    void setId(int id);

    void setSuma(int suma_noua);

    void setDetaliiBancnote(const Colectie& noi_bancnote);

    // Destructor
    ~Tranzactie() = default;

};


#endif //ATM_LAB2_TRANZACTIE_H
