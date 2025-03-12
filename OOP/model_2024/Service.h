//
// Created by ema_a on 5/28/2024.
//

#ifndef MODEL_2024_SERVICE_H
#define MODEL_2024_SERVICE_H

#include "Repo.h"
#include "Bacterie.h"

class Service {
private:
    Repo<Bacterie> elemRepo;
public:
    Service(Repo<Bacterie> bacterii);
    ~Service() = default;

    void add(string nume, int varsta, int tip);
    vector<Bacterie> getAll();
    double calcMedieBacterii(int timp);



};

#endif //MODEL_2024_SERVICE_H
