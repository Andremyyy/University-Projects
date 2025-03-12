#include <iostream>
#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "Manuscris.h"
#include "Teste.h"
using namespace std;

int main() {
    Teste teste;
    teste.testeManuscris();
    teste.testeRepo();
    teste.testeService();


     cout << "Testele functioneaza!";
    try {
        Repo<Manuscris> repo;
        Service service( repo);
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