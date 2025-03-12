import unittest

from service.cafea_service import CafeaService
from validator.cafea_validator import CafeaValidator


class FiltreazaTaraTestCase(unittest.TestCase):
    def setUp(self):
        self.__repo = "C:\\Users\\ema_a\\pythonProject\\cafenea_practic_v2\\tests\\teste.txt"
        self.__validator = CafeaValidator()
        self.__service =CafeaService(self.__repo, self.__validator)

    def test_filtrare_tara(self):
        tara_existenta = "Italia"
        cafele_italia = self.__service.filtreaza_tara(tara_existenta)
        self.assertEqual(cafele_italia, 1)

        tara_existenta_2 = "Franta"
        cafele_franta = self.__service.filtreaza_tara(tara_existenta_2)
        self.assertEqual(cafele_franta, 4)

if __name__ == '__main__':

    unittest.main()

