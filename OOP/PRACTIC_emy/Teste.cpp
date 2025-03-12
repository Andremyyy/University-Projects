//
// Created by ema_a on 6/3/2024.
//

#include "Teste.h"

void Teste::testeRepo() {
    Repo<Manuscris> repo;
    Manuscris m1("Ion", "Rebreanu", 1800, 300);
    Manuscris m2("MaraEpilog", "smo", 1982, 15);
    Manuscris m3("story", "Camelia", 2000, 25);
    Manuscris m4("Enigma", "Sadoveanu", 1950, 50);
    Manuscris m5("POVESTIRE_Usoara", "Paula", 2012, 27);
    repo.addElem(m1);
    repo.addElem(m2);
    repo.addElem(m3);
    repo.addElem(m4);

    assert(repo.getSize() == 4);
    repo.deleteElem(m1);
    assert(repo.getSize() == 3);
    repo.updateElem(m2, m5);
    assert(repo.findElem(m5) == 0);


}

void Teste::testeManuscris() {
    Manuscris m1("Ion", "Rebreanu", 1800, 300);
    assert(m1.getNume() == "Ion");
    assert(m1.getAutor() == "Rebreanu");
    assert(m1.getAn() == 1800);
    assert(m1.getNrPagini() == 300);
    Manuscris m2(m1);
    assert(m1 == m2);
    assert(m2.getNume() == "Ion");
    assert(m2.getAutor() == "Rebreanu");
    assert(m2.getAn() == 1800);
    assert(m2.getNrPagini() == 300);
    Manuscris m = Manuscris();
    assert(m1 != m);
    assert(m.getNume() == "");
    assert(m.getAutor() == "");
    assert(m.getAn() == 0);
    assert(m.getNrPagini() == 0);
    m.setNume("Ion");
    assert(m.getNume() == "Ion");
    m.setAutor("Rebreanu");
    assert(m.getAutor() == "Rebreanu");
    m.setAn(1800);
    assert(m.getAn() == 1800);
    m.setNrPagini(300);
    assert(m.getNrPagini() == 300);

}

void Teste::testeService() {
    Repo<Manuscris> repo;
    Service service(repo);
    service.addManuscris("Luceafarul", 1883, "Eminescu", 100);
    service.addManuscris("Maxton", 2012, "julia", 45);
    service.addManuscris("AlbaPoveste", 1892, "Caragiale", 251);
    service.addManuscris("Moara", 1881, "Slavici", 200);
    service.addManuscris("TSITP", 2020, "Jenny", 200);

    service.addManuscris("Ion", 1880, "Rebreanu", 300);
    service.addManuscris("MaraEpilog", 1882, "SMO", 15);
    service.addManuscris("story", 2000, "Camelia", 25);

    service.addManuscris("Enigma", 1882, "Sadoveanu", 50);
    service.addManuscris("POVESTIRE_Usoara", 1925, "Paula", 27);


    // test afisare
    vector<Manuscris> manuscrise = service.afiseazaManuscrise();
    assert(manuscrise.size() == 10);

    //test updateVolume

    service.updateVolume();
    manuscrise = service.afiseazaManuscrise();
    assert(manuscrise.size() == 14);

    // test afiseaza volume cu mai putin de 50 de pagini

    manuscrise = service.afiseazaLessThan50Pag();
    assert(manuscrise.size() == 4);


}
