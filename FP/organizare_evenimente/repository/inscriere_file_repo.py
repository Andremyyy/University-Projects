from domain.DTO import InscriereDTO
from exceptions.erori import InscriereRepoException


class InscriereFileRepo:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__inscrieri = {}

    def add_inscriere(self, inscriere):

        if inscriere.get_id_inscriere() in self.__inscrieri:
            raise InscriereRepoException("id existent")
        self.__inscrieri[inscriere.get_id_inscriere()] = inscriere
        with open(self.__file_path, 'a') as f:
            f.write(
                f"{inscriere.get_id_inscriere()},{inscriere.get_id_persoana()},{inscriere.get_id_eveniment()},{inscriere.get_pret()}\n")

    def __read_all_from_file(self):
        # trebuie folosit inscriereDTO in care am id_inscriere, id_persoana, id_eveniemnt si pret
        # in fisier tin doar id-urile
        with open(self.__file_path, "r") as f:
            self.__inscrieri.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id_inscriere = int(parts[0])
                id_persoana = int(parts[1])
                id_eveniment = int(parts[2])
                pret = int(parts[3])

                # fac un obiect de tip DTO!!!
                inscriere = InscriereDTO(id_inscriere, id_persoana, id_eveniment, pret)

                self.__inscrieri[id_inscriere] = inscriere

    def get_inscrieri(self):
        self.__read_all_from_file()
        return list(self.__inscrieri.values())
