//
// Created by ema_a on 4/8/2024.
//

#include "Cheltuieli.h"
#include <iostream>
using namespace std;
#include <cstring>

//constructor implicit
Cheltuieli::Cheltuieli() {
    this->zi = 0;
    this->suma = 0;
    this->tip = nullptr;
}

// constructor general
Cheltuieli::Cheltuieli(int nr, int suma, char *tip) {
    this->zi = nr;
    this->suma = suma;
    this->tip = new char[strlen(tip) + 1];
    strncpy(this->tip, tip, strlen(tip) + 1);
}

// constructor de copiere
Cheltuieli::Cheltuieli(const Cheltuieli &c) {
    this -> zi = c.zi;
    this -> suma = c.suma;
    if (c.tip != nullptr) {
        this->tip = new char[strlen(c.tip) + 1];
        strcpy(this->tip, c.tip);
    } else {
        this->tip = nullptr;
    }

}

//getter pt zi
int Cheltuieli::getzi() {
    return this -> zi;
}

//getter pt suma
int Cheltuieli::getsuma() {
    return this -> suma;
}

//getter pt tip
char *Cheltuieli::gettip() {
    return this -> tip;
}

// deconstructor:
Cheltuieli::~Cheltuieli() {
    if (this->tip != nullptr) {
        delete[] this->tip;
    }
}

//setter pt zi
void Cheltuieli::setzi(int zi) {
    this -> zi = zi;
}

//setter pt suma
void Cheltuieli::setsuma(int suma) {
    this -> suma = suma;
}

//setter pt tip
void Cheltuieli::settip(char *tip) {

    delete[] this->tip;

    this->tip = new char[strlen(tip) + 1];
    strcpy(this->tip, tip);
}

//suprascrierea operatorului <<
ostream &operator<<(ostream &output, Cheltuieli &other) {
    output << "Apartamentul " << other.getzi() << " a platit " << other.getsuma() << " pentru " << other.gettip();
    return output;
}

