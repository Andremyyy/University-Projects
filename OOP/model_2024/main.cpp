
// 28.05.2024

//// E FARA TESTE SI FARA SPECIFICATII

#include <iostream>
using namespace std;
#include "Repo.h"
#include "Service.h"
#include "Bacterie.h"
#include "UI.h"

//TODO: testele


int main(){

//    teste();

    Repo<Bacterie> repo;

    Service service(repo);

    UI ui(service);

    ui.showMenu();
    return 0;
}