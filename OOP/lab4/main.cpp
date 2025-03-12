#include "test.h"
#include "Rectangle.h"

#include "utils.h"
#include <iostream>
using namespace std;

int main()
{
    testRectangle();
    test_determinare_cea_mai_mare();
    test_primul_cadran();
    test_cea_mai_lunga_secventa();



    Rectangle x[1000];
    int n = 0;
    Rectangle sol;

    int option;
    do {
        cout << "\n===== MENIU =====\n";
        cout << "1. Citire date\n";
        cout << "2. Afisare date\n";
        cout << "3. Determinare cea mai mare entitate\n";
        cout << "4. Afisare solutie\n";
        cout << "5. Verificare daca solutia se afla in primul cadran\n";
        cout << "6. Afisare rezultat verificare\n";
        cout << "7. Identificare cea mai lunga secventa de entitati egale\n";
        cout << "0. Iesire din program\n";
        cout << "Introduceti optiunea: ";
        cin >> option;

        switch (option) {
            case 1:
                read(x, n);
                break;
            case 2:
                print(x, n);
                break;
            case 3:
                determinare_cea_mai_mare(x, n, sol);
                afisare_sol(sol);
                break;
            case 5:
                for ( int i = 0; i < n; i++ ){
                    afisare_first_qudrant(isInFirstQuadrant(x[i]), x[i]);
                    cout << endl;
                }
                break;
            case 7:
                cout << "cea mai lunga secventa are lungimea: " << longestEqualSequence(x,n);
                break;
            case 0:
                cout << "Iesire din program...\n";
                break;
            default:
                cout << "Optiune invalida! Va rugam sa reincercati.\n";
        }
    } while (option != 0);


    return 0;

}

