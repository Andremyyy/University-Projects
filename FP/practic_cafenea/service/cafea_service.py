from domain.entities import Cafea


class CafeleService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add_cafele(self, id, nume, tara_de_origine, pret):
        """
        Creeaza o un obiect de tip Cafea si il valideaza
        :param id: int
        :param nume: string
        :param tara_de_origine: string
        :param pret: float
        :return: None
        """
        cafea = Cafea(id, nume, tara_de_origine, pret)
        self.__validator.validate(cafea)
        self.__repo.add_cafea(cafea)

    def get_all_cafele(self):
        return self.__repo.get_all_cafele()

    def get_cafele_dupa_tara(self):
        cafele = self.__repo.get_all_cafele()
        sorted_cafele = sorted(cafele, key=lambda cafea: (cafea.get_tara_de_origine(), cafea.get_pret()))
        return sorted_cafele

    def get_cafele_filtrate(self, tara, pret):
        cafele = self.__repo.get_all_cafele()
        cafele_filtrate = [cafea for cafea in cafele if
                           cafea.get_tara_de_origine() == tara and cafea.get_pret() <= pret]
        return cafele_filtrate

    def get_cafele_dupa_pret(self, pret):
        cafele = self.__repo.get_all_cafele()
        cafele_filtrate = [cafea for cafea in cafele if cafea.get_pret() <= float(pret)]
        return cafele_filtrate

    def filtreaza_cafele_tara(self, tara):
        cafele = self.__repo.get_all_cafele()
        cafele_filtrate = [cafea for cafea in cafele if cafea.get_tara_de_origine() == tara]
        return cafele_filtrate
