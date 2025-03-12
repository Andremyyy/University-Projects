//
// Created by ema_a on 5/29/2024.
//

#include "UI.h"
using namespace std;



void UI::showMenu() {
    bool ok = true;
    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1. Insereaza obiect de arta in expozitie \n"
                "2. Afiseaza statistica in functie de voturi \n"
                " in ordine descrescatoare in functie de categorie  \n"
                "3. Calculeaza numărul de obiecte de artă dintr-o categorie dată\n"
                "care are artistul dat \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: " << endl;
        cin >> optiune;


        switch (optiune) {
            case 1: insertObiect(); break;
            case 2: afiseazaStatistica();break;
            case 3: calcNrObiecteCategorieNume(); break;
            case 0: ok = false; break;
            default: break;
        }
    }
}
// Aplicația trebuie să permită utilizatorilor să:
//1. Insereze în baza de date definiția unei compoziții,
// pe un index furnizat ca parametru de intrare (2p)
//Dacă obiectul există deja în cadrul catalogului expoziției, sau dacă indexul furnizat
//depășește dimensiunea catalogului, aplicația trebuie să afișeze un
// mesaj de avertizare în acest
//sens, și să nu permită inserarea acestuia în catalog (2p).
void UI::insertObiect() {

        string autor;
        string denumire;
        string categorie;
        int voturi;

        cout<<"Introduceti autorul: " << endl;
        cin >> autor;
        cout<<"Introduceti denumirea: " << endl;
        cin >> denumire;
        cout<<"Introduceti categorie: " << endl;
        cin >> categorie;
        cout<<"Introduceti nr de voturi: " << endl;
        cin>>voturi;

        int pozitie;
        cout << "Introdceti pozitia la care doriti sa adaugati obiectul: "<<endl;
        cout << "Pozitie maxima valida este " << service.getSize() << endl;
        cin >> pozitie;

        try {
            service.insertPoz(pozitie, autor, denumire, categorie, voturi);
            cout << "Obiect adaugat cu succes!" << endl;
        }
        catch (out_of_range &exp) {
            cout << exp.what() << endl;
        }
        catch (invalid_argument &exp) {
            cout << exp.what() << endl;
        }


}
//Vizualizeze o statistică a voturilor,
// care să conțină numărul de voturi pe fiecare categorie,
//sortată în ordine descrescătoare a numărului de voturi (2p).
void UI::afiseazaStatistica() {
    try{
        vector<StatisticaEntry> statistica = service.getStatistica();
        for (auto entry:statistica) {
            cout << entry.categorie << " " << entry.voturi << endl;
        }
    }
    catch (invalid_argument &ind){
        cout << ind.what() << endl;
    }
}

//3. Identifice numărul de obiecte de artă dintr-o categorie dată
// care au fost acceptate în cadrul
//expoziției, pentru care numele artistului creator este nume,
// unde nume reprezintă un parametru
//de intrare (2p).

void UI::calcNrObiecteCategorieNume(){
    string categorie;
    cout << "Introduceti categoria: " << endl;
    cin >> categorie;
    string artist;
    cout << "Introduceti numele artistului: " << endl;
    cin >> artist;

    try{
        int nr = service.calcNr(categorie, artist);
        cout << "Numarul de obiecte de arta din categoria " << categorie << " care au fost acceptate in cadrul expozitiei si au fost create de artistul " << artist << " este: " << nr << endl;
    }
    catch (invalid_argument &ind){
        cout << ind.what() << endl;
    }
}