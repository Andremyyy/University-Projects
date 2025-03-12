from domain.enitities import Eveniment
from exceptions.erori import EvenimentRepoException


class EvenimentFileRepo:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__evenimente = {}

    def __read_all_from_file(self):
        with open(self.__filepath, 'r') as f:
            self.__evenimente.clear()
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                data = parts[1]
                ora = parts[2]
                descriere = parts[3]
                eveniment = Eveniment(id, data, ora, descriere)
                self.__evenimente[id] = eveniment

    def add_eveniment(self, eveniment):

        if eveniment.get_id() in self.__evenimente:
            raise EvenimentRepoException("Duplicate id!")
        self.__evenimente[eveniment.get_id()] = eveniment

        with open(self.__filepath, "a") as f:
            f.write(f"{eveniment.get_id()}, {eveniment.get_data()}, {eveniment.get_ora()}, {eveniment.get_descriere()} \n")

    def find_eveniment_by_id(self, id):
        if id not in self.__evenimente:
            raise EvenimentRepoException("Nu exista evenimente cu id-ul respectiv")
        return self.__evenimente[id]

    def get_evenimente(self):
        self.__read_all_from_file()
        return list(self.__evenimente.values())

    def __save_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for eveniment in self.__get_evenimente_fara_fisier():
                f.write(f"{eveniment.get_id()}, {eveniment.get_data()}, {eveniment.get_ora()}, {eveniment.get_descriere()} \n")

    def delete_eveniment(self, id):

        if self.find_eveniment_by_id(id) is None:
            raise EvenimentRepoException("Nu exista evenimente cu id-ul dat!")

        del self.__evenimente[id]

        self.__save_all_to_file()

    def __get_evenimente_fara_fisier(self):
        return list(self.__evenimente.values())

    def update_eveniment(self, eveniment_nou):

        if self.find_eveniment_by_id(eveniment_nou.get_id()) is None:
            raise EvenimentRepoException("Nu exista evenimente cu id-ul dat!")
        self.__evenimente[eveniment_nou.get_id()] = eveniment_nou
        self.__save_all_to_file()
