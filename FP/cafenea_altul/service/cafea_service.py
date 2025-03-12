from domain.entities import Cafea
from exceptions.erori import RepoException


class CafeaService:
    def __init__(self, file_repo, validator):
        self.__cafea_file_repo = file_repo
        self.__cafea_validator = validator

    def add_cafea(self, id, nume, tara_de_origine, pret):
        cafea = Cafea(id, nume, tara_de_origine, pret)
        self.__cafea_validator.validate(cafea)
        self.__cafea_file_repo.add_cafea(cafea)

    def get_all_cafele(self):
        return self.__cafea_file_repo.get_all_cafele()

    def cresc_dupa_tara_si_pret(self):

        lista_nesortata = self.__cafea_file_repo.get_all_cafele()

        lista_sortata = sorted(lista_nesortata, key = lambda x: (x.get_tara_de_origine(), x.get_pret()))

        return lista_sortata

    def filtrati_dupa_tara_si_pret(self, tara, pret):

        lista_initiala = self.__cafea_file_repo.get_all_cafele()

        rezultat = []

        for cafea in lista_initiala:
            if cafea.get_tara_de_origine() == tara and cafea.get_pret() <= pret:
                rezultat.append(cafea)

        return rezultat

    def filtrati_dupa_pret(self, pret):
        lista_initiala = self.__cafea_file_repo.get_all_cafele()

        rezultat = []
        for cafea in lista_initiala:
            if cafea.get_pret() <= pret:
                rezultat.append(cafea)

        return rezultat

    def filtrati_dupa_tara(self, tara):
        lista_initiala = self.__cafea_file_repo.get_all_cafele()

        rezultat = []
        for cafea in lista_initiala:
            if cafea.get_tara_de_origine() == tara:
                rezultat.append(cafea)

        return rezultat

    def update_cafea(self, id, nume, tara, pret):

        cafea = Cafea(id, nume, tara, pret)
        self.__cafea_validator.validate(cafea)
        self.__cafea_file_repo.update_cafea(cafea)

    def delete_cafea(self, id):

        self.__cafea_file_repo.delete_cafea(id)

    def update_cafea_cu_tara_data(self,tara):

        lista = self.__find_cafea_cu_tara(tara)

        for cafea in lista:
            new_tara = cafea.get_tara_de_origine().upper()
            new_pret = cafea.get_pret() * 2
            cafea = Cafea(cafea.get_id(), cafea.get_nume(), new_tara, new_pret)
            self.__cafea_file_repo.update_cafea(cafea)

    def __find_cafea_cu_tara(self, tara):
        lista_totala = self.__cafea_file_repo.get_all_cafele()
        result = []
        for cafea in lista_totala:
            if cafea.get_tara_de_origine().strip() == tara:
                result.append(cafea)
        if not result:
            raise RepoException("nu avem cafele cu tara data!")

        return result
