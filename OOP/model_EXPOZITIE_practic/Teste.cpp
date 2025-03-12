//
// Created by ema_a on 5/29/2024.
//

#include "Teste.h"
#include <cassert>
using namespace std;

void Teste::testService() {

    Repo<ObiectArta> repo;

    Service service(repo);

    service.insertPoz(0,"autor1","denumire1","categorie1",1);
    service.insertPoz(1,"autor2","denumire2","categorie2",2);
    service.insertPoz(2,"autor3","denumire3","categorie3",3);
    service.insertPoz(3,"autor4","denumire4","categorie4",4);
    service.insertPoz(4,"autor5","denumire5","categorie5",5);
    assert(service.getSize() == 5);
    service.insertPoz(5,"autor3","den5","categorie3",6);
    assert(service.calcNr("categorie1","autor1") == 1);
    assert(service.calcNr("categorie3","autor3") == 2);
    vector<StatisticaEntry> statistica = service.getStatistica();
    assert(statistica.size() == 5);
    assert(statistica[0].categorie == "categorie3");
    assert(statistica[0].voturi == 9);
    assert(statistica[1].categorie == "categorie5");
    assert(statistica[1].voturi == 5);
    assert(statistica[2].categorie == "categorie4");
    assert(statistica[2].voturi == 4);
    assert(statistica[3].categorie == "categorie2");
    assert(statistica[3].voturi == 2);
    assert(statistica[4].categorie == "categorie1");
    assert(statistica[4].voturi == 1);

}

void Teste::testRepo() {
    Repo<ObiectArta> repo;
    ObiectArta obiectArta1("autor1","denumire1","categorie1",1);
    ObiectArta obiectArta2("autor2","denumire2","categorie2",2);
    ObiectArta obiectArta3("autor3","denumire3","categorie3",3);
    ObiectArta obiectArta4("autor4","denumire4","categorie4",4);
    ObiectArta obiectArta5("autor5","denumire5","categorie5",5);
    repo.insertPoz(0,obiectArta1);
    repo.insertPoz(1,obiectArta2);
    repo.insertPoz(0,obiectArta3);
    repo.insertPoz(2,obiectArta4);
    repo.insertPoz(4,obiectArta5);
    assert(repo.getSize() == 5);
    assert(repo.findElem(obiectArta1) == 1);
    assert(repo.findElem(obiectArta2) == 3);
    assert(repo.findElem(obiectArta3) == 0);
    assert(repo.findElem(obiectArta4) == 2);
    assert(repo.findElem(obiectArta5) == 4);
    assert(repo.elemAtPos(0) == obiectArta3);
    assert(repo.elemAtPos(1) == obiectArta1);
    assert(repo.elemAtPos(2) == obiectArta4);
    assert(repo.elemAtPos(3) == obiectArta2);
    assert(repo.elemAtPos(4) == obiectArta5);
    vector<ObiectArta> obiecte = repo.getAll();
    assert(obiecte.size() == 5);
    assert(obiecte[0] == obiectArta3);
    assert(obiecte[1] == obiectArta1);
    assert(obiecte[2] == obiectArta4);
    assert(obiecte[3] == obiectArta2);
    assert(obiecte[4] == obiectArta5);


}

void Teste::testObiectArta() {
    ObiectArta obiectArta1("autor1","denumire1","categorie1",1);
    ObiectArta obiectArta2("autor2","denumire2","categorie2",2);
    ObiectArta obiectArta3("autor3","denumire3","categorie3",3);
    ObiectArta obiectArta4("autor4","denumire4","categorie4",4);
    ObiectArta obiectArta5("autor5","denumire5","categorie5",5);
    assert(obiectArta1.getAutor() == "autor1");
    assert(obiectArta1.getDenumire() == "denumire1");
    assert(obiectArta1.getCategorie() == "categorie1");
    assert(obiectArta1.getVoturi() == 1);
    assert(obiectArta2.getAutor() == "autor2");
    assert(obiectArta2.getDenumire() == "denumire2");
    assert(obiectArta2.getCategorie() == "categorie2");
    assert(obiectArta2.getVoturi() == 2);
    assert(obiectArta3.getAutor() == "autor3");
    assert(obiectArta3.getDenumire() == "denumire3");
    assert(obiectArta3.getCategorie() == "categorie3");
    assert(obiectArta3.getVoturi() == 3);
    assert(obiectArta4.getAutor() == "autor4");
    assert(obiectArta4.getDenumire() == "denumire4");
    assert(obiectArta4.getCategorie() == "categorie4");
    assert(obiectArta4.getVoturi() == 4);
    assert(obiectArta5.getAutor() == "autor5");
    assert(obiectArta5.getDenumire() == "denumire5");
    assert(obiectArta5.getCategorie() == "categorie5");
    assert(obiectArta5.getVoturi() == 5);

    ObiectArta obiectArta6 = obiectArta1;
    assert(obiectArta6 == obiectArta1);

    ObiectArta B1 = ObiectArta("autor1","denumire1","categorie1",1);

    assert(B1.getAutor() == "autor1");
    assert(B1.getDenumire() == "denumire1");
    assert(B1.getCategorie() == "categorie1");
    assert(B1.getVoturi() == 1);

    assert(B1 != obiectArta2);
    assert(B1 == obiectArta1);

}
