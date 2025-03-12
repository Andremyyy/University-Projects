class Cafea:
    def __init__(self, id, nume, tara_de_origine, pret):
        self.__id = id
        self.__nume = nume
        self.__tara_de_origine = tara_de_origine
        self.__pret = pret

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_tara_de_origine(self):
        return self.__tara_de_origine

    def get_pret(self):
        return self.__pret


    def __str__(self):
        return f"{self.__id} Cafeaua: {self.__nume} este din {self.__tara_de_origine} si are pretul: {self.__pret}"