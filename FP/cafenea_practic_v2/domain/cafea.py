class Cafea:
    def __init__(self, id, nume, tara, pret):
        self.__id = id
        self.__nume = nume
        self.__tara = tara
        self.__pret = pret

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_tara(self):
        return self.__tara

    def get_pret(self):
        return self.__pret

    def __str__(self):
        return f"{self.__id} {self.__nume} este din {self.__tara} si are pretul de {self.__pret}"