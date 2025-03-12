//
// Created by ema_a on 3/25/2024.
//

#include <iostream>
#include <vector>
using namespace std;
#include "Rectangle.h"

void read(vector <Rectangle>& x, int &n) {
    cout<< "Lungimea sirului este: " ;
    cin >> n;

    x.reserve(n);
    for ( int i = 0; i < n;i++ )
        x.push_back(Rectangle());


    for (int i = 0; i < n; i++) {
        int a, b, c, d;
        cout << "a_" << i + 1 << "=";
        cin >> a;
        cout << "b_" << i + 1 << "=";
        cin >> b;
        cout << "c_" << i + 1 << "=";
        cin >> c;
        cout << "d_" << i + 1 << "=";
        cin >> d;
        cout << endl;
        x[i].setX1(a);
        x[i].setY1(b);
        x[i].setX2(c);
        x[i].setY2(d);
    }
}

void print(vector <Rectangle>& x, int n){
    int s=0;
    for(int i=0;i<n;i++)
    {
        int a=x[i].detAria();
        s=s+a;
        cout<<a<<endl;
    }
    cout<<s<<endl;
}

void determinare_cea_mai_mare(vector <Rectangle>& x, int n, Rectangle &sol) {
    // Functia determina dreptunghiul cu cea mai mare arie
    //In: un vector x de tipul Rectangle, n- un nr natural
    //Out: o variabila sol de tip Rectangle
    x.reserve(n);
    for ( int i = 0; i < n;i++ )
        x.push_back(Rectangle());
    sol.setX1(0);
    sol.setX2(0);
    sol.setY1(0);
    sol.setY2(0);

    int arie_maxima = -1;
    int arie_actuala = 0;

    for (int i = 0; i < n; i++) {
        arie_actuala = x[i].detAria();
        if (arie_actuala > arie_maxima){
            sol.setX1(x[i].getx1());
            sol.setX2(x[i].getx2());
            sol.setY1(x[i].gety1());
            sol.setY2(x[i].gety2());
            arie_maxima =  x[i].detAria();
        }

    }
}

void afisare_sol(Rectangle &sol){
    cout << "The rectangle that has the biggest area is: " << endl;
    cout << sol.getx1() << endl;
    cout << sol.getx2() << endl;
    cout << sol.gety1() << endl;
    cout << sol.gety2() << endl;
    cout << "si are aria de: " << endl;
    cout << sol.detAria() << endl;
}

bool isInFirstQuadrant(Rectangle sol)  {
    // Verificăm dacă toate colțurile dreptunghiului sunt în cadranul 1
    //In: sol - variabila de tip Rectangle
    //Out: False sau True

    return (sol.getx1() >= 0 && sol.gety2() >= 0 && sol.getx2() >= 0 && sol.gety1() >= 0);
}

void afisare_first_qudrant( bool rez, Rectangle sol){
    if (rez){
        cout << "Rectangle: " << sol.getx1() << " " << sol.getx2() << " " << sol.gety1() << " " <<  sol.gety2() << " " << "se afla in primul cadran";
    }
    else
        cout << "Rectangle: " << sol.getx1() << " " << sol.getx2() << " " << sol.gety1() << " " <<  sol.gety2() << " " << "NU se afla in primul cadran!!!";
}

void longestEqualSequence(vector <Rectangle>& entities, int size, int &maxLength, int &st, int &dr) {
    // Determina secventa de lungime maxima care contine dreptunghiuri egale din punct de vedere al coordonatelor
    //In: un vector de tip Rectangle, size- un nr natural
    //Out: 3 numere naturale
    entities.reserve(size);
    for ( int i = 0; i < size;i++ )
        entities.push_back(Rectangle());
    maxLength = 1; // Lungimea maximă a secvenței
    st = 0;
    dr = 0;
    int ok = 0;
    int currentLength = 1; // Lungimea curentă a secvenței
    Rectangle prevEntity;
    prevEntity=  entities[0]; // Entitatea precedentă
    int i;
    for ( i = 1; i < size; ++i) {
        if (entities[i] == prevEntity) {
            ok = 1;
            currentLength++;
            if (currentLength > maxLength) {
                dr = i;
                maxLength = currentLength;
            }
        }
        else if (ok == 1) {
            ok = 0;
            st = i - currentLength; // Actualizăm st pentru a marca începutul secvenței
            currentLength = 1; // Resetăm lungimea secvenței curente
        }
        prevEntity = entities[i];
    }

    if (ok == 1) {
        st = size - currentLength; // Actualizăm st pentru a marca începutul secvenței
        dr = i-1;
    }
}
