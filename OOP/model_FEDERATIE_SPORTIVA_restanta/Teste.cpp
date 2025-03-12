//
// Created by ema_a on 5/30/2024.
//

#include "Teste.h"
#include "Service.h"
#include "Repo.h"
#include "Meci.h"
#include <cassert>
using namespace std;

void Teste::testService() {
    Repo<Meci> repo;
    Service service(repo);
    service.addMeci("e1", "e2", 3, 4);
    //e1 - 3
    //e2 -3
    //e3-0
    //e4-6
    service.addMeci("e3", "e1", 5, 6);
    service.addMeci("e3", "e4", 5, 6);
    service.addMeci("e2", "e4", 5, 6);
    vector <Echipa> echipe = service.getEchipe();
    assert(echipe.size() == 4);
    assert(echipe[0].getNume() == "e4");
    assert(echipe[0].getPunctaj() == 6);
    assert(echipe[1].getNume() == "e2");
    assert(echipe[1].getPunctaj() == 3);
    assert(echipe[2].getNume() == "e1");
    assert(echipe[2].getPunctaj() == 3);
    assert(echipe[3].getNume() == "e3");
    assert(echipe[3].getPunctaj() == 0);

    vector<Echipa> echipeCastigatoare = service.getCastigatori();
    int maxPunctaj = 0;
    for (auto& e : echipe) {
        if (e.getPunctaj() > maxPunctaj) {
            maxPunctaj = e.getPunctaj();
        }
    }
    int nrCastigatori = 0;
    vector <Echipa> castigatori;
    for (auto& e : echipe) {
        if (e.getPunctaj() == maxPunctaj) {
            castigatori.push_back(e);
        }
    }
    assert(maxPunctaj == echipe[0].getPunctaj());
    assert(echipe[0].getNume() == echipeCastigatoare[0].getNume());



}

void Teste::testRepo() {
    Repo<Meci> repo;
    Meci meci1("e1", "e2", 3, 4);
    Meci meci2("e3", "e4", 5, 6);
    repo.addElem(meci1);
    repo.addElem(meci2);
    assert(repo.getSize() == 2);
    assert(repo.findElem(meci1) == 0);
    assert(repo.findElem(meci2) == 1);
    assert(repo.elemAtPos(0) == meci1);
    assert(repo.elemAtPos(1) == meci2);
    vector<Meci> meciuri = repo.getAll();
    assert(meciuri.size() == 2);
    assert(meciuri[0] == meci1);
    assert(meciuri[1] == meci2);

}

void Teste::testeMeci() {
    Meci meci("e1", "e2", 3, 4);
    assert(meci.getEchipa1() == "e1");
    assert(meci.getEchipa2() == "e2");
    assert(meci.getGolEchipa1() == 3);
    assert(meci.getGolEchipa2() == 4);

    Meci meci_implicit = Meci();
    assert(meci_implicit.getEchipa1() == "");
    assert(meci_implicit.getEchipa2() == "");
    assert(meci_implicit.getGolEchipa1() == 0);
    assert(meci_implicit.getGolEchipa2() == 0);

    Meci meci_copiat = meci;
    assert(meci_copiat.getEchipa1() == "e1");
    assert(meci_copiat.getEchipa2() == "e2");
    assert(meci_copiat.getGolEchipa1() == 3);
    assert(meci_copiat.getGolEchipa2() == 4);

    assert(meci == meci_copiat);
    assert(meci != meci_implicit);

    meci.setEchipa1("e3");
    meci.setEchipa2("e4");
    meci.setGolEchipa1(5);
    meci.setGolEchipa2(6);
    assert(meci.getEchipa1() == "e3");
    assert(meci.getEchipa2() == "e4");
    assert(meci.getGolEchipa1() == 5);
    assert(meci.getGolEchipa2() == 6);

}
