
//7.25 PM
//8.21 PM

#include <iostream>

//Subiect practic restanță
//
//O federație sportivă organizează un turneu de fotbal
// pentru un număr de 8 echipe înscrise.
// Se dorește menținerea evidenței scorului pe parcusul întregului turneu.
// Un meci se caracterizează prin numele celor două echipe participante
// și prin numărul de goluri marcate de către fiecare în cadrul meciului.
// O echipă primește 3 puncte dacă reușește să câștige un joc,
// 1 punct dacă scorul a fost unul egal si 0 puncte dacă pierde meciul.


//Dezvoltarea corectă a entităților necesare
//// (1p).
//Stil: specificare sub-algoritmi, claritate cod, etc.
//// (1p).
//Notă1: Aplicația trebuie să fie una stratificată.
// În cazul în care nu este, se va aplica o depunctare de 2p din nota finală.
//
//Notă2: Aplicația trebuie testată prin aserțiuni;
// în caz contrar, se va aplica o depunctare de 2p din nota finală.
//

//Notă3: Pentru generarea unui număr random între 0 și val se folosește:




#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "Meci.h"
#include "Teste.h"
int main() {
    Teste teste;
    teste.testService();
    teste.testRepo();
    teste.testeMeci();
    cout <<"Testele functioneaza!" << endl << endl;

    Repo<Meci> repo;

    Service service(repo);

    UI ui(service);

    ui.showMenu();
    return 0;
}
