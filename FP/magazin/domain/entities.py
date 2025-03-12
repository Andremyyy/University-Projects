class Produs:
    def __init__(self, id, nume, pret):
        self.__id = id
        self.__nume = nume
        self.__pret = pret

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_pret(self):
        return self.__pret

    def set_nume(self, other):
        self.__nume = other

    def set_pret(self, other):
        self.__pret = other

    def __str__(self):
        return f"{self.__id} Produsul: {self.__nume} are pretul de: {self.__pret}"

class Battery(Produs):
    def __init__(self, id, nume, pret, rechargeable):
        super().__init__(id, nume, pret)
        self.__rechargeable = rechargeable

    def get_rechargeable(self):
        return self.__rechargeable

    def set_rechargeable(self, other):
        self.__rechargeable = other

    def __str__(self):
        return f"{self.get_id()} Produsul {self.get_nume()} are pretul de:{self.get_pret()} si valoarea de rechargeable: {self.__rechargeable}"