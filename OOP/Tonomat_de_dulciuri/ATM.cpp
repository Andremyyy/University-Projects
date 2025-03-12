//
// Created by ema_a on 4/29/2024.
//

#include "ATM.h"
#include "Tranzactie.h"
#include "MyException.h"


bool ATM::confirmare_tranzactie(int idTranzactie, int suma, int cod, string nume, int pret) {
    // Verificăm dacă suma introdusă este suficientă pentru a cumpăra produsul
    if (suma < pret) {
        throw MyException("Suma introdusa este insuficienta pentru a cumpara produsul.");
    }

    int suma_ramas = suma - pret; // Restul care trebuie dat
    Colectie detalii_bancnote; // Bancnotele folosite pentru a da restul

    // Calculul bancnotelor pentru rest
    for (int i = 0; i < bancnote_disponibile.getSize() && suma_ramas > 0; i++) {
        Pereche bancnota = bancnote_disponibile.getAt(i);
        int valoare = bancnota.element;
        int număr_disponibil = bancnota.frecventa;

        int număr_folosite = min(suma_ramas / valoare, număr_disponibil); // Bancnotele necesare pentru rest

        if (număr_folosite > 0) {
            detalii_bancnote.add(Pereche(valoare, număr_folosite));
            suma_ramas -= număr_folosite * valoare; // Actualizăm restul
        }
    }

    if (suma_ramas > 0) { // Dacă nu putem da restul cu bancnotele disponibile
        throw MyException("Nu sunt suficiente bancnote pentru rest.");
    }

    // Actualizarea bancnotelor disponibile cu cele folosite pentru rest
    for (int i = 0; i < detalii_bancnote.getSize(); i++) {
        Pereche b = detalii_bancnote.getAt(i);
        bancnote_disponibile.scade_bancnote(b.element, b.frecventa); // Reducem frecvența bancnotelor folosite
    }

    // Afișăm restul dat și noua frecvență a bancnotelor disponibile
    cout << "Restul dat este: " << suma - pret << "\n" << endl; // Afișăm restul final
    cout << "Bancnotele disponibile dupa tranzactie:\n";
    for (int i = 0; i < bancnote_disponibile.getSize(); i++) {
        Pereche p = bancnote_disponibile.getAt(i);
        cout << "Valoare: " << p.element << ", Frecventa: " << p.frecventa << "\n"; // Afișăm frecvența actualizată
    }

    cout << endl << endl;
    return true; // Tranzacția a fost confirmată cu succes
}

// Metode pentru a adăuga sau actualiza bancnotele disponibile
void ATM::adauga_bancnote(const Pereche& p) {
    bancnote_disponibile.add(p);
}

void ATM::elimina_bancnote(int valoare, int numar) {
    for (int i = 0; i < numar; i++) {
        bancnote_disponibile.remove(valoare);
    }
}

// Obține colecția actuală de bancnote disponibile
Colectie ATM::getBancnoteDisponibile() const {
    return bancnote_disponibile;
}

ATM::~ATM() {

}

// Setter pentru colecția de bancnote disponibile
void ATM:: setBancnoteDisponibile(const Colectie& noi_bancnote) {
    bancnote_disponibile = noi_bancnote;
}
