//
// Created by ema_a on 6/3/2024.
//

#ifndef PRACTIC_MANUSCRIS_H
#define PRACTIC_MANUSCRIS_H

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Manuscris {
private:
    // atributele:
    string nume;
    string autor;
    int nrPagini;
    int an;

public:
    // constructor implicit

    Manuscris(){
        this->nume = "";
        this->autor = "";
        this->nrPagini = 0;
        this->an = 0;
    }

    // constructor cu parametri

    Manuscris(string nume, string autor, int an, int nrPagini) : nume(nume), autor(autor), nrPagini(nrPagini), an(an) {
    }

    // constructor de copiere
    Manuscris (const Manuscris& manuscris) : nume(manuscris.nume), autor(manuscris.autor), nrPagini(manuscris.nrPagini), an(manuscris.an) {
    }

    // getteri

    string getNume(){
        return nume;
    }

    string getAutor(){
        return autor;
    }

    int getNrPagini(){
        return nrPagini;
    }

    int getAn(){
        return an;
    }

    // setteri

    void setNume(string nume){
        this->nume = nume;
    }

    void setAutor(string autor){
        this->autor = autor;
    }

    void setNrPagini(int nrPagini){
        this->nrPagini = nrPagini;
    }

    void setAn(int an){
        this->an = an;
    }


    // destructor

    ~Manuscris(){
    }


    // operator de egalitate

    bool operator==(const Manuscris& manuscris){
        return nume == manuscris.nume && autor == manuscris.autor && nrPagini == manuscris.nrPagini && an == manuscris.an;
    }

    // operator de copiere

    void operator=(const Manuscris& manuscris){
        nume = manuscris.nume;
        autor = manuscris.autor;
        nrPagini = manuscris.nrPagini;
        an = manuscris.an;
    }

    // operator de afisare

    friend ostream& operator<<(ostream& os, const Manuscris& manuscris){
        os << "Nume: " << manuscris.nume << ", Autor: " << manuscris.autor << ", Numar pagini: " << manuscris.nrPagini << ", An: " << manuscris.an;
        return os;
    }
    // operator de neegalitate

    bool operator!=(const Manuscris& manuscris){
        return nume != manuscris.nume || autor != manuscris.autor || nrPagini != manuscris.nrPagini || an != manuscris.an;
    }

};



#endif //PRACTIC_MANUSCRIS_H
