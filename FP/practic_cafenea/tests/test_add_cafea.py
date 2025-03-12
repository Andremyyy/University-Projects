import unittest

from exceptions.erori import ValidatorException, RepoException
from repository.cafea_repo import CafeleRepo
from service.cafea_service import CafeleService
from validator.cafea_validator import CafeaValidator


class AddCafeaTestCase(unittest.TestCase):

    def setUp(self):

        self.__repo = CafeleRepo()
        self.__validator = CafeaValidator()
        self.__service = CafeleService(self.__repo, self.__validator)

    def test_add_cafea(self):
        # pentru CafeleService

        # pentru validare

        with self.assertRaises(ValidatorException):
            self.__service.add_cafele(10, "Tare", "Uruguay", -2)

        self.__service.add_cafele(10, "Tare", "Uruguay", 2)

        cafele = self.__repo.get_all_cafele()

        self.assertEqual(len(cafele), 6)

        self.__service.add_cafele(12, "Patura", "Italia", 2)
        self.__service.add_cafele(13, "Exista", "Franta", 1)

        # pentru id duplicat:
        with self.assertRaises(RepoException):
            self.__service.add_cafele(12, "Ceva", "Undeva", 3)
        # pentru nume duplicat
        with self.assertRaises(RepoException):
            self.__service.add_cafele(17, "Exista", "Undeva", 3)

        cafele = self.__repo.get_all_cafele()
        self.assertEqual(len(cafele), 8)


if __name__ == '__main__':
    unittest.main()
