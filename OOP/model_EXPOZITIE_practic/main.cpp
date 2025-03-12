// 7.35 pm 29.05.2024
// 8.42 pm 29.05.2024



//Expoziție
//Un muzeu organizează o expoziție virtuală de artă.
// Obiectele de artă pot fi identificate după autorul
//acestora, denumirea lor, respectiv categoria din care fac parte.
// Vizitatorii virtuali pot oferi voturi
// compozițiilor preferate.
//
// Aplicația trebuie să permită utilizatorilor să:
//1. Insereze în baza de date definiția unei compoziții, pe un index furnizat ca parametru de intrare
////(2p).
// Dacă obiectul există deja în cadrul catalogului expoziției, sau dacă indexul furnizat
// depășește dimensiunea catalogului, aplicația trebuie să afișeze un mesaj de avertizare în acest
// sens, și să nu permită inserarea acestuia în catalog
////(2p).

//2. Vizualizeze o statistică a voturilor, care să conțină numărul de voturi pe fiecare categorie,
//sortată în ordine descrescătoare a numărului de voturi
////(2p).
//3. Identifice numărul de obiecte de artă dintr-o categorie dată care au fost acceptate în cadrul
//        expoziției, pentru care numele artistului creator este nume, unde nume reprezintă un parametru
//de intrare
//// (2p).


//Dezvoltarea corectă a entităților necesare
////(1p).
//Stil: specificare sub-algoritmi, claritate cod, etc.
////(1p).

//Notă1: Aplicația trebuie să fie una stratificată. În cazul în care nu este, se va aplica o depunctare de 2p
//din nota finală.
//Notă2: Aplicația trebuie testată prin aserțiuni; în caz contrar, se va aplica o depunctare de 2p din nota
//finală.


#include <iostream>
#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "ObiectArta.h"
#include "Teste.h"

int main() {

    Teste teste;
    teste.testService();
    teste.testRepo();
    teste.testObiectArta();
    cout <<"Testele functioneaza!" << endl << endl;

    Repo<ObiectArta> repo;

    Service service(repo);

    UI ui(service);

    ui.showMenu();
    return 0;
}
