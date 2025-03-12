//
// Created by ema_a on 5/30/2024.
//

#ifndef MODEL_FEDERATIE_SPORTIVA_RESTANTA_MECI_H
#define MODEL_FEDERATIE_SPORTIVA_RESTANTA_MECI_H

//Un meci se caracterizează prin numele celor două echipe participante
// și prin numărul de goluri marcate de către fiecare în cadrul meciului.
// O echipă primește 3 puncte dacă reușește să câștige un joc,
// 1 punct dacă scorul a fost unul egal si 0 puncte dacă pierde meciul.

#include <iostream>
#include "string"
using namespace std;

class Meci {
private:
    string echipa1;
    string echipa2;
    int golEchipa1;
    int golEchipa2;
public:
    Meci(string echipa1, string echipa2, int golEchipa1, int golEchipa2) : echipa1(echipa1), echipa2(echipa2), golEchipa1(golEchipa1), golEchipa2(golEchipa2) {}

    Meci(){
        this->echipa1 = "";
        this->echipa2 = "";
        this->golEchipa1 = 0;
        this->golEchipa2 = 0;
    }

    Meci (const Meci& meci){
        this->echipa1 = meci.echipa1;
        this->echipa2 = meci.echipa2;
        this->golEchipa1 = meci.golEchipa1;
        this->golEchipa2 = meci.golEchipa2;
    }
    bool operator ==(const Meci& meci){
        return (this->echipa1 == meci.echipa1 && this->echipa2 == meci.echipa2 && this->golEchipa1 == meci.golEchipa1 && this->golEchipa2 == meci.golEchipa2);
    }

    Meci operator =(const Meci& meci){
        this->echipa1 = meci.echipa1;
        this->echipa2 = meci.echipa2;
        this->golEchipa1 = meci.golEchipa1;
        this->golEchipa2 = meci.golEchipa2;
        return *this;
    }

    bool operator != (const Meci& meci){
        return !(this->echipa1 == meci.echipa1 && this->echipa2 == meci.echipa2 && this->golEchipa1 == meci.golEchipa1 && this->golEchipa2 == meci.golEchipa2);
    }

    ostream &operator <<(ostream &os){
        os<<this->echipa1<<" "<<this->echipa2<<" "<<this->golEchipa1<<" "<<this->golEchipa2;
        return os;
    }

    void setEchipa1(string echipa1){
        this->echipa1 = echipa1;
    }

    void setEchipa2(string echipa2){
        this->echipa2 = echipa2;
    }

    void setGolEchipa1(int golEchipa1){
        this->golEchipa1 = golEchipa1;
    }

    void setGolEchipa2(int golEchipa2){
        this->golEchipa2 = golEchipa2;
    }

    string getEchipa1(){
        return this->echipa1;
    }

    string getEchipa2(){
        return this->echipa2;
    }

    int getGolEchipa1(){
        return this->golEchipa1;
    }

    int getGolEchipa2(){
        return this->golEchipa2;
    }

    ~Meci(){
        this->echipa1 = "";
        this->echipa2 = "";
        this->golEchipa1 = 0;
        this->golEchipa2 = 0;
    }

};


#endif //MODEL_FEDERATIE_SPORTIVA_RESTANTA_MECI_H
