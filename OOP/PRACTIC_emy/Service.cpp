//
// Created by ema_a on 6/3/2024.
//

#include "Service.h"

void Service::addManuscris(string nume, int an, string autor, int nrPagini) {
    Manuscris m(nume, autor, an, nrPagini);
    if (repo.findElem(m) != -1)
        throw invalid_argument("Manuscrisul exista deja!");
    repo.addElem(m);
}

void Service::deleteManuscris(string nume, int an, string autor, int nrPagini) {
    Manuscris m(nume, autor, an, nrPagini);
    if (repo.findElem(m) == -1)
        throw invalid_argument("Manuscrisul nu exista!");
    repo.deleteElem(m);
}

vector<Manuscris> Service::afiseazaManuscrise() {
    return repo.getAll();
}

vector<Manuscris> Service::afiseazaLessThan50Pag() {
    vector<Manuscris> all = repo.getAll();
    vector<Manuscris> result;
    for (Manuscris manuscris : all) {
        if (manuscris.getNrPagini() < 50)
            result.push_back(manuscris);
    }
    if (result.empty())
        throw invalid_argument("Nu exista manuscrise cu mai putin de 50 de pagini!");
    return result;
}

void Service::updateManuscris() {
    vector<Manuscris> all = repo.getAll();

    bool ok = false;

    for (Manuscris manuscris : all) {

        time_t now = time(0);
        tm *ltm = localtime(&now);
        int anNou = 1900 + ltm->tm_year;

        string nume = manuscris.getNume();
        string originalNume = nume;

        transform(nume.begin(), nume.end(), nume.begin(), ::tolower);


        if (nume.find("poveste") != string::npos || nume.find("povestire") != string::npos || nume.find("story") != string::npos) {
            // Create the updated Manuscris with the current year
            Manuscris newM(originalNume, manuscris.getAutor(), anNou, manuscris.getNrPagini());
            repo.updateElem(manuscris, newM); // Assuming updateElem takes the old and new Manuscris objects
            ok = true;
        }
    }

    if (ok){
        cout << "Manuscrisele au fost modificate cu succes!" << endl;
    }
    else{
        throw invalid_argument("Nu exista manuscrise cu numele care sa contina 'poveste', 'povestire' sau 'story'!");
    }
}

void Service::updateVolume() {
    vector<Manuscris> all = repo.getAll();
    bool ok = false;
    int jumate1, jumate2;
    for (Manuscris manuscris : all) {
        if (manuscris.getNrPagini() >= 200)
        {
            jumate1 = manuscris.getNrPagini() / 2;
            jumate2 = manuscris.getNrPagini() - jumate1;
            string m1Name = manuscris.getNume() + " Volumul 1";
            string m2Name = manuscris.getNume() + " Volumul 2";
            Manuscris newM1(m1Name, manuscris.getAutor(), manuscris.getAn(),jumate1 );
            Manuscris newM2(m2Name, manuscris.getAutor(), manuscris.getAn(),jumate2);
            repo.updateElem(manuscris, newM1);
            repo.addElem(newM2);
            ok = true;
        }
    }
    if (!ok)
        throw invalid_argument("Nu exista manuscrise cu mai mult de 200 de pagini!");


}
