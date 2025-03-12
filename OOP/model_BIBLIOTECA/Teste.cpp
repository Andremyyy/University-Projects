//
// Created by ema_a on 6/2/2024.
//

#include "Teste.h"

void Teste::testCarte() {
    Carte carte1("Ion", 2000, "Liviu", 5);
    assert(carte1.getNume() == "Ion");
    assert(carte1.getAn() == 2000);
    assert(carte1.getAutor() == "Liviu");
    assert(carte1.getBucati() == 5);
    Carte carte2("Moara", 2005, "Ioan", 3);
    assert(carte2.getNume() == "Moara");
    assert(carte2.getAn() == 2005);
    assert(carte2.getAutor() == "Ioan");
    assert(carte2.getBucati() == 3);
    Carte carte3("Ion", 2000, "Liviu", 5);
    assert(carte1 == carte3);
    assert(carte1 != carte2);
    carte1 = carte2;
    assert(carte1 == carte2);
    assert(carte1 != carte3);
    cout<<"Testele pentru clasa Carte au trecut cu succes!"<<endl;
}

void Teste::testService() {
    Repo<Carte> repo;
    Service service(repo);
    service.addCarte("Ion", 2000, "Liviu", 5);
    service.addCarte("Moara", 2005, "Ioan", 3);
    service.addCarte("Mara", 2003, "Liviu", 4);
    Carte carte_noua("Ion", 2010, "Liviu", 6);
    service.updateCarte("Ion", 2000, "Liviu", 5, carte_noua);
    vector<Carte> carti = service.afiseazaCarti();
    assert(carti.size() == 3);
    service.deleteCarte("Ion", 2010, "Liviu", 6);
    carti = service.afiseazaCarti();
    assert(carti.size() == 2);



    cout<<"Testele pentru clasa Service (operatii CRUD) au trecut cu succes!"<<endl;


    service.addCarte("Ion", 2010, "Liviu", 5);
    service.addCarte("Ion", 2013,"Tila", 8 );


    carti = service.sortNumeAutor();

    assert(carti[0].getNume() == "Ion" && carti[0].getAutor() == "Tila");
    assert(carti[1].getNume() == "Ion" && carti[1].getAutor() == "Liviu");
    cout<<"Testele pentru clasa Service (sortare) au trecut cu succes!"<<endl;

    service.filtrareCarti(2000, 4);
    carti = service.afiseazaCarti();
    assert(carti.size() == 2);
    cout<<"Testele pentru clasa Service (filtrare) au trecut cu succes!"<<endl;

}

void Teste::testRepo() {
    Repo<Carte> repo;
    Carte carte1("Ion", 2000, "Liviu", 5);
    Carte carte2("Moara", 2005, "Ioan", 3);
    Carte carte3("Mara", 2003, "Liviu", 4);
    repo.addElem(carte1);
    repo.addElem(carte2);
    repo.addElem(carte3);
    vector<Carte> carti = repo.getAll();
    assert(carti.size() == 3);
    repo.deleteElem(carte1);
    carti = repo.getAll();
    assert(carti.size() == 2);
    repo.updateElem(carte2, carte1);
    carti = repo.getAll();
    assert(carti[0].getNume() == "Ion");
    cout<<"Testele pentru clasa Repo au trecut cu succes!"<<endl;
}
