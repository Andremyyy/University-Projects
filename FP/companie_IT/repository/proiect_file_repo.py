from domain.enitities import Proiect
from exceptions.erori import RepoException


class ProiectFileRepo:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__proiecte = {}

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self.__proiecte.clear()

            lines = f.readlines()

            for line in lines:
                line = line.strip()

                if line == "":
                    return

                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                numar_de_ore = int(parts[2])
                buget = int(parts[3])
                nume_client = parts[4]

                proiect = Proiect(id, nume, numar_de_ore,buget,nume_client)

                self.__proiecte[id] = proiect

    def add_proiect(self,proiect):

        self.__read_all_from_file()

        if proiect.get_id() in self.__proiecte:
            raise RepoException("id duplicat!")

        self.__proiecte[id] = proiect

        with open(self.__file_path, "a") as f:
            f.write(f"{proiect.get_id()},{proiect.get_nume()},{proiect.get_numar_de_ore()},{proiect.get_buget()},{proiect.get_nume_client()}\n")

    def print_proiecte(self):
        self.__read_all_from_file()
        return list(self.__proiecte.values())

    def __save_all_to_file(self):
        with open(self.__file_path, "w") as f:
            for proiect in list(self.__proiecte.values()):
                f.write(f"{proiect.get_id()},{proiect.get_nume()},{proiect.get_numar_de_ore()},{proiect.get_buget()},{proiect.get_nume_client()}\n")

    def __find_proiect_by_id(self,id):
        if id not in self.__proiecte:
            raise RepoException("Nu exista proiect cu id-ul dat!")
        return self.__proiecte[id]

    def update_proiect(self, proiect):
        if self.__find_proiect_by_id(proiect.get_id()) is None:
            raise RepoException("Nu exista proiect cu id-ul dat!")
        self.__proiecte[proiect.get_id()] = proiect
        self.__save_all_to_file()

    def delete_proiect(self,id):

        if self.__find_proiect_by_id(id) is None:
            raise RepoException("Nu exista proiect cu id-ul dat!")

        del self.__proiecte[id]
        self.__save_all_to_file()