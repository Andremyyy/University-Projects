//
// Created by ema_a on 6/1/2024.
//

#include "Service.h"

Service::Service(Repo<Profesor> bacterii) {
    this->elemRepo = bacterii;
}

int Service::calcNrProfesoriGreva() {
    vector<Profesor> profesori = this->elemRepo.getAll();
    int nr = 0;
    for (Profesor profesor : profesori) {
        if (profesor.getInGreva() == 1) {
            nr++;
        }
    }
    if (nr == 0) {
        throw invalid_argument("Nu exista profesori in greva!");
    }
    return nr;
}

vector<string> Service::calcDisciplinaMaxGreva() {
    int nrMax = 0;
    vector<string> disciplineMax;
    vector<Profesor> profesori = this->elemRepo.getAll();
    for (Profesor profesor : profesori) {
        if (profesor.getInGreva() == 1) {
            string disciplina = profesor.getDisciplina();
            int nr = 0;
            for (Profesor profesor1 : profesori) {
                if (profesor1.getDisciplina() == disciplina && profesor1.getInGreva() == 1 && profesor1.getNume() != profesor.getNume()) {
                    nr++;
                }
            }
            if (nr > nrMax) {
                nrMax = nr;
                disciplineMax.clear();
                disciplineMax.push_back(disciplina);
            } else if (nr == nrMax) {
                disciplineMax.push_back(disciplina);
            }
        }
    }

    if (disciplineMax.empty()) {
        throw invalid_argument("Nu exista profesori in greva!");
    }
    else {
        return disciplineMax;
    }
}

string Service::calcClasaMaxGreva() {
    int nrMax = 0;
    string clasaMax;
    vector<Profesor> profesori = this->elemRepo.getAll();
    for (Profesor profesor: profesori) {
        if (profesor.getInGreva() == 1) {
            vector<string> clasa = profesor.getClase();
            for (string clasa1: clasa) {
                int nr = 0;
                for (Profesor profesor1: profesori) {
                    if (find(profesor1.getClase().begin(), profesor1.getClase().end(), clasa1) !=
                        profesor1.getClase().end() && profesor1.getInGreva() == 1) {
                        nr++;
                    }
                }
                if (nr > nrMax) {
                    nrMax = nr;
                    clasaMax = clasa1;
                }
            }
        }
    }
    if (clasaMax.empty()) {
        throw invalid_argument("Nu exista profesori in greva!");
    }
    else {
        return clasaMax;
    }
}

vector<string> Service::calcDisciplineValabile(string clasa, string orar[20], int nr) {

    vector<Profesor> profesori = this->elemRepo.getAll();
    if (profesori.empty()) {
        throw invalid_argument("Nu exista profesori in baza de date!");
    }
    vector<string> disciplineValabile;
    for (Profesor profesor: profesori) {
        // verific daca clasa data are ora respectiva in orar si daca profesorul actual preda la aceasta clasa
        for (string clasa1: profesor.getClase()) {
            if (clasa1 == clasa) {
                bool ok = false;
                for (int i = 0; i < nr; i++) {
                    string ora = orar[i];
                    if (profesor.getDisciplina() == ora) {
                        ok = true;
                    }
                }
                if (ok && profesor.getInGreva() == 0) {
                    disciplineValabile.push_back(profesor.getDisciplina());
                }
            }
        }
    }
    if (disciplineValabile.empty()) {
        throw invalid_argument("Nu se poate preda nicio disciplina!");
    }
    else {
        return disciplineValabile;
    }
}

void Service::addProfesor(string nume, string disciplina, vector<string> clase, bool inGreva) {
    Profesor profesor(nume, disciplina, clase, inGreva);
    this->elemRepo.addElem(profesor);
}

vector<Profesor> Service::afiseazaProfesori() {
    return this->elemRepo.getAll();
}
