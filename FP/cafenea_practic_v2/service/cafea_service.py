from domain.cafea import Cafea


class CafeaService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def print_all(self):
        return self.__repo.print_all()

    def filtreaza_tara(self, tara):
        """
        Creeaza o lista cu toate cafelele care au tara data
        :param tara: string
        :return: new_list (o lista) care contine toate cafelele care au tara data
                [], daca nu exista cafele cu tara data
        """
        cafele = self.__repo.print_all()

        new_list = []

        for cafea in cafele:
            if cafea.get_tara() == tara:
                new_list.append(cafea)

        return new_list

    def add_cafea(self, id, nume, tara, pret):

        cafea = Cafea(id, nume, tara, pret)
        self.__validator.validate(cafea)
        self.__repo.add_cafea(cafea)