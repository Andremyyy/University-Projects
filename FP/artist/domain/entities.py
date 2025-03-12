class Artist:
    def __init__(self, id, nume, categorie, tarif):
        self.__id = id
        self.__nume = nume
        self.__categorie = categorie
        self.__tarif = tarif

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_categorie(self):
        return self.__categorie

    def get_tarif(self):
        return self.__tarif

    def __str__(self):
        return f"{self.__id} Artistul: {self.__nume} este din categoria: {self.__categorie} si are un tarif de: {self.__tarif}"