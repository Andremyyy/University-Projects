//
// Created by ema_a on 4/8/2024.
//

#ifndef GESTIUNE_APARTAMENTE_CHELTUIELI_H
#define GESTIUNE_APARTAMENTE_CHELTUIELI_H

#include <cstring>
#include <ostream>
using namespace std;


class Cheltuieli {
private:
    int zi;
    int suma;
    char *tip;
public:

    // constructori:

    Cheltuieli();//implicit
    Cheltuieli(int, int, char*);// general
    Cheltuieli( const Cheltuieli &c);// de copiere


    //getteri:

    int getzi();

    int getsuma();

    char * gettip();


    //deconstructor:

    ~Cheltuieli();


    //setteri:

    void setzi(int nr);
    void setsuma(int suma);
    void settip(char *tip);


    // Suprascrierea operatorului ==

    bool operator == (const Cheltuieli& other)  {
        return zi == other.zi && suma == other.suma && strcmp(tip, other.tip) == 0 ;
    }


    //Suprascrierea operatorului =

    Cheltuieli operator = (const Cheltuieli &c) {
        if (this != &c) { // Verificați auto-atribuirea
            this->zi = c.zi;
            this->suma = c.suma;

            if (this->tip != nullptr) {
                delete[] this->tip; // Eliberați memoria existentă
            }

            if (c.tip != nullptr) {
                this->tip = new char[strlen(c.tip) + 1];
                strcpy(this->tip, c.tip);
            } else {
                this->tip = nullptr;
            }
        }
        return *this;
    }

    //suprascrierea operatorului <<
    friend std::ostream &operator<<(std::ostream &output, Cheltuieli &other);
};

std::ostream &operator<<(std::ostream &output, Cheltuieli &other);


#endif //GESTIUNE_APARTAMENTE_CHELTUIELI_H
