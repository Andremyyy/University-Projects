//
// Created by ema_a on 5/29/2024.
//
//Expoziție
//Un muzeu organizează o expoziție virtuală de artă.
// Obiectele de artă pot fi identificate după autorul
//acestora, denumirea lor, respectiv categoria din care fac parte.
// Vizitatorii virtuali pot oferi voturi
//compozițiilor preferate.

#ifndef MODEL_EXPOZITIE_PRACTIC_OBIECTARTA_H
#define MODEL_EXPOZITIE_PRACTIC_OBIECTARTA_H

#include "string"
#include <iostream>
using namespace std;

class ObiectArta {
private:
    string autor;
    string denumire;
    string categorie;
    int voturi;
public:
    ObiectArta(string autor, string denumire, string categorie, int voturi) : autor(autor), denumire(denumire), categorie(categorie), voturi(voturi) {}
    ObiectArta(){
        this->autor = "";
        this->denumire = "";
        this->categorie = "";
        this->voturi = 0;
    }
    ObiectArta(const ObiectArta& obiectArta) {
        this->autor = obiectArta.autor;
        this->denumire = obiectArta.denumire;
        this->categorie = obiectArta.categorie;
        this->voturi = obiectArta.voturi;
    }

    bool operator ==(const ObiectArta& obiectArta){
        return (this->autor == obiectArta.autor && this->denumire == obiectArta.denumire && this->categorie == obiectArta.categorie && this->voturi == obiectArta.voturi);
    }

    ObiectArta operator =(const ObiectArta& obiectArta){
        this->autor = obiectArta.autor;
        this->denumire = obiectArta.denumire;
        this->categorie = obiectArta.categorie;
        this->voturi = obiectArta.voturi;
        return *this;
    }

    bool operator !=(const ObiectArta& obiectArta){
        return !(this->autor == obiectArta.autor && this->denumire == obiectArta.denumire && this->categorie == obiectArta.categorie && this->voturi == obiectArta.voturi);
    }

    ostream &operator <<(ostream &os){
        os<<this->autor<<" "<<this->denumire<<" "<<this->categorie<<" "<<this->voturi;
        return os;
    }

    void setAutor(string autor){
        this->autor = autor;
    }

    void setDenumire(string denumire){
        this->denumire = denumire;
    }

    void setCategorie(string categorie){
        this->categorie = categorie;
    }

    void setVoturi(int voturi){
        this->voturi = voturi;
    }

    string getAutor(){
        return this->autor;
    }

    string getDenumire(){
        return this->denumire;
    }

    string getCategorie(){
        return this->categorie;
    }

    int getVoturi(){
        return this->voturi;
    }


};


#endif //MODEL_EXPOZITIE_PRACTIC_OBIECTARTA_H
