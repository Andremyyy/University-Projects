//
// Created by Asus on 4/23/2024.
//

#ifndef TONOMAT_DE_DULCIURI_DULCIURI_H
#define TONOMAT_DE_DULCIURI_DULCIURI_H

#include <iostream>
#include <string>
#include <cstring>
#include <ostream>
using namespace std;

class Dulciuri {
private:
    static int next_cod; // Membre static pentru următorul cod disponibil
    int cod;
    string nume;
    int pret;
public:
    Dulciuri();
    Dulciuri(string, int);
    Dulciuri(const Dulciuri &other);

    // Constructor cu cod specificat (pentru utilizare manuală)
    Dulciuri(int cod, string nume, int pret);

    ~Dulciuri();

    int getCod();
    string getNume();
    int getPret();


    void setCod(int cod);
    void setNume(string);
    void setPret(int);


    // Suprascrierea operatorului ==

    bool operator == (const Dulciuri& other) const {
        return cod == other.cod && pret == other.pret && nume == other.nume ;
    }



    //Suprascrierea operatorului =

    Dulciuri operator = (const Dulciuri &c) {
        cod = c.cod;
        pret = c.pret;
        nume = c.nume;

        return *this;
    }

    //suprascrierea operatorului <<
    friend ostream &operator<<(ostream &output, Dulciuri &other);

};

std::ostream &operator<<(std::ostream &output, Dulciuri &other);


#endif //TONOMAT_DE_DULCIURI_DULCIURI_H
