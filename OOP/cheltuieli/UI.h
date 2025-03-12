//
// Created by ema_a on 4/19/2024.
//

#ifndef GESTIUNE_APARTAMENTE_UI_H
#define GESTIUNE_APARTAMENTE_UI_H

#include "Service.h"

class UI {
private:
    Service &service;
public:
    UI(Service& service);
    ~UI();

    void read(int&, int&, char*&);
    void insertChelt();
    void addChelt();
    void getAll();
    void deleteChelt();
//    void getChelt();
    void showMenu();
    void afiseazaOptiuni();
    void getsize();
    void deleteCheltZi();
    void deleteCheltInterval();
    void deleteCheltTip();
    void getAllTip();
    void getAllTipBiggerThanSuma();
    void getAllTipEqualSuma();
    void detSumaTip();
    void detZiMaxSuma();
    void sortareSumaDupaZi();
    void sortareSumaDupaTip();
    void sortareSumaDupaZiSiTip();

    void filtrareTip();
    void filtrareTipLessThanSuma();
    void filtrareTipEqualSuma();

    void update();

    void undo();

};


#endif //GESTIUNE_APARTAMENTE_UI_H
