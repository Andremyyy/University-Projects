//
// Created by ema_a on 6/2/2024.
//

#ifndef MODEL_BIBLIOTECA_UI_H
#define MODEL_BIBLIOTECA_UI_H


#include <iostream>
using namespace std;
#include "Service.h"

class UI {
private:

    Service service;

public:

    void addCarte();
    void updateCarte();
    void deleteCarte();
    void afiseazaCarti();
    void sortNumeAutor();
    void filtrareCarti();


    ~UI() = default;
    UI(Service &service1) : service(service1) {

    }

    void showMenu();
};


#endif //MODEL_BIBLIOTECA_UI_H
