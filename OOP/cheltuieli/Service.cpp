//
// Created by ema_a on 4/19/2024.
//

#include "Service.h"
#include "Cheltuieli.h"
#include <ctime>
#include <cstring>
#include <iostream>
using namespace std;


//constructor implicit:
Service::Service() {

}

//deconstructor:
Service::~Service() {

}


int Service::today() {

    /*
     * Descr:determina ziua actuala
     * In:-
     * Out: ziua actuala de tip int
     */

    time_t now = time(0);
    tm *localTime = localtime(&now);
    return localTime -> tm_mday;
}


Cheltuieli Service::getElem(int pozitie) {

    /*
     * Descr: returneaza obiectul Cheltuiala de pe pozitia data
     * In: pozitie -  intreg
     * Out: un obiect Cheltuiala
     */

    return r.getElem(pozitie);
}


void Service::insertElem(int zi, int suma, char *tip) {

    /*
     * Descr: insereaza la sfarsit un obiect Cheltuiala cu ziua, suma si tipul date
     * In: zi, suma - intregi
     *     tip - char*
     * Out: -
     */

    Cheltuieli c(zi,suma, tip);
    r.addElem(c);

    // Salvăm informațiile pentru undo
    Operation op{"insert", {}, c,index: r.dim() - 1};
    history.push(op);
}


void Service::addElem(int suma, char *tip) {

    /*
     * Descr: adauga un  obiect Cheltuiala cu ziua actuala (foflosind functia today), suma si tipul date
     * In: suma - intreg
     *     tip - char*
     * Out: -
     */

    int zi = today();
    if (tip == nullptr) {
        throw invalid_argument("Tipul nu poate fi null");
    }
    Cheltuieli c(zi,suma, tip);
    r.addElem(c);

    // Salvează operațiunea în istoric
    Operation op{"add", {}, c, index:r.dim() - 1};
    history.push(op);  // Salvezi doar operațiunea, nu întregul repo

}


bool Service::deleteElem(int zi, int suma, char * tip) {

    /*
     * Descr: sterge  obiectul Cheltuiala cu ziua, suma si tipul date
     * In: zi, suma - intregi
           tip - char *
     * Out: True daca s-a efectuat stergerea
            altferl, False daca nu exista obiectul Cheltuiala cu datele date

     */

    int index = -1;
    int i;
    for (i = 0; i < r.dim(); i++)
        if (r.getElem(i).getzi() == zi && r.getElem(i).getsuma() == suma && strcmp(r.getElem(i).gettip(), tip) == 0){
            index = i;
            break;
            }
    if (index == -1)
        return false;

    Cheltuieli c = r.getElem(index);
    r.deleteElem(index);

    // Salvează operațiunea de ștergere pentru undo
    Operation op{"delete", previous: c, {},index: index};
    history.push(op);

    return true;
}


bool Service::updateElem(int zi, int suma, char *tip, int zi_noua, int suma_noua, char *tip_nou) {

    /*
     * Descr: modifica  obiectul Cheltuiala cu ziua, suma, tipul date in  obiectul Cheltuiala cu ziua_noua, suma_noua, tipul_nou date
     * In: zi, suma - intregi
           tip - char *
           zi_noua, suma_noua - intregi
           tip_nou - char *
     * Out: True daca s-a efectuat modificarea,
            altfel, False daca nu exista obiectul Cheltuiala cu datele date
     */
    int index = -1;
    int i;
    for (i = 0; i < r.dim(); i++)
        if (r.getElem(i).getzi() == zi && r.getElem(i).getsuma() == suma && strcmp(r.getElem(i).gettip(), tip) == 0){
            index = i;
            break;
        }
    if (index == -1)
        return false;

    Cheltuieli inainte = r.getElem(index);
    Cheltuieli actual(zi_noua, suma_noua, tip_nou);
    r.updateElem(index, actual);

    // Salvează operațiunea de actualizare pentru undo
    Operation op{"update", previous:inainte, actual, index:index};
    history.push(op);

    return true;
}


vector <Cheltuieli> Service::getAll() {

    /*
     * Descr: retuneaza vectorul cu toate cheltuielile
     * In: -
     * Out: vector de tip <Cheltuiala>
     */

    return r.getAll();
}


int Service::getsize() {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile
     * In: -
     * Out: intreg
     */

    return r.dim();
}


int Service::deleteCheltZi(int zi) {

    /*
     * Descr: sterge obiectele Cheltuiala din ziua data
     * In: zi - intreg
     * Out: numarul de stergeri efectuate - intreg
     */

    vector <Cheltuieli> cheltuieliSterse; // Pentru a reține cheltuielile șterse
    int sterse = 0;
    int index[1000];
    int i;
    for (i = 0; i < r.dim(); i++)
        if (r.getElem(i).getzi() == zi){
            index[sterse] = i;
            cheltuieliSterse.push_back(r.getElem(i)); // Stochez cheltuiala înainte de a o șterge
            sterse++;
        }
    if (sterse != 0) {
        for ( int j = sterse-1; j >= 0; j-- )
            for ( i = 0; i < r.dim(); i++)
                if ( i == index[j] ) {
                    r.deleteElem(i);
                    break;
                }

        // Adăugați operațiunea în istoricul undo
        Operation op{"deleteZi", cheltuieliSterse};  // Tipul de operațiune
        history.push(op);

    }
    return sterse;
}


int Service::deleteCheltInterval(int zi1, int zi2) {

    /*
     * Descr: sterge obiectele Cheltuiala din intervalul inchis dat
     * In: zi1, zi2 - intregi
     * Out: numarul de stergeri efectuate - intreg
     */

    vector <Cheltuieli> cheltuieliSterse;
    int sterse = 0; // Pentru a conta câte cheltuieli au fost șterse
    int index[1000]; // Indexul elementelor de șters
    int numIndex = 0; // Numărul total de elemente de șters

    // Ma asigur că intervalul este corect
    if (zi1 > zi2) {
        int temp = zi1;
        zi1 = zi2;
        zi2 = temp;
    }

    // Găsește indexurile pentru cheltuieli de șters
    for (int i = 0; i < r.dim(); i++) {
        int zi = r.getElem(i).getzi();
        if (zi >= zi1 && zi <= zi2) {
            index[numIndex] = i;
            cheltuieliSterse.push_back(r.getElem(i));
            numIndex++;
        }
    }

    // Șterge elementele, începând de la sfârșitul listei de indexuri
    if (numIndex > 0) {
        // Ștergerea trebuie să fie inversă pentru a evita schimbarea indexurilor
        for (int j = numIndex - 1; j >= 0; j--) {
            r.deleteElem(index[j]);
            sterse++;
        }
    }

    // Adăugați operațiunea în istoricul undo
    Operation op{"deleteInterval", cheltuieliSterse};  // Operațiunea de ștergere cu cheltuielile șterse
    history.push(op);  // Adaugă în istoric

    return sterse; // Returnează numărul de ștergeri
}


int Service::deleteCheltTip(char *tip) {

    /*
     * Descr: sterge obiectele Cheltuiala de tipul dat
     * In: tip - char*
     * Out: numarul de stergeri efectuate - intreg
     */

    vector <Cheltuieli> cheltuieliSterse;
    int sterse = 0;
    int index[1000];
    int i;
    for (i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(), tip) == 0){
            index[sterse] = i;
            cheltuieliSterse.push_back(r.getElem(i));
            sterse++;
        }
    if (sterse != 0) {
        for ( int j = sterse-1; j >= 0; j-- )
            for ( i = 0; i < r.dim(); i++)
                if ( i == index[j] ) {
                    r.deleteElem(i);
                    break;
                }
    }

    // Adăugați operațiunea în istoricul undo
    Operation op{"deleteTip", cheltuieliSterse}; // Creează o operațiune de tip "delete"
    history.push(op); // Salvați operațiunea în istoric

    return sterse;
}


int Service::getSizeTip(char *tip) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile de tipul dat
     * In: tip - char *
     * Out: intreg
     */


    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(), tip) == 0)
            sol++;

    return sol;
}


vector<Cheltuieli> Service :: getAllTip(char *tip) {

    /*
     * Descr: retuneaza vectorul cu toate cheltuielile de tipul dat
     * In: tip - char *
     * Out: vector de tip <Cheltuiala>
     */

    vector<Cheltuieli> solutie;
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0) {
            solutie.push_back(r.getElem(i));
        }
    }
    return solutie;
}


int Service::getSizeTipBiggerThanSuma(char *tip, int suma) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile de tipul dat cu suma strict mai mare decat suma data
     * In: tip - char *
           suma - intreg
     * Out: intreg
     */

    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() > suma)
            sol++;

    return sol;
}


vector<Cheltuieli> Service::getAllTipBiggerThanSuma(char *tip, int suma) {

    /*
     * Descr: retuneaza vectorul care contine toate cheltuielile de tipul dat cu suma strict mai mare decat suma data
     * In: tip - char *
           suma - intreg
     * Out: vector de tip <Cheltuieli>
     */

    vector<Cheltuieli> solutie;
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() > suma) {
            solutie.push_back(r.getElem(i));
        }
    }
    return solutie;
}


int Service::getSizeTipEqualSuma(char *tip, int suma) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile de tipul dat care au suma egala cu suma data
     * In: tip - char *
           suma - intreg
     * Out: intreg
     */

    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() == suma)
            sol++;

    return sol;
}


vector<Cheltuieli> Service::getAllTipEqualSuma(char *tip, int suma) {

    /*
     * Descr: returneaza vectorului care contine toate cheltuielile de tipul dat care au suma egala cu suma data
     * In: tip - char *
           suma - intreg
     * Out: vector de tip <Cheltuieli>
     */

    vector<Cheltuieli> solutie;
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() == suma) {
            solutie.push_back(r.getElem(i));
        }
    }
    return solutie;
}


int Service::detSumaTip(char *tip) {

    /*
     * Descr: returneaza suma cheltuilelilor de tipul dat
     * In: tip - char *
     * Out: intreg
     */

    int rezultat = 0;

    for (int i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(),tip) == 0)
            rezultat += r.getElem(i).getsuma();


    return rezultat;
}


int Service::detZiMaxSuma() {

    /*
     * Descr: determina ziua in care s-au efectuat cele mai multe cheltuieli in functie de suma cheltuita
     * In: -
     * Out: intreg
     */

    int rezultat[32];
    for ( int i = 0; i < 32; i++ )
        rezultat[i] = 0;
    int rezultat_maxim = 0;
    int zi_maxima = 0;

    for (int i = 0; i < r.dim(); i++)
        rezultat[r.getElem(i).getzi()] += r.getElem(i).getsuma();

    for (int i = 0; i< 32; i++ )
        if (rezultat[i] > rezultat_maxim) {
            rezultat_maxim = rezultat[i];
            zi_maxima = i;
        }

    return zi_maxima;
}


int Service::getSizeZi(int zi) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile din ziua data
     * In: zi - intreg
     * Out: intreg
     */

    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (r.getElem(i).getzi() == zi )
            sol++;

    return sol;
}


void Service::getAllZiDescr(int zi, int solutie[1000]) {

    /*
     * Descr: returneaza un vector care contine toate sumele cheltuile in ziua data ordonate descrescator
     * In: zi - intreg,
     * Out: solutie[1000] - vector cu valori intregi
     */

    int j = 0;
    for (int i = 0; i < r.dim(); i++) {
        if (r.getElem(i).getzi() == zi) {
            solutie[j] = r.getElem(i).getsuma();
            j++;
        }
    }

    //Sortare descrescatoare:
    for ( int i = 0; i < j-1; i++ )
        for ( int k = i+1; k < j; k++ )
            if (solutie [i] < solutie [k] ){
                int a = solutie[i];
                solutie[i] = solutie[k];
                solutie[k] = a;
            }
}


void Service::getAllTipCresc(char *tip, int solutie[1000], int &lung) {

    /*
     * Descr: returneaza un vector care contine toate sumele cheltuile de tipul dat ordonate crescator
     * In: tip - char *
     * Out: solutie[1000] - vector cu valori intregi,
            lung - intreg
     */

    lung = 0; // Numărul de zile cu cheltuieli pentru tipul dat
    int vector[1000];
    for ( int i = 0; i < 1000; i++ )
        vector[i] = 0;
    // Calculați suma cheltuielilor pentru fiecare zi cu tipul dat
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0) {
            int zi = r.getElem(i).getzi(); // Ziua cheltuielii
            vector[zi] += r.getElem(i).getsuma(); // Adăugați suma pentru ziua respectivă
        }
    }

    // Determinați lungimea efectivă a array-ului care conține sume nezero
    lung = 0;
    for (int i = 1; i <= 31; i++) { // zilele dintr-o lună
        if (vector[i] > 0) {
            solutie[lung] = vector[i]; // Puneți sumele nezero la începutul array-ului
            lung++;
        }
    }

    // Sortați în ordine crescătoare sumele găsite
    for (int i = 0; i < lung - 1; i++) {
        for (int j = i + 1; j < lung; j++) {
            if (solutie[i] > solutie[j]) { // Sortare manuală
                int temp = solutie[i];
                solutie[i] = solutie[j];
                solutie[j] = temp;
            }
        }
    }
}


int Service::getSizeTipZi(char *tip, int zi) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile din ziua data de tipul dat
     * In: tip - char*,
           zi - intreg
     * Out: intreg
     */

    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (r.getElem(i).getzi() == zi && strcmp(r.getElem(i).gettip(), tip) == 0)
            sol++;

    return sol;
}


void Service::getAllTipZiCresc(char *tip, int zi, int *solutie) {

    /*
     * Descr: returneaza un vector care contine toate sumele cheltuile de tipul dat in ziua data ordonate crescator
     * In: tip - char *,
           zi - intreg
     * Out: solutie - referinta la un vector cu valori intregi
     */

    int lung = 0;
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getzi() == zi) {
                solutie[lung] = r.getElem(i).getsuma();
                lung++;
            }
        }

    //Sortare crescator:
    for ( int i = 0; i < lung-1; i++ )
        for ( int k = i+1; k < lung; k++ )
            if (solutie [i] > solutie [k] ){
                int a = solutie[i];
                solutie[i] = solutie[k];
                solutie[k] = a;
            }
}


int Service::getSizeTipLessThanSuma(char *tip, int suma) {

    /*
     * Descr: returneaza marimea vectorului care contine toate cheltuielile de tipul dat cu suma mai mica strict decat suma data
     * In: tip - char*,
           suma - intreg
     * Out: intreg
     */

    int sol = 0;
    for (int i = 0; i < r.dim(); i++)
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() < suma)
            sol++;

    return sol;
}


vector<Cheltuieli> Service::getAllTipLessThanSuma(char *tip, int suma) {

    /*
     * Descr: returneaza un vector care contine toate cheltuielile de tipul dat cu suma mai mica strict decat suma data
     * In: tip - char*,
           suma - intreg
     * Out: vector de tip <Cheltuieli>
     */

    vector<Cheltuieli> solutie;
    for (int i = 0; i < r.dim(); i++) {
        if (strcmp(r.getElem(i).gettip(), tip) == 0 && r.getElem(i).getsuma() < suma) {
            solutie.push_back(r.getElem(i));
        }
    }
    return solutie;
}

bool Service::undo() {
    if (history.empty()) {
        return false;  // Nimic de anulat
    }

    Operation lastOp = history.top();  // Obtine ultima operațiune
    history.pop();  // Sterge din istoric

    if (lastOp.type == "add") {
        // Șterge ultima cheltuială adăugată
        if (r.dim() > 0) {
            r.deleteElem(r.dim() - 1);  // Șterge ultima cheltuială
        }
    }
    else if (lastOp.type == "delete") {
        // Re-adaugă cheltuiala ștearsă
        r.addElem(lastOp.previous);
    }
    else if (lastOp.type == "update") {
        // Re-adaugă vechea cheltuială
        r.updateElem(lastOp.index, lastOp.previous);
    }
    else if (lastOp.type == "insert") {
            r.deleteElem(r.dim() - 1);
    }
    else if (lastOp.type == "deleteZi" || lastOp.type == "deleteInterval" || lastOp.type == "deleteTip") {
        // presupunând că `lastOp.deleted` conține lista de cheltuieli șterse pentru ziua respectivă
        for (const auto& item : lastOp.deleted) {
            r.addElem(const_cast<Cheltuieli &>(item));  // re-adaugă fiecare element șters
        }
    }
    else if (lastOp.type == "insert"){
        if (r.dim() > 0) {
            r.deleteElem(r.dim() - 1);  // Șterge ultima cheltuială adăugată prin `insert`
        }
    }

    return true;  // Anularea a avut succes
}


//ostream &Service::operator<<(ostream &output, Service &service) {
//    // Afișează toate cheltuielile din repo-ul asociat cu serviciul
//    auto allExpenses = service.getAll(); // Obține toate cheltuielile
//    output << "Service contains " << allExpenses.size() << " expenses:\n";
//    for (Cheltuieli expense: allExpenses) {
//        output << "Day: " << expense.getzi() << ", Sum: " << expense.getsuma() << ", Type: " << expense.gettip()
//               << "\n";
//    }
//    return output;
//}
