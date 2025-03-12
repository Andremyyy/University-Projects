//
// Created by ema_a on 3/18/2024.
//

#include "test.h"
#include "utils.h"
#include "Rectangle.h"
#include "cassert"
#include <cmath>
#include <vector>
using namespace std;

void testRectangle()
{

    Rectangle r1;
    assert(r1.getx1()==0);

    Rectangle r2(3, 4, 5, 1);
    assert(r2.getx1()==3);

    Rectangle r3(r2);
    assert(r3.getx1()==3);
    r3.setX1(2);
    assert(r3.getx1()==2);
    assert(r3.detAria()==9);

    double epsilon = 0.000001;

    assert(r2.detSRA() - sqrt(6) < epsilon);

}

void test_determinare_cea_mai_mare(){
    vector <Rectangle> x;

    Rectangle sol;

    determinare_cea_mai_mare(x,0,sol);

    assert(sol.getx1()==0);
    assert(sol.getx2()==0);
    assert(sol.gety1()==0);
    assert(sol.gety2()==0);

    int n = 5;
    x.reserve(n);
    for ( int i = 0; i < n;i++ )
        x.push_back(Rectangle());

    x[0].setX1(8);
    x[0].setX2(4);
    x[0].setY1(2);
    x[0].setY2(2);

    x[1].setX1(8);
    x[1].setX2(4);
    x[1].setY1(5);
    x[1].setY2(2);
    x[2].setX1(8);
    x[2].setX2(4);
    x[2].setY1(2);
    x[2].setY2(2);
    x[3].setX1(8);
    x[3].setX2(4);
    x[3].setY1(2);
    x[3].setY2(2);
    x[4].setX1(8);
    x[4].setX2(4);
    x[4].setY1(2);
    x[4].setY2(2);

    assert(x[1].detAria() == 12);
    assert(x[0].detAria()==0);

    determinare_cea_mai_mare(x,5,sol);

    assert(sol.getx1()==8);
    assert(sol.getx2()==4);
    assert(sol.gety1()==5);
    assert(sol.gety2()==2);

    x[1].setX1(8);
    x[1].setX2(4);
    x[1].setY1(2);
    x[1].setY2(2);

    determinare_cea_mai_mare(x,5,sol);

    assert(sol.getx1()==8);
    assert(sol.getx2()==4);
    assert(sol.gety1()==2);
    assert(sol.gety2()==2);

}

void test_primul_cadran(){
    vector <Rectangle> x;
    x.reserve(5);
    for ( int i = 0; i < 5;i++ )
        x.push_back(Rectangle());
    x[0].setX1(8);
    x[0].setX2(-4);
    x[0].setY1(2);
    x[0].setY2(2);
    x[1].setX1(8);
    x[1].setX2(4);
    x[1].setY1(5);
    x[1].setY2(2);
    x[2].setX1(-8);
    x[2].setX2(4);
    x[2].setY1(-2);
    x[2].setY2(2);

    assert(isInFirstQuadrant(x[0]) == false);
    assert(isInFirstQuadrant(x[1]) == true);
    assert(isInFirstQuadrant(x[2]) == false);
}

void test_cea_mai_lunga_secventa(){
    vector <Rectangle> x;
    x.reserve(5);
    for ( int i = 0; i < 5;i++ )
        x.push_back(Rectangle());
    x[0].setX1(8);
    x[0].setX2(4);
    x[0].setY1(2);
    x[0].setY2(2);
    x[1].setX1(8);
    x[1].setX2(4);
    x[1].setY1(2);
    x[1].setY2(2);
    x[2].setX1(8);
    x[2].setX2(4);
    x[2].setY1(2);
    x[2].setY2(2);
    x[3].setX1(8);
    x[3].setX2(4);
    x[3].setY1(2);
    x[3].setY2(2);
    x[4].setX1(8);
    x[4].setX2(4);
    x[4].setY1(2);
    x[4].setY2(2);

    int l, s, d;
    longestEqualSequence(x, 5, l ,s, d);

    assert(l == 5);
    assert (s == 0);
    assert(d == 4);

    x[1].setX1(1);
    x[1].setX2(2);
    x[1].setY1(3);
    x[1].setY2(4);

    longestEqualSequence(x, 5, l ,s, d);


    assert(l == 3);
    assert(s == 2);
    assert(d == 4);

    x[1].setX1(1);
    x[1].setX2(1);
    x[1].setY1(1);
    x[1].setY2(1);
    x[0].setX1(0);
    x[0].setX2(0);
    x[0].setY1(0);
    x[0].setY2(0);
    x[2].setX1(2);
    x[2].setX2(2);
    x[2].setY1(2);
    x[2].setY2(2);
    x[3].setX1(3);
    x[3].setX2(3);
    x[3].setY1(3);
    x[3].setY2(3);
    x[4].setX1(4);
    x[4].setX2(4);
    x[4].setY1(4);
    x[4].setY2(4);

    longestEqualSequence(x, 5, l ,s, d);

    assert(l == 1);
    assert(s == 0);
    assert(d == 0);

    x[1].setX1(1);
    x[1].setX2(1);
    x[1].setY1(1);
    x[1].setY2(1);
    x[0].setX1(1);
    x[0].setX2(1);
    x[0].setY1(1);
    x[0].setY2(1);
    x[2].setX1(2);
    x[2].setX2(2);
    x[2].setY1(2);
    x[2].setY2(2);
    x[3].setX1(3);
    x[3].setX2(3);
    x[3].setY1(3);
    x[3].setY2(3);
    x[4].setX1(3);
    x[4].setX2(3);
    x[4].setY1(3);
    x[4].setY2(3);

    longestEqualSequence(x, 5, l ,s, d);

    assert(l == 2);
    assert (s == 3);
    assert(d == 4);

}
