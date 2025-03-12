#include "C:\Users\ema_a\CLionProjects\lab2\Headers\io.h"
#include "C:\Users\ema_a\CLionProjects\lab2\Headers\test.h"
#include "C:\Users\ema_a\CLionProjects\lab2\Headers\utils.h"
#include <iostream>

using namespace std;

int main() {

    test_Sum();
    test_secv();
    int l = 0;
    int *a;
    readArray(l,a);
    int R = sum(l,a);
    printRes(R);

    int secv[4] = {0,0,0,0};
    int nr = 0;
    secventa_3_distincte(l, a, secv, nr);

    printSecv(nr, secv);

    if (a!= NULL){
        delete [] a;
    }

    return 0;
}


