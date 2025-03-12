#include "io.h"
#include <iostream>
using namespace std;

void readArray(int &n, int *&x){
    /* Descr: Algoritmul citeste date de la tastura
     * In: n - un nr natural
     *     vectorul x de elemente naturale
     *Out:
     */
    cout << "Lungimea sirului este de: " << endl;
    cin >> n;
    x = new int[n];
    cout << "Sirul este:" << endl;
    for ( int i = 0; i < n; i++ )
        cin >> x[i];

}

void printRes(int v){
    /* Descr: Algoritmul afiseaza date
     * In: v- un nr natural
     *Out:
     */
    cout << "Valorea calculata este de: " << endl;
    cout << v;
}

void printSecv(int nr, int secv[]){
    /* Descr: Algoritmul afiseaza date
     * In: rn - un nr natural
     *     vectorul secv de elemente naturale
     *Out:
     */
    if (nr == 0)
        cout  << endl << "Nu exista numere";
    else {
        cout  << endl << "Valorile cautate sunt:" << endl;
        for (int i = 0; i < nr; i++)
            cout << secv[i] << endl;
    }
}