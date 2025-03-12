//
// Created by ema_a on 6/2/2024.
//

#include "UI.h"

void UI::showMenu() {
    bool ok = true;


    while (ok) {
        cout << "-----------Meniu:-----------" << endl;
        cout << "1. Adauga carte in biblioteca. \n"
                "2. Afiseaza cartile din biblioteca. \n"
                "3. Update carte existenta in biblioteca \n"
                "4. Sterge carte din biblioteca \n"
                "5. Afiseaza cartile sortate dupa nume si autor \n"
                "6. Filtrare carti dupa an si buacti. \n"
                "0. EXIT \n\n\n";
        int optiune;
        cout << "Alege o optiune: " << endl;
        cin >> optiune;


        switch (optiune) {
            case 1: addCarte(); break;
            case 2: afiseazaCarti();break;
            case 3: updateCarte(); break;
            case 4: deleteCarte(); break;
            case 5: sortNumeAutor(); break;
            case 6: filtrareCarti(); break;
            case 0: ok = false; break;
            default: break;
        }
    }
}

void UI::addCarte() {
    string nume;
    cout << "Introduceti numele cartii: " << endl;
    cin >> nume;

    int an;
    cout << "Introduceti anul aparitiei cartii: " << endl;
    cin >> an;

    if (an <= 0)
        throw invalid_argument("Anul trebuie sa fie pozitiv!");

    string autor;
    cout << "Introduceti numele autorului cartii: " << endl;
    cin >> autor;

    int bucati;
    cout << "Introduceti numarul de bucati disponibile: " << endl;
    cin >> bucati;

    if (bucati <= 0)
        throw invalid_argument("Numarul de bucati trebuie sa fie pozitiv!");

    try{
        service.addCarte(nume, an, autor, bucati);
        cout << "Cartea a fost adaugata cu succes!" << endl;
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }


}

void UI::updateCarte() {
    string nume;
    cout << "Introduceti numele cartii: " << endl;
    cin >> nume;

    int an;
    cout << "Introduceti anul aparitiei cartii: " << endl;
    cin >> an;

    if (an <= 0)
        throw invalid_argument("Anul trebuie sa fie pozitiv!");

    string autor;
    cout << "Introduceti numele autorului cartii: " << endl;
    cin >> autor;

    int bucati;
    cout << "Introduceti numarul de bucati disponibile: " << endl;
    cin >> bucati;

    if (bucati <= 0)
        throw invalid_argument("Numarul de bucati trebuie sa fie pozitiv!");

    string numeNou;
    cout << "Introduceti noul nume al cartii: " << endl;
    cin >> numeNou;

    int anNou;
    cout << "Introduceti noul an al cartii: " << endl;
    cin >> anNou;

    if (anNou <= 0)
        throw invalid_argument("Anul trebuie sa fie pozitiv!");

    string autorNou;
    cout << "Introduceti noul autor al cartii: " << endl;
    cin >> autorNou;

    int bucatiNou;
    cout << "Introduceti noul numar de bucati disponibile: " << endl;
    cin >> bucatiNou;

    if (bucatiNou <= 0)
        throw invalid_argument("Numarul de bucati trebuie sa fie pozitiv!");

    try{
        Carte carteNoua(numeNou, anNou, autorNou, bucatiNou);
        service.updateCarte(nume, an, autor, bucati, carteNoua);
        cout << "Cartea a fost updatata cu succes!" << endl;
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }

}

void UI::deleteCarte() {
    string nume;
    cout << "Introduceti numele cartii: " << endl;
    cin >> nume;

    int an;
    cout << "Introduceti anul aparitiei cartii: " << endl;
    cin >> an;

    if (an <= 0)
        throw invalid_argument("Anul trebuie sa fie pozitiv!");

    string autor;
    cout << "Introduceti numele autorului cartii: " << endl;
    cin >> autor;

    int bucati;
    cout << "Introduceti numarul de bucati disponibile: " << endl;
    cin >> bucati;

    if (bucati <= 0)
        throw invalid_argument("Numarul de bucati trebuie sa fie pozitiv!");

    try{
        service.deleteCarte(nume, an, autor, bucati);
        cout << "Cartea a fost stearsa cu succes!" << endl;
    }
    catch (invalid_argument &e) {
        cout << e.what() << endl;
    }


}

void UI::afiseazaCarti() {
    vector<Carte> carti = service.afiseazaCarti();
    if (carti.empty()) {
        cout << "Nu exista carti in biblioteca!" << endl;
        return;
    }
    for (Carte carte : carti) {
        cout << carte.getNume() << " " << carte.getAn() << " " << carte.getAutor() << " " << carte.getBucati() << endl;
    }

}

void UI::sortNumeAutor() {

    vector<Carte> carti = service.sortNumeAutor();
    if (carti.empty()) {
        cout << "Nu exista carti in biblioteca!" << endl;
        return;
    }
    for (Carte carte : carti) {
        cout << carte.getNume() << " " << carte.getAn() << " " << carte.getAutor() << " " << carte.getBucati() << endl;
    }
}

void UI::filtrareCarti() {
    int an;
    cout << "Introduceti anul dupa care doriti sa filtrati cartile: " << endl;
    cin >> an;

    if (an <= 0)
        throw invalid_argument("Anul trebuie sa fie pozitiv!");

    int bucati;
    cout << "Introduceti numarul de bucati dupa care doriti sa filtrati cartile: " << endl;
    cin >> bucati;

    if (bucati <= 0)
        throw invalid_argument("Numarul de bucati trebuie sa fie pozitiv!");

    vector<Carte> carti = service.filtrareCarti(an, bucati);
    if (carti.empty()) {
        cout << "Nu exista carti in biblioteca care sa satisfaca cerintele!" << endl;
        return;
    }
    for (Carte carte : carti) {
        cout << carte.getNume() << " " << carte.getAn() << " " << carte.getAutor() << " " << carte.getBucati() << endl;
    }
}
