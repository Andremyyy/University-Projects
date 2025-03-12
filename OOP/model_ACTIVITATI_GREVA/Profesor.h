//
// Created by ema_a on 6/1/2024.
//

#ifndef MODEL_ACTIVITATI_GREVA_PROFESOR_H
#define MODEL_ACTIVITATI_GREVA_PROFESOR_H

//În școală activează mai mulți profesori pentru care se cunosc numele,
//disciplina predată și clasele la care predau, precum și faptul că sunt sau nu în grevă.
#include "string"
#include "vector"
#include "iostream"
using namespace std;
class Profesor {
private:
    string nume;
    string disciplina;
    vector<string> clase;
    bool inGreva;
public:
    Profesor(string nume, string disciplina, vector<string> clase, bool inGreva) : nume(nume), disciplina(disciplina), clase(clase), inGreva(inGreva) {}

    Profesor(){
        this->nume = "";
        this->disciplina = "";
        this->inGreva = false;
    }

    Profesor(const Profesor& profesor) {
        this->nume = profesor.nume;
        this->disciplina = profesor.disciplina;
        this->clase = profesor.clase;
        this->inGreva = profesor.inGreva;
    }

    bool operator ==(const Profesor& profesor){
        return (this->nume == profesor.nume && this->disciplina == profesor.disciplina && this->clase == profesor.clase && this->inGreva == profesor.inGreva);
    }

    Profesor operator =(const Profesor& profesor){
        this->nume = profesor.nume;
        this->disciplina = profesor.disciplina;
        this->clase = profesor.clase;
        this->inGreva = profesor.inGreva;
        return *this;
    }

    bool operator !=(const Profesor& profesor){
        return !(this->nume == profesor.nume && this->disciplina == profesor.disciplina && this->clase == profesor.clase && this->inGreva == profesor.inGreva);
    }

    ostream &operator <<(ostream &os){
        os<<this->nume<<" "<<this->disciplina;
        for (string clasa : this->clase) {
            os << " " << clasa;
        }
        os << " "<<this->inGreva;
        return os;
    }

    void setNume(string nume){
        this->nume = nume;
    }

    void setDisciplina(string disciplina){
        this->disciplina = disciplina;
    }

    void setClase(vector<string> clase){
        this->clase = clase;
    }

    void setInGreva(bool inGreva){
        this->inGreva = inGreva;
    }

    string getNume(){
        return this->nume;
    }

    string getDisciplina(){
        return this->disciplina;
    }

    vector<string> getClase(){
        return this->clase;
    }

    bool getInGreva(){
        return this->inGreva;
    }

    ~Profesor(){
        this->nume = "";
        this->disciplina = "";
        this->clase.clear();
        this->inGreva = false;
    }
};


#endif //MODEL_ACTIVITATI_GREVA_PROFESOR_H
