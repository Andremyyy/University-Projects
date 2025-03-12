//
// Created by ema_a on 5/20/2024.
//

//
// Created by ema_a on 5/19/2024.
//
#include <exception>
using namespace std;

#ifndef TONOMAT_DE_DULCIURI_VALIDATOREXCEPTION_H
#define TONOMAT_DE_DULCIURI_VALIDATOREXCEPTION_H


class ValidatorException : public exception {
private:
    const char *message;
public:
    explicit ValidatorException(const char *m) : message(m){}

    const char *what() const noexcept override {
        return message;
    }

    const char *getMessage() const {
        return message;
    }
};

#endif //TONOMAT_DE_DULCIURI_VALIDATOREXCEPTION_H
