//
// Created by ema_a on 3/25/2024.
//

#ifndef LAB4_UTILS_H
#define LAB4_UTILS_H

#include "Rectangle.h"
#include <vector>

using namespace std;

void read(vector <Rectangle>& x, int &n);
void print(vector <Rectangle>& x, int n);
void determinare_cea_mai_mare(vector <Rectangle>& x, int n, Rectangle &sol);
void afisare_sol (Rectangle &sol);
bool isInFirstQuadrant(Rectangle sol);
void afisare_first_qudrant( bool rez, Rectangle sol);

int longestEqualSequence(vector <Rectangle>& entities, int size, int &l, int &s, int &d);

#endif //LAB4_UTILS_H
