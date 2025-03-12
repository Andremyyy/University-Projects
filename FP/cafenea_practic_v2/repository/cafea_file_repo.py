from domain.cafea import Cafea
from exceptions.errors import RepoException


class CafeaFileRepo:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__cafele = {}

    def read_all_from_file(self):
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    return
                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                tara = parts[2]
                pret = float(parts[3])

                cafea = Cafea(id, nume, tara, pret)
                self.__cafele[(id,nume)] = cafea

    def print_all(self):
        self.read_all_from_file()
        return list(self.__cafele.values())

    def add_cafea(self, cafea):

        for (id, _) in self.__cafele:
            if cafea.get_id() == id:
                raise RepoException("O cafea cu acel id exista deja")

        for (_, nume) in self.__cafele:
            if cafea.get_nume() == nume:
                raise RepoException("O cafea cu acel nume exista deja")

        self.__cafele[(cafea.get_id(), cafea.get_nume())] = cafea

        with open(self.__filepath, 'a') as f:
            f.write(f"{cafea.get_id()},{cafea.get_nume()},{cafea.get_tara()},{cafea.get_pret()}\n")