import unittest

from domain.entities import Cafea
from domain.validator import CafeaValidator
from exceptions.erori import RepoException, ValidatorException
from repository.cafea_file_repo import CafeaFileRepo
from service.cafea_service import CafeaService


class AddCafeaTestCase(unittest.TestCase):

    def setUp(self):
        file_test = "C:\\Users\\ema_a\\pythonProject\\cafenea_altul\\tests\\add_cafea_test"
        self.__file_repo = CafeaFileRepo(file_test)
        self.__validator = CafeaValidator()
        self.__service = CafeaService(self.__file_repo, self.__validator)

    def test_add_cafea(self):

        id = 11
        nume = "Espesso Lung"
        tara_de_origine = "Spania"
        pret = 15.9

        self.__service.add_cafea(id, nume, tara_de_origine,pret)

        lista = self.__service.get_all_cafele()

        self.assertEqual(len(lista), 7)

        id_invalid = 3

        with self.assertRaises(RepoException):
            self.__service.add_cafea(id_invalid, nume, tara_de_origine, pret)

        pret_invalid = -6.8
        with self.assertRaises(ValidatorException):
            self.__service.add_cafea(13, nume, tara_de_origine, pret_invalid)

    def test_delete_cafea(self):

        id = 11

        lista = self.__service.get_all_cafele()

        self.assertEqual(len(lista), 7)

        self.__service.delete_cafea(id)

        lista = self.__service.get_all_cafele()

        self.assertEqual(len(lista), 6)

        with self.assertRaises(RepoException):
            self.__service.delete_cafea(id)

    def teste_update_cafea(self):

        id = 11
        nume = "Noua"
        tara = "Tara Noua"
        pret = 15

        with self.assertRaises(RepoException):
            self.__service.update_cafea(id, nume, tara, pret)

if __name__ == '__main__':
    unittest.main()