class Persoana:
    def __init__(self, id, nume, adresa):
        self.__id = id
        self.__nume = nume
        self.__adresa = adresa

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def set_nume(self, nume):
        self.__nume = nume

    def set_adresa(self, adresa):
        self.__adresa = adresa

    def __str__(self):
        return f"{self.__id} {self.__nume} are adresa {self.__adresa}"


class Eveniment:
    def __init__(self, id, data, ora, descriere):
        self.__id = id
        self.__data = data
        self.__ora = ora
        self.__descriere = descriere

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_ora(self):
        return self.__ora

    def get_descriere(self):
        return self.__descriere

    def set_data(self, data):
        self.__data = data

    def set_ora(self, ora):
        self.__ora = ora

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def __str__(self):
        return f"{self.__id} Evenimentul din data de {self.__data} de la ora {self.__ora} are descrierea: {self.__descriere}"


class Inscriere:
    def __init__(self, id_inscriere, persoana, eveniment, pret):
        self.__id_inscriere = id_inscriere
        self.__persoana = persoana
        self.__eveniment = eveniment
        self.__pret = pret

    def get_id_inscriere(self):
        return self.__id_inscriere

    def get_persoana(self):
        return self.__persoana

    def get_eveniment(self):
        return self.__eveniment

    def get_pret(self):
        return self.__pret

    def __str__(self):
        return f"{self.__id_inscriere} Inscrierea realizata de {self.__persoana.get_nume()} la evenimentul {self.__eveniment.get_id()} are pretul de {self.__pret}"
