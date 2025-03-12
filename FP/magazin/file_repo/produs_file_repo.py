from domain.entities import Produs
from exceptions.erori import RepoException


class ProdusFileRepo:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__produse = {}

    def show_products(self):
        self.__read_all_from_file()
        return list(self.__produse.values())

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self.__produse.clear()
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                pret = float(parts[2])

                produs = Produs(id, nume, pret)
                self.__produse[id] = produs

    def save(self, produs):

        self.__read_all_from_file()
        if produs.get_id() in self.__produse:
            raise RepoException("id duplicat")

        self.__produse[id] = produs

        with open(self.__file_path, 'a') as f:
            f.write(f"{produs.get_id()},{produs.get_nume()},{produs.get_pret()} \n")

    def delete_produs(self,id):

        if self.__find_produs_by_id(id) is None:
            raise RepoException("NU EXISTA PRODUS CU ID-UL DAT")
        del self.__produse[id]
        self.__save_all_to_file()

    def __find_produs_by_id(self, id):
        if id not in self.__produse:
            raise RepoException("nu exista produse cu id-ul dat!")
        return self.__produse[id]

    def __save_all_to_file(self):
        with open(self.__file_path, "w") as f:
            for produs in self.__produse.values():
                f.write(f"{produs.get_id()},{produs.get_nume()},{produs.get_pret()} \n")

    def update_produs(self, produs_nou):

        if self.__find_produs_by_id(produs_nou.get_id()) is None:
            raise RepoException("NU EXISTA PRODUS CU ID-UL DAT!")

        self.__produse[produs_nou.get_id()] = produs_nou

        self.__save_all_to_file()
