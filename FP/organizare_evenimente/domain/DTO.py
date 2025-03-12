class InscriereDTO:
    def __init__(self, id_inscriere, id_persoana, id_eveniment, pret):
        self.__id_inscriere = id_inscriere
        self.__id_persoana = id_persoana
        self.__id_eveniment = id_eveniment
        self.__pret = pret

    def get_id_inscriere(self):
        return self.__id_inscriere
    def get_id_persoana(self):
        return self.__id_persoana
    def get_id_eveniment(self):
        return self.__id_eveniment
    def get_pret(self):
        return self.__pret

    def __str__(self):
        return f"{self.__id_inscriere} Inscrierea facuta de persoana cu id-ul: {self.__id_persoana} la evenimentul cu id-ul: {self.__id_eveniment} are pretul de: {self.__pret}"


class Top20EvenDTO:
    def __init__(self,id_eveniment, eveniment_data, eveniment_ora, eveniment_descriere, eveniment_numar_participanti):
        self.__id_eveniment = id_eveniment
        self.__eveniment_data = eveniment_data
        self.__eveniment_ora = eveniment_ora
        self.__eveniment_descriere = eveniment_descriere
        self.__eveniment_numar_participanti = eveniment_numar_participanti

    def get_id_eveniment(self):
        return self.__id_eveniment

    def get_data(self):
        return self.__eveniment_data

    def get_ora(self):
        return self.__eveniment_ora

    def get_descriere(self):
        return self.__eveniment_ora

    def get_numar_participanti(self):
        return self.__eveniment_numar_participanti

    def __str__(self):
        return f"La evenimentul {self.__id_eveniment} din data de {self.__eveniment_data} de la ora {self.__eveniment_ora} au fost {self.__eveniment_numar_participanti} de particpanti."


class Top3PersDTO:
    def __init__(self,id_persoana, persoana_nume, evenimente_persoana):
        self.__id_persoana = id_persoana
        self.__persoana_nume = persoana_nume
        self.__evenimente_persoana = evenimente_persoana

    def get_id_persoana(self):
        return self.__id_persoana

    def get_nume(self):
        return self.__persoana_nume

    def get_evenimente_persoana(self):
        return self.__evenimente_persoana

    def __str__(self):
        return f"{self.__id_persoana} {self.__persoana_nume} a participat la {self.__evenimente_persoana} evenimente."