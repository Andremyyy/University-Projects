#include "C:\Users\ema_a\CLionProjects\lab2\Headers\utils.h"
#include <iostream>
using namespace std;

int sum(int n, int x[]){
    /* Descr: Algoritmul calculeaza suma elementelor unui vector
     * In: n - un nr natural
     *     vectorul x de elemente naturale
     *Out: s - suma elementelor vectororului x
     */
    int s = 0;
    for ( int i = 0; i < n; i++ )
        s += x[i];

    return s;
}

//void secventa_3_distincte(int n, int x[], int maxsecv[], int &maxnr) {
//    int j = 0;
//    int nr = 0;
//    int prim = x[0];
//    maxnr = -1;
//    int secv[4] = {0, 0, 0, 0};
//
//    if (n == 1) {
//        maxsecv[0] = x[0];
//        maxnr = 1;
//    } else {
//        for (int i = 1; i < n; i++) {
//            if (x[i] != prim) {
//                secv[j] = prim;
//                secv[j + 1] = x[i];
//                prim = x[i];
//                j++;
//                nr += 2;
//            } else if (nr == 0) {
//                prim = x[i];
//            } else {
//                if (nr != 2)
//                    nr--;
//                if (nr > maxnr) {
//                    maxnr = nr;
//                    for (int i = 0; i < maxnr; i++)
//                        maxsecv[i] = secv[i];
//                }
//                if (nr == 3 || maxnr == 3)
//                    break;
//                nr = 0;
//                j = 0;
//                for (int i = 0; i < 4; i++)
//                    secv[i] = 0;
//            }
//        }
//        if (nr != 2)
//            nr--;
//        if (nr > maxnr) {
//            maxnr = nr;
//            for (int i = 0; i < maxnr; i++)
//                maxsecv[i] = secv[i];
//        }
//    }
//}

void secventa_3_distincte(int n, int x[], int maxsecv[], int &maxnr) {
    /* Descr: Algoritmul calculeaza secventa de lungime maxina de 3 elemente distincte
     * In: n - un nr natural
     *     vectorul x de elemente naturale
     *     maxsecv- un vector
     *     maxnr - un nr natural
     *Out: in maxsecv calculeaza secventa cautata, iar maxnr va contine nr de elemente din secventa maxima
     */
    maxnr = 0; // Lungimea maximă a secvenței
    int count = 0; // Numărul de elemente distincte din secvență
    int start_index = 0; // Indexul de început al secvenței curente
    int max_start_index = 0; // Indexul de început al secvenței maxime
    int max_length = 0; // Lungimea secvenței maxime

    for (int i = 0; i < n; i++) {
        bool found = false; // Verificăm dacă elementul curent a fost găsit deja în secvență

        // Verificăm dacă elementul curent a fost găsit anterior în secvență
        for (int j = start_index; j < i; j++) {
            if (x[j] == x[i]) {
                found = true;
                start_index = j + 1; // Actualizăm indexul de început al secvenței
                count = i - j - 1; // Actualizăm numărul de elemente distincte
                break;
            }
        }

        if (!found) {
            count++; // Incrementăm numărul de elemente distincte
        }

        // Verificăm dacă avem o secvență cu cel mult 3 elemente distincte
        if (count <= 3) {
            // Actualizăm lungimea și indexul secvenței maxime
            int length = i - start_index + 1;
            if (length > max_length && length <= 3) {
                max_length = length;
                max_start_index = start_index;
            }
        }
        else {
            // Resetăm start_index și count pentru a căuta o nouă secvență
            start_index = i - 1;
            count = 1;
        }
    }

    // Copiem secvența maximă în maxsecv
    maxnr = max_length;
    for (int i = 0; i < maxnr; i++) {
        maxsecv[i] = x[max_start_index + i];
    }
}