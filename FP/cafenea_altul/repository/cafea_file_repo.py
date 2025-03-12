from domain.entities import Cafea
from exceptions.erori import RepoException


class CafeaFileRepo:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__cafele = {}

    def add_cafea(self, cafea):

        self.__read_all_from_file()
        if cafea.get_id() in self.__cafele:
            raise RepoException("id duplicat!")

        self.__cafele[cafea.get_id()] = cafea

        with open(self.__file_path, "a") as f:
            f.write(f"{cafea.get_id()}, {cafea.get_nume()}, {cafea.get_tara_de_origine()}, {cafea.get_pret()} \n")

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self.__cafele.clear()
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                if line == "":
                    return
                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                tara_de_origine = parts[2]
                pret = float(parts[3])

                cafea = Cafea(id, nume, tara_de_origine, pret)

                self.__cafele[id] = cafea

    def get_all_cafele(self):
        self.__read_all_from_file()
        return list(self.__cafele.values())

    def update_cafea(self, cafea):

        if self.__find_cafea_by_id(cafea.get_id()) is None:
            raise RepoException("nu exista cafea cu id-ul dat!!")

        self.__cafele[cafea.get_id()] = cafea

        self.__save_all_to_file()

    def __find_cafea_by_id(self, id):
        if id not in self.__cafele:
            raise RepoException("nu exista cafea cu id-ul dat!!")
        return self.__cafele[id]

    def __save_all_to_file(self):
        with open(self.__file_path, "w") as f:
            for cafea in list(self.__cafele.values()):
                f.write(f"{cafea.get_id()}, {cafea.get_nume()}, {cafea.get_tara_de_origine()}, {cafea.get_pret()} \n")

    def delete_cafea(self, id):
        if self.__find_cafea_by_id(id) is None:
            raise RepoException("Nu exista cafele cu id-ul dat!")

        del self.__cafele[id]

        self.__save_all_to_file()