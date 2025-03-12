class Student:
    def __init__(self, id, nume, numar_prezente, nota):
        self.__id = id
        self.__nume = nume
        self.__numar_prezente = numar_prezente
        self.__nota = nota

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_numar_prezente(self):
        return self.__numar_prezente

    def get_nota(self):
        return self.__nota

    def __str__(self):
        return f"{self.__id} {self.__nume} are {self.__numar_prezente} prezente si nota {self.__nota}."
