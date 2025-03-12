//
// Created by ema_a on 5/28/2024.
//

#ifndef MODEL_2024_UI_H
#define MODEL_2024_UI_H

#include "Service.h"
#include "Bacterie.h"
#include <iostream>
using namespace std;

class UI {
private:

    Service service;

public:
    void addBacterie();
    void showAllBacterii();
    void showBacteriiTip();
    void CalculeazaBacteriiTimp();


    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //MODEL_2024_UI_H
