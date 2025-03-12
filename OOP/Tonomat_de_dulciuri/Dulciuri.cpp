//
// Created by Asus on 4/23/2024.
//

#include "Dulciuri.h"

// Inițializarea variabilei statice pentru următorul cod disponibil
int Dulciuri::next_cod = 1; // Pornim cu codul 1 și incrementăm la fiecare instanțiere

Dulciuri::Dulciuri() {
    this ->cod = next_cod++;
    this ->nume = "";
    this ->pret = -1;
}

// Constructor cu cod specificat (pentru utilizare manuală)
Dulciuri:: Dulciuri(int cod, string nume, int pret) {
    this ->cod = cod;
    this ->nume = nume;
    this -> pret = pret;
}

Dulciuri::Dulciuri( string nume, int pret) {
    this -> cod = next_cod++;
    this -> pret = pret;
    this -> nume = nume;
}

Dulciuri::Dulciuri(const Dulciuri &other) {
    this -> cod = other.cod;
    this ->pret = other.pret;
    this -> nume = other.nume;
}

Dulciuri::~Dulciuri() {
}

int Dulciuri::getCod() {
    return this -> cod;
}

string Dulciuri::getNume() {
    return this -> nume;
}

int Dulciuri::getPret() {
    return this -> pret;
}


void Dulciuri::setNume(string nume) {
    this -> nume = nume;
}

void Dulciuri::setPret(int pret) {
    this -> pret = pret;
}

ostream &operator<<(ostream &output, Dulciuri &other) {
    output << other.cod << " " << other.nume << " " << other.pret;
    return output;
}

void Dulciuri::setCod(int cod) {
    this -> cod = cod;
}



