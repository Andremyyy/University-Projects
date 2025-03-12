//
// Created by Asus on 4/23/2024.
//

#ifndef TONOMAT_DE_DULCIURI_SERVICE_H
#define TONOMAT_DE_DULCIURI_SERVICE_H

#include "RepoDulciuri.h"
#include "Dulciuri.h"

class Service {
private:
    RepoDulciuri<Dulciuri> elemRepo;
public:
    Service(RepoDulciuri<Dulciuri> dulciuri);
    ~Service() = default;

    void add(string nume, int pret);
    void remove(int, string, int);
    void update(int cod, string nume, int pret,  Dulciuri& dulceNou);
    int find(int , string, int);
    vector<Dulciuri> getAll();

    // Operator de egalitate
    bool operator==(const Service& other) const {
        return elemRepo == other.elemRepo;
    }
};


#endif //TONOMAT_DE_DULCIURI_SERVICE_H
