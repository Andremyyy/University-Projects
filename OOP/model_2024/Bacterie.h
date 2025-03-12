//
// Created by ema_a on 5/28/2024.
//

#ifndef MODEL_2024_BACTERIE_H
#define MODEL_2024_BACTERIE_H

#include <string>
#include <iostream>
using namespace std;

class Bacterie {
private:
    string nume;
    int varsta;
    int tip;
public:
    Bacterie(string nume, int varsta, int tip) : nume(nume), varsta(varsta), tip(tip) {}

    Bacterie(const Bacterie& b) {
        this->nume = b.nume;
        this->varsta = b.varsta;
        this->tip = b.tip;
    }

    Bacterie& operator=(const Bacterie& b) {
        this->nume = b.nume;
        this->varsta = b.varsta;
        this->tip = b.tip;
        return *this;
    }

    void increaseVarsta() {
        this->varsta++;
    }

    Bacterie(){
        this->nume = "";
        this->varsta = 0;
        this->tip = 0;
    }

    bool operator ==(const Bacterie& b){
        return (this->nume == b.nume && this->varsta == b.varsta && this->tip == b.tip);
    }

    bool operator !=(const Bacterie& b){
        return !(this->nume == b.nume && this->varsta == b.varsta && this->tip == b.tip);
    }

    friend ostream& operator<<(ostream& os, const Bacterie& b){
        os<<b.nume<<" "<<b.varsta<<" "<<b.tip;
        return os;
    }


    string getNume() const {
        return nume;
    }

    int getVarsta() const {
        return varsta;
    }

    int getTip() const {
        return tip;
    }


};


#endif //MODEL_2024_BACTERIE_H
