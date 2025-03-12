#ifndef TONOMAT_DE_DULCIURI_VALIDATOR_H
#define TONOMAT_DE_DULCIURI_VALIDATOR_H

#include "ValidatorException.h"
#include "Service.h" // Adaugă include-ul pentru Service
#include <iostream>
#include <cctype>
#include <set>
using namespace std;

class Validator {
public:
    static void validateCod(int cod){
        if (!cin)
            throw ValidatorException("Codul trebuie sa fie de tip int!");
        if (cod <= 0)
            throw ValidatorException("Codul trebuie sa fie strict mai mare decat 0!");
    }
    static void validateNume(string nume){
        if (!cin )
            throw ValidatorException("Numele trebuie sa fie de tip string!");
        if (nume.empty()) {
            throw ValidatorException("Numele trebuie sa existe!");
        }

        if(isdigit(nume[0]) != 0)
            throw ValidatorException("Numele nu trebuie sa inceapa cu cifra!");
    }
    static void validatePret(int pret){
        if (!cin )
        {
            throw ValidatorException("Pretul trebuie sa fie de tip int!");
//            throw exc;
        }
        if (pret <= 0)
            throw ValidatorException("Pretul trebuie sa fie strict mai mare decat 0!");
    }
    static void validateBancota(int banc){
        if (!cin )
            throw ValidatorException("Banconta trebuie sa fie de tip int!");
        if (banc < 1)
            throw ValidatorException("Bancnota trebuie sa fie mai mare decat 1!");
        set<int> bancnote = {1, 5, 10, 20, 50, 100, 200, 500};
        if (bancnote.find(banc) == bancnote.end()) {
            throw ValidatorException("Bancnota trebuie sa fie una din valorile: 1, 5, 10, 20, 50, 100, 200, 500!");
        }
    }
    static void validateValoare(int val){
        if (!cin )
            throw ValidatorException("Valoarea trebuie sa fie de tip int!");
        if (val < 1)
            throw ValidatorException("Valoarea trebuie sa fie mai mare decat 1!");
    }


};


#endif //TONOMAT_DE_DULCIURI_VALIDATOR_H
