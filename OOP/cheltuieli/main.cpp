#include <iostream>
#include "tests.h"
#include "Cheltuieli.h"
#include "Repo.h"
#include "Service.h"
#include "UI.h"
using namespace std;

int main() {

//    testCheltuieli();
//    testRepo();
//    testService();
//    cout << "testele functioneaza!" << endl << endl;


    Repo repo;
    Service service;
    UI ui (service);

    ui.showMenu();


    return 0;
}
