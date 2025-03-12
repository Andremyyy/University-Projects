//
// Created by ema_a on 4/19/2024.
//

#include "UI.h"
#include <iostream>
#include "Cheltuieli.h"
using namespace std;

UI::UI(Service& service) : service(service) {

}

UI::~UI() {

}

void UI::read(int & day, int &money, char * & type){
    cout << "Dati ziua cheltuielii: " << endl;
    cin >> day;
    cout << "Dati suma cheltuielii: " << endl;
    cin >> money;
    cout << "Dati tipul cheltuielii: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> type;
}

void UI::insertChelt() {
    int day, money;
    char *type = new char[25];
    read(day, money, type);
    this->service.insertElem(day, money, type);
    delete[] type;
}

void UI::showMenu() {
    bool inchis = false;
    while (!inchis) {
        cout << "       Meniu:      " << endl;
        afiseazaOptiuni();
        cout << "Dati optiunea: ";
        int optiune;
        cin >> optiune;
        switch (optiune) {
            case 1: addChelt(); break;
            case 2: insertChelt(); break;
            case 3: update(); break;
            case 4: deleteChelt(); break;
            case 5: getAll();break;
            case 6: getsize(); break;
            case 7: deleteCheltZi(); break;
            case 8: deleteCheltInterval(); break;
            case 9: deleteCheltTip(); break;
            case 10: getAllTip(); break;
            case 11: getAllTipBiggerThanSuma(); break;
            case 12: getAllTipEqualSuma(); break;
            case 13: detSumaTip(); break;
            case 14: detZiMaxSuma(); break;
            case 15: sortareSumaDupaZi(); break;
            case 16: sortareSumaDupaTip(); break;
            case 17: sortareSumaDupaZiSiTip(); break;
            case 18: filtrareTip(); break;
            case 19: filtrareTipLessThanSuma(); break;
            case 20: filtrareTipEqualSuma(); break;
            case 21: undo(); break;
            case 0: inchis = true; break;
            default: cout << "Optiune invalida! Introduceti o optiune valida!" ; break;
        }
    }
}

void UI::afiseazaOptiuni() {
    cout << "1. Adauga cheltuiala" << endl;
    cout << "2. Insereaza cheltuiala" << endl;
    cout << "3. Update cheltuiala" << endl;
    cout << "4. Sterge cheltuiala data complet" << endl;
    cout << "5. Afiseaza toate cheltuielile" << endl;
    cout << "6. Afiseaza numar de cheltuieli" << endl;
    cout << "7. Sterge cheltuielile dintr-o zi data." << endl;
    cout << "8. Sterge cheltuielile dintr-un interval dat." << endl;
    cout << "9. Sterge cheltuielile de un tip dat." << endl;
    cout << "10. Afiseaza toate cheltuielile de un tip dat." << endl;
    cout << "11. Afiseaza toate cheltuielile de un tip dat care au suma mai mare strict decat o suma data." << endl;
    cout << "12. Afiseaza toate cheltuielile de un tip dat care au suma egala cu o suma data." << endl;
    cout << "13. Determina suma cheltuielilor de un tip dat." << endl;
    cout << "14. Afiseaza ziua cu suma maxima de cheltuielilor ." << endl;
    cout << "15. Sorteaza in ordine descrescatoare sumele cheltuite in ziua data." << endl;
    cout << "16. Sorteaza in ordine crescatoare sumele cheltuite in zilele lunii dupa un tip dat." << endl;
    cout << "17. Sorteaza in ordine crescatoare sumele cheltuite in ziua data dupa tipul dat." << endl;
    cout << "18. Filtreaza cheltuielile dupa tipul dat." << endl;
    cout << "19. Filtreaza cheltuielile dupa tipul dat si care au suma mai mica strict decat suma data." << endl;
    cout << "20. Filtreaza cheltuielile dupa tipul dat si care au suma egala cu suma data." << endl;
    cout << "21. UNDO. (reface ultima operatie) " << endl;
    cout << "0. Exit" << endl;
}

void UI::addChelt() {
    int suma;
    char *type = new char[25];
    cout << "Dati suma: " << endl;
    cin >> suma;
    cout << "Dati tipul: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> type;
    this->service.addElem(suma, type);
    delete[] type;
}


void UI::getAll(){
    cout << "Cheltuielile sunt: " << endl;
    int noChelt = service.getsize();
    vector <Cheltuieli> cheltuieli = service.getAll();
    if (noChelt == 0)
        cout << "NU exista cheltuieli!!!";
    else
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 <<". " << cheltuieli[i] << endl;
}


void UI::deleteChelt() {
    char * tip = new char[25];
    int suma, zi;
    read(zi, suma, tip);

    if (service.deleteElem(zi, suma, tip))
        cout << "STERGERE CU SUCCES!" << endl;
    else
        cout << "NU EXISTA CHELTUIALA DATA!!!" << endl;

    delete[] tip;
}

void UI::getsize() {
    int noChelt = service.getsize();
    if (noChelt)
        cout << "Exista " << noChelt << "cheltuieli" << endl;
    else
        cout << "Nu exista cheltuieli!!!" << endl;
}

void UI::deleteCheltZi() {
    int  zi;
    cout << "Dati ziua dupa care se doreste stergerea cheltuielilor: " << endl;
    cin >> zi;
    int optiune = service.deleteCheltZi(zi);
    if (optiune !=0)
        cout << optiune <<  " STERGERI CU SUCCES!" << endl;
    else
        cout << "NU EXISTA CHELTUIALA CU ZIUA DATA!!!" << endl;

}

void UI::deleteCheltInterval() {
    int  zi1, zi2;
    cout << "Dati ziua de inceput dupa care se doreste stergerea cheltuielilor: " << endl;
    cin >> zi1;
    cout << "Dati ziua de sfarsit dupa care se doreste stergerea cheltuielilor: " << endl;
    cin >> zi2;
    int optiune = service.deleteCheltInterval(zi1,zi2);
    if (optiune !=0)
        cout << optiune <<  " STERGERI CU SUCCES!" << endl;
    else
        cout << "NU EXISTA CHELTUIALA CU ZIUA DATA!!!" << endl;
}

void UI::deleteCheltTip() {
    char * tip = new char[25];

    cout << "Dati tipul dupa care se doreste stergerea cheltuielilor: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> tip;

    int optiune = service.deleteCheltTip(tip);
    if (optiune !=0)
        cout << optiune <<  " STERGERI CU SUCCES!" << endl;
    else
        cout << "NU EXISTA CHELTUIALA CU ZIUA DATA!!!" << endl;

    delete[] tip;
}

void UI::getAllTip() {
    char *tip = new char[25];

    cout << "Dati tipul dupa care se doreste afisarea cheltuielilor: (menaj/mancare/transport/haine/internet/altele)"
         << endl;
    cin >> tip;

    int noChelt = service.getSizeTip(tip);
    vector <Cheltuieli> cheltuieli = service.getAllTip(tip);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli de tipul dat!";
    else {
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }
    delete []tip;
}

void UI::getAllTipBiggerThanSuma() {
    char *tip = new char[25];
    int suma = 0;
    cout << "Dati tipul dupa care se doreste afisarea cheltuielilor: (menaj/mancare/transport/haine/internet/altele)"
         << endl;
    cin >> tip;
    cout << "Dati minimul sumei dupa care se doreste afisarea cheltuielilor: "
         << endl;
    cin >> suma;

    int noChelt = service.getSizeTipBiggerThanSuma(tip, suma);
    vector <Cheltuieli> cheltuieli = service.getAllTipBiggerThanSuma(tip, suma);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli de tipul dat care sa aiba suma mai mare strict decat suma data!" << endl;
    else {
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }
    delete [] tip;

}

void UI::getAllTipEqualSuma() {
    char *tip = new char[25];
    int suma = 0;
    cout << "Dati tipul dupa care se doreste afisarea cheltuielilor: (menaj/mancare/transport/haine/internet/altele)"
         << endl;
    cin >> tip;
    cout << "Dati sumei dupa care se doreste afisarea cheltuielilor: "
         << endl;
    cin >> suma;

    int noChelt = service.getSizeTipEqualSuma(tip, suma);
    vector < Cheltuieli > cheltuieli = service.getAllTipEqualSuma(tip, suma);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli de tipul dat care sa aiba suma egala cu suma data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }
    delete [] tip;
}

void UI::detSumaTip() {
    char *tip = new char[25];
    int suma = 0;
    cout << "Dati tipul dupa care se doreste calcularea sumei cheltuielilor: (menaj/mancare/transport/haine/internet/altele)"
         << endl;
    cin >> tip;

    suma = service.detSumaTip(tip);
    if (suma == 0)
        cout << "NU exista cheltuieli de tipul dat!" << endl;
    else
        cout << "Suma cheltuita pentru tripul: " << tip << " este: " << suma << endl;

    delete []tip;

}

void UI::detZiMaxSuma() {
    int zi = 0;
    zi = service.detZiMaxSuma();
    if (zi == 0)
        cout << "NU exista cheltuieli!" << endl;
    else
        cout << "Ziua cu suma maxima cheltuita este: " << zi << endl;
}

void UI::sortareSumaDupaZi(){
    int zi;
    cout << "Dati ziua dupa care doriti sa sortati descrescator sumele cheltuite:" << endl;
    cin >> zi;

    int noChelt = service.getSizeZi(zi);
    int cheltuieli[1000];
    service.getAllZiDescr(zi, cheltuieli);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli in ziua data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }
}

void UI::sortareSumaDupaTip() {
    char *tip = new char[25];

    cout << "Dati tipul dupa care doriti sa sortati crescator sumele cheltuite: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> tip;

    int cheltuieli[1000];
    int lung = 0;
    service.getAllTipCresc(tip, cheltuieli, lung);

    if (lung == 0)
        cout << "Nu exista cheltuieli in ziua data!" << endl;
    else{
        for (int i = 0; i < lung; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }

    delete [] tip;
}

void UI::sortareSumaDupaZiSiTip()  {
    char *tip = new char[25];
    int zi = 0;
    cout << "Dati tipul dupa care doriti sa sortati crescator sumele cheltuite: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> tip;
    cout << "Dati ziua dupa care doriti sa sortati crescator sumele cheltuite:" << endl;
    cin >> zi;

    int noChelt = service.getSizeTipZi(tip, zi);
    int cheltuieli[1000];
    service.getAllTipZiCresc(tip,zi, cheltuieli);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli in ziua data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }

    delete [] tip;
}

void UI::filtrareTip() {

    char *tip = new char[25];
    cout << "Dati tipul dupa care doriti cheltuielile: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> tip;

    int noChelt = service.getSizeTip(tip);
    vector <Cheltuieli> cheltuieli = service.getAllTip(tip);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli in ziua data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }

    delete [] tip;

}

void UI::filtrareTipLessThanSuma() {
    char *tip = new char[25];
    cout << "Dati tipul dupa care doriti cheltuielile: (menaj/mancare/transport/haine/internet/altele)" << endl;
    cin >> tip;

    int suma = 0;
    cout << "Dati suma MAXIMA dupa care doriti cheltuielile:" << endl;
    cin >> suma;

    int noChelt = service.getSizeTipLessThanSuma(tip, suma);
    vector <Cheltuieli> cheltuieli = service.getAllTipLessThanSuma(tip, suma);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli in ziua data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }

    delete [] tip;
}

void UI::filtrareTipEqualSuma() {

    char *tip = new char[25];
    int suma = 0;
    cout << "Dati tipul dupa care se doreste afisarea cheltuielilor: (menaj/mancare/transport/haine/internet/altele)"
         << endl;
    cin >> tip;
    cout << "Dati sumei dupa care se doreste afisarea cheltuielilor: "
         << endl;
    cin >> suma;

    int noChelt = service.getSizeTipEqualSuma(tip, suma);
    vector < Cheltuieli > cheltuieli = service.getAllTipEqualSuma(tip, suma);

    if (noChelt == 0)
        cout << "Nu exista cheltuieli de tipul dat care sa aiba suma egala cu suma data!" << endl;
    else{
        for (int i = 0; i < noChelt; i++)
            cout << i + 1 << ". " << cheltuieli[i] << endl;
    }
    delete [] tip;
}

void UI::update() {

    int zi;
    int zi_noua;
    int suma, suma_noua;
    char *tip = new char[25];
    char *tip_nou = new char[25];

    cout << "Dati ziua de modificat: " << endl;
    cin >> zi;
    cout << "Dati suma de modificat: " << endl;
    cin >> suma;
    cout << "Dati tipul de modificat: " << endl;
    cin >> tip;

    cout << "Dati ziua noua: " << endl;
    cin >> zi_noua;
    cout << "Dati suma noua: " << endl;
    cin >> suma_noua;
    cout << "Dati tipul nou: " << endl;
    cin >> tip_nou;

    if (service.updateElem(zi, suma, tip, zi_noua, suma_noua, tip_nou))
        cout << "Update reusit!" << endl;
    else
        cout << "Nu exista cheltuiala cu datele date!!!";

    delete []tip;
    delete[] tip_nou;

}

void UI::undo() {

    if (service.undo())
        cout << "Undo a avut succes!" << endl;
    else
        cout << "Nu se poate face undo!" << endl;

}
