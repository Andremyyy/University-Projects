class Proiect:
    def __init__(self, id, nume, numar_de_ore, buget, nume_client):
        self.__id = id
        self.__nume = nume
        self.__numar_de_ore = numar_de_ore
        self.__buget = buget
        self.__nume_client = nume_client

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_numar_de_ore(self):
        return self.__numar_de_ore

    def get_buget(self):
        return self.__buget

    def get_nume_client(self):
        return self.__nume_client

    def __str__(self):
        return f"{self.__id} Proiectul: {self.__nume} are {self.__numar_de_ore} de ore, un buget egal cu:  {self.__buget} si este realizat de clientul: {self.__nume_client}"