//
// Created by ema_a on 5/30/2024.
//

#ifndef MODEL_FEDERATIE_SPORTIVA_RESTANTA_UI_H
#define MODEL_FEDERATIE_SPORTIVA_RESTANTA_UI_H


#include <iostream>
using namespace std;
#include "Service.h"

class UI {
private:

    Service service;

public:
    void addMeci();
    void afiseazaClasament();
    void genereazaTurneu();


    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //MODEL_FEDERATIE_SPORTIVA_RESTANTA_UI_H
