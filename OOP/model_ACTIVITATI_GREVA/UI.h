//
// Created by ema_a on 6/1/2024.
//

#ifndef MODEL_ACTIVITATI_GREVA_UI_H
#define MODEL_ACTIVITATI_GREVA_UI_H


#include <iostream>
using namespace std;
#include "Service.h"

class UI {
private:

    Service service;

public:

    void statisticaProfGreva();
    void statisticaDisciplinaMaxGreva();
    void calcClasaMaxGreva();
    void afiseazaOre();

    //in plus
    void addProfesor();
    void afiseazaProfesori();

    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //MODEL_ACTIVITATI_GREVA_UI_H
