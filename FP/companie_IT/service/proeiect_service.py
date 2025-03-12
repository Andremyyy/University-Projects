from domain.enitities import Proiect


class ProiectService:
    def __init__(self, file_repo, validator):
        self.__file_repo = file_repo
        self.__validator = validator

    def add_proiect(self, id, nume, numar_de_ore,buget_per_colaborator,nume_client):
        proiect = Proiect(id, nume, numar_de_ore, buget_per_colaborator, nume_client)
        self.__validator.validate(proiect)
        self.__file_repo.add_proiect(proiect)

    def print_proiecte(self):
        return self.__file_repo.print_proiecte()

    def sort_proiecte_dupa_ore(self):
        lista_nesortata = self.__file_repo.print_proiecte()

        lista_sortata = sorted(lista_nesortata, key = lambda x:x.get_numar_de_ore(), reverse = True)

        return lista_sortata

    def update_proiect(self,id,nume,numar_de_ore,buget_per_colaborator,nume_client):

        proiect_nou = Proiect(id, nume,numar_de_ore,buget_per_colaborator,nume_client)
        self.__validator.validate(proiect_nou)
        self.__file_repo.update_proiect(proiect_nou)

    def delete_proiect(self, id):
        self.__file_repo.delete_proiect(id)
