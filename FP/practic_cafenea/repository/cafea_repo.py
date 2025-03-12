from domain.entities import Cafea
from exceptions.erori import RepoException


class CafeleRepo:
    def __init__(self):
        self.__cafele = {
            (1, "Capuccino"): Cafea(1, "Capuccino", "Italia", 12),
            (3, "Americano"): Cafea(3, "Americano", "Franta", 14),
            (4, "Flat White"): Cafea(4, "Flat White", "Italia", 18),
            (6, "Espresso Lung"): Cafea(6, "Espresso Lung", "Franta", 1),
            (9, "Iced Coffee"): Cafea(9, "Iced Coffee", "Germania", 5)
        }

    def add_cafea(self, cafea):
        """
        Verifica daca id-ul si numele sunt unice.
        Daca da, adauga cafea in dictionarul __cafele
        :param cafea: un obiect de tip Cafea
        :return: None
        :raises: RepoException daca id-ul este existent
                RepoException daca numele este existent
        """
        for (id, _) in self.__cafele:
            if cafea.get_id() == id:
                raise RepoException("Duplicate id!")

        for (_, nume) in self.__cafele:
            if cafea.get_nume() == nume:
                raise RepoException("Duplicate name!")

        self.__cafele[(cafea.get_id(), cafea.get_nume())] = cafea

    def get_all_cafele(self):
        return self.__cafele.values()