//
// Created by ema_a on 6/3/2024.
//

#ifndef PRACTIC_UI_H
#define PRACTIC_UI_H


#include <iostream>
using namespace std;
#include "Service.h"

class UI {
private:

    Service service;

public:

    //// DECLAR TOATE FUNCTIILE NECESARE
    //void addCarte();
    void getAll();
    void getAllLessThan50Pag();
    void updateManuscrisDupaNume();

    void premiumUpdate();

    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //PRACTIC_UI_H
