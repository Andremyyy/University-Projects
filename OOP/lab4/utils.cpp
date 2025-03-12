//
// Created by ema_a on 3/25/2024.
//

#include <iostream>
using namespace std;
#include "Rectangle.h"

void read(Rectangle x[], int &n) {
    cout<< "Lungimea sirului este: " ;
    cin >> n;
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

void print(Rectangle x[], int n){
    int s=0;
    for(int i=0;i<n;i++)
    {
        int a=x[i].detAria();
        s=s+a;
        cout<<a<<endl;
    }
    cout<<s<<endl;
}

void determinare_cea_mai_mare(Rectangle x[], int n, Rectangle &sol) {

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
    return (sol.getx1() >= 0 && sol.gety2() >= 0 && sol.getx2() >= 0 && sol.gety1() >= 0);
}

void afisare_first_qudrant( bool rez, Rectangle sol){
    if (rez){
        cout << "Rectangle: " << sol.getx1() << " " << sol.getx2() << " " << sol.gety1() << " " <<  sol.gety2() << " " << "se afla in primul cadran";
    }
    else
        cout << "Rectangle: " << sol.getx1() << " " << sol.getx2() << " " << sol.gety1() << " " <<  sol.gety2() << " " << "NU se afla in primul cadran!!!";
}

int longestEqualSequence(Rectangle entities[], int size) {
    int maxLength = 1; // Lungimea maximă a secvenței
    int currentLength = 1; // Lungimea curentă a secvenței
    Rectangle entity = entities[0]; // Entitatea cu care comparăm
    Rectangle prevEntity = entities[0]; // Entitatea precedentă

    for (int i = 1; i < size; ++i) {
        if (entities[i] == prevEntity) {
            currentLength++;
            if (currentLength > maxLength) {
                maxLength = currentLength;
                entity = entities[i];
            }
        } else {
            currentLength = 1; // Resetăm lungimea secvenței curente
        }
        prevEntity = entities[i];
    }

    return maxLength;
}