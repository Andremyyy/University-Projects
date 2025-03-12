//
// Created by ema_a on 6/2/2024.
//

#ifndef MODEL_BIBLIOTECA_CARTE_H
#define MODEL_BIBLIOTECA_CARTE_H

#include "string"
using namespace std;
#include "iostream"

class Carte {
private:
    string nume;
    int an;
    string autor;
    int bucati;
public:
    Carte(string nume, int an, string autor, int bucati) : nume(nume), an(an), autor(autor), bucati(bucati) {}
    Carte (){
        this->nume = "";
        this->an = 0;
        this->autor = "";
        this->bucati = 0;
    }
    Carte(const Carte& carte) {
        this->nume = carte.nume;
        this->an = carte.an;
        this->autor = carte.autor;
        this->bucati = carte.bucati;
    }

    ~Carte() = default;

    bool operator ==(const Carte& carte){
        return (this->nume == carte.nume && this->an == carte.an && this->autor == carte.autor && this->bucati == carte.bucati);
    }

    Carte operator =(const Carte& carte){
        this->nume = carte.nume;
        this->an = carte.an;
        this->autor = carte.autor;
        this->bucati = carte.bucati;
        return *this;
    }

    bool operator !=(const Carte& carte){
        return !(this->nume == carte.nume && this->an == carte.an && this->autor == carte.autor && this->bucati == carte.bucati);
    }

    ostream &operator <<(ostream &os){
        os<<this->nume<<" "<<this->an<<" "<<this->autor<<" "<<this->bucati;
        return os;
    }

    string getNume() const {
        return this-> nume;
    }

    void setNume(string nume) {
        this->nume = nume;
    }

    int getAn() const {
        return this-> an;
    }

    void setAn(int an) {
        this->an = an;
    }

    string getAutor() const {
        return this->autor;
    }

    void setAutor(string autor) {
        this->autor = autor;
    }

    int getBucati() const {
        return this->bucati;
    }

    void setBucati(int bucati) {
        this->bucati = bucati;
    }




};


#endif //MODEL_BIBLIOTECA_CARTE_H
