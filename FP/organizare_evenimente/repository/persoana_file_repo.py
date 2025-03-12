from domain.enitities import Persoana
from exceptions.erori import PersoanaRepoException


class PersoanaFileRepo:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__persoane = {}

    def __read_all_from_file(self):
        with open(self.__filepath, "r") as f:
            self.__persoane.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                adresa = parts[2]
                self.__persoane[id] = Persoana(id, nume, adresa)

    def add_persoana(self, persoana):
        if persoana.get_id() in self.__persoane:
            raise PersoanaRepoException("Duplicate id!")

        self.__persoane[persoana.get_id()] = persoana

        with open(self.__filepath, "a") as f:
            f.write(f"{persoana.get_id()}, {persoana.get_nume()}, {persoana.get_adresa()} \n")

    def get_persoane(self):
        self.__read_all_from_file()
        return list(self.__persoane.values())

    def get_persoane_fara_fisier(self):
        return list(self.__persoane.values())

    def gaseste_persoana_dupa_id(self, id):
        if id not in self.__persoane:
            raise PersoanaRepoException("Nu exista persoana cu id-ul dat.")
        return self.__persoane[id]

    def delete_persoana(self, id):
        # self.__read_all_from_file()

        if self.gaseste_persoana_dupa_id(id) is None:
            raise PersoanaRepoException("Nu exista persoana cu id-ul dat.")
        del self.__persoane[id]

        self.__save_all_to_file()

    def __save_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for persoana in self.get_persoane_fara_fisier():
                f.write(f"{persoana.get_id()}, {persoana.get_nume()}, {persoana.get_adresa()} \n")

    def update_persoana(self, persoana_noua):

        if self.gaseste_persoana_dupa_id(persoana_noua.get_id()) is None:
            raise PersoanaRepoException("Nu exista persoana cu id-ul dat.")

        self.__persoane[persoana_noua.get_id()] = persoana_noua

        self.__save_all_to_file()
