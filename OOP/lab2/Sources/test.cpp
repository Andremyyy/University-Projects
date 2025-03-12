#include <assert.h>
#include <iostream>
using namespace std;
#include "C:\Users\ema_a\CLionProjects\lab2\Headers\test.h"
#include "C:\Users\ema_a\CLionProjects\lab2\Headers\utils.h"

void test_Sum(){
//    int a[3] = {7,9,1};
//    assert(sum(a,3) == 17);
//    a[0]=0;
//    a[1] = 0;
//    a[2] = 0;
//    assert(sum(a,3) == 0);
}

void test_secv(){
    int a[5] = {0,1,2,3,4};
    int secv[4];
    int nr;
    secventa_3_distincte(3, a, secv, nr);
    assert(secv[0] == 0);
    assert(secv[1] == 1);
    assert(secv[2] == 2);
    assert (nr == 3);
    a[0] = 1;
    secventa_3_distincte(1, a, secv, nr);
    assert(nr == 1);
    assert (secv[0] == 1);
    a[0] = 1;
    a[1] = 1;
    a[2] = 1;
    a[3] = 1;
    a[4] = 2;
    secventa_3_distincte(5, a, secv, nr);
    assert(nr == 2);
    assert (secv[0] == 1);
    assert (secv[1] == 2);

    a[0] = 1;
    a[1] = 1;
    a[2] = 1;
    a[3] = 1;
    a[4] = 1;

    secventa_3_distincte(5, a, secv, nr);
    assert(nr == 1);
    assert (secv[0] == 1);

    int x[6];
    x[0] = 1;
    x[1] = 2;
    x[2] = 1;
    x[3] = 1;
    x[4] = 2;
    x[5] = 1;
    secventa_3_distincte(6, x, secv, nr);
    assert(nr == 2);
    assert (secv[0] == 1);
    assert (secv[1] == 2);

    x[0] = 1;
    x[1] = 1;
    x[2] = 1;
    x[3] = 1;
    x[4] = 1;
    x[5] = 1;
    secventa_3_distincte(6, x, secv, nr);
    assert(nr == 1);
    x[0] = 1;
    x[1] = 2;
    x[2] = 3;
    x[3] = 3;
    x[4] = 2;
    x[5] = 1;
    secventa_3_distincte(6, x, secv, nr);
    assert(nr == 3);
    int v[10];
    v[0] = 1;
    v[1] = 2;
    v[2] = 3;
    v[3] = 4;
    v[4] = 4;
    v[5] = 1;
    v[6] = 2;
    v[7] = 3;
    v[8] = 5;
    v[9] = 4;

    secventa_3_distincte(10, v, secv, nr);

    assert(nr == 3);

}