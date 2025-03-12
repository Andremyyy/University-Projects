//
// Created by ema_a on 5/19/2024.
//

#ifndef TONOMAT_DE_DULCIURI_MYEXCEPTION_H
#define TONOMAT_DE_DULCIURI_MYEXCEPTION_H

#include <exception>
using namespace std;

class MyException : public exception {
private:
    const char* message;
public:
    MyException(const char* m) : message(m){
    }
    const char* getMessage(){
        return message;
    }
};


#endif //TONOMAT_DE_DULCIURI_MYEXCEPTION_H
