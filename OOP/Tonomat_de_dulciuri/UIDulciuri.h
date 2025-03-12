//
// Created by Asus on 4/23/2024.
//

#ifndef TONOMAT_DE_DULCIURI_UIDULCIURI_H
#define TONOMAT_DE_DULCIURI_UIDULCIURI_H

#include "Service.h"
#include "ATM.h"
#include "Validator.h"
class UIDulciuri {
private:

    Service service;
    ATM atm;
    Validator validator;
public:
    void addDulce();
    void deleteDulce();
    void updateDulce();
    void findDulce();
    void getAll();


    ~UIDulciuri();
    UIDulciuri(Service &service1, ATM atm, Validator val) : service(service1), atm(atm), validator(val) {

    }

    void showMenu();

    void addMoneda();

    void addCerere();

    void showMonede();
};


#endif //TONOMAT_DE_DULCIURI_UIDULCIURI_H
