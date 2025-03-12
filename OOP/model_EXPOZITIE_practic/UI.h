//
// Created by ema_a on 5/29/2024.
//

#ifndef MODEL_EXPOZITIE_PRACTIC_UI_H
#define MODEL_EXPOZITIE_PRACTIC_UI_H


#include <iostream>
using namespace std;
#include "Service.h"

class UI {
private:

    Service service;

public:
    void insertObiect();
    void afiseazaStatistica();
    void calcNrObiecteCategorieNume();


    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //MODEL_EXPOZITIE_PRACTIC_UI_H
