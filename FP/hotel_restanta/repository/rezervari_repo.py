from domain.entities import Rezervare
from exceptions.erori import RepoException


class RezervariRepo:
    def __init__(self, filepath):
        self.__rezervari = {}
        self.__filepath = filepath

    def add_rezervare(self, rezervare):

        if rezervare.get_id() in self.__rezervari:
            raise RepoException("Duplicate id!")

        self.__rezervari[rezervare.get_id()] = rezervare

        with open(self.__filepath, 'a') as f:
            f.write(f"{rezervare.get_id()}, {rezervare.get_tip()}, {rezervare.get_check_in_date()}, {rezervare.get_numar_zile()}")

    def get_all_rezervari(self):
        self.__read_all_from_file()
        return self.__rezervari.values()

    def __read_all_from_file(self):
        with open(self.__filepath, 'r') as f:
            self.__rezervari.clear()
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id = int(parts[0])
                    tip = parts[1]
                    check_in_date = int(parts[2])
                    numar_zile = int(parts[3])
                    rezervare = Rezervare(id, tip, check_in_date, numar_zile)
                    self.__rezervari[rezervare.get_id()] = rezervare
