//Bibleoteca
//Imagina'-va ca sunte' angajatul unei bibleoteci. Trebuie sa implementa' o
//aplica'e care permite opera'i CRUD asupra bibleotecii, prin manipularea
//en'ta'i de 'p CARTE.
//En'tatea de 'p Carte are: nume, anul publicarii, autor, numar de car7 in
//bibleoteca.
//Se cer urmatoarele:
//1. Ci're din fisier cu spa'i - 1.5p - din care 1p daca se foloseste mostenire
//2. Implementare opera'i CRUD - 2.5p - Ci're, Creere, Update si Delete
//3. Sortarea car'lor dupa un anumit criteriu (nume si autor) - 1p - 0.5 doar
//nume sau autor
//4. Filtrarea car'lor dupa un anumit criteriu (anul publicarii si numarul de car7
//disponibile) - 1p - 0.5 doar anul publicarii sau nr de car7 disponibile
//Se vor puncta urmatoarele:
//• arhitectura ( UI + Repo + Service) - 1p
//• teste si specifica'i - 2p - se puncteaza propor'onal pe numarul de
//func'onalita' implementate cu success (0.5 per func'onalitate
//completa)
//!!! Daca aplica'a nu are interfata consola (meniu si comenzi 1,2,3,...),
//inseamna ca nu e u'lizabila si nota finala va fi 1!
//!!! Daca aplica'a nu compileaza/ crapa la pornire, inseamna ca nu e
//u'lizabila si nota finala va fi 1!
//1 P din oficiu
//Timp de lucru: 70 min

#include <iostream>
#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "Carte.h"
#include "FileRepo.h"
#include "Teste.h"
using namespace std;

int main() {
    Teste teste;
    teste.testService();
      teste.testCarte();
      teste.testRepo();
    try {
        Repo<Carte> repo;
        FileRepo<Carte> frepo("biblioteca.txt");
        Service service( frepo);
        UI ui(service);

        ui.showMenu();
    }

    catch (invalid_argument &vaex){
        cout << "Erori: " << vaex.what() << endl;
    }    catch(...){
        cout << " Alte probleme: ..." << endl;
    }
    return 0;
}
