//
// Created by ema_a on 3/18/2024.
//

#include "Rectangle.h"

#include "Rectangle.h"
#include <iostream>
#include <cmath>
using namespace std;

Rectangle::Rectangle(){
        this->x1=0;
        this->x2=0;
        this->y1=0;
        this->y2=0;
}
Rectangle::getx1() {
    return this->x1;
}

Rectangle::getx2(){
    return this->x2;
}

Rectangle::gety1(){
    return this->y1;
}

Rectangle::gety2(){
    return this->y2;
}

Rectangle::Rectangle(int a, int b, int c, int d) {
    this->x1 = a;
    this->y1 = b;
    this->x2 = c;
    this->y2 = d;
}
Rectangle::Rectangle(const Rectangle &r){
    this->x1=r.x1;
    this->y1=r.y1;
    this->x2=r.x2;
    this->y2=r.y2;
}

Rectangle::~Rectangle() {
//    cout<<"destructor for: "<<this->x1<<endl;
}

void Rectangle::setX1(int a){
    this->x1=a;
}

void Rectangle::setX2(int a){
    this->x2=a;
}

void Rectangle::setY1(int a){
    this->y1=a;
}

void Rectangle::setY2(int a){
    this->y2=a;
}

int Rectangle::detAria(){
    int L1=abs(this->x1-this->x2);
    int L2=abs(this->y1-this->y2);
    int A=L1*L2;
    return A;
}
double Rectangle::detSRA(){
    int L1=abs(this->x1-this->x2);
    int L2=abs(this->y1-this->y2);
    int A=L1*L2;
    return sqrt(A);
}



