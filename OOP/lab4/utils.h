//
// Created by ema_a on 3/25/2024.
//

#ifndef LAB4_UTILS_H
#define LAB4_UTILS_H

#include "Rectangle.h"


void read(Rectangle x[], int &n);
void print(Rectangle x[], int n);
void determinare_cea_mai_mare(Rectangle x[], int n, Rectangle &sol);
void afisare_sol (Rectangle &sol);
bool isInFirstQuadrant(Rectangle sol);
void afisare_first_qudrant( bool rez, Rectangle sol);

int longestEqualSequence(Rectangle entities[], int size);

#endif //LAB4_UTILS_H
