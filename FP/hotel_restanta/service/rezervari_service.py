from domain.entities import Rezervare
from exceptions.erori import RepoException


class RezervariService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def get_all_rezervari(self):
        return self.__repo.get_all_rezervari()

    def add_rezervare(self, id, tip, check_in, numar_zile):

        rezervare = Rezervare(id, tip, check_in, numar_zile)
        self.__validator.validate(rezervare)

        check_out = check_in + numar_zile
        if check_out > 31:
            raise RepoException("Rezervarea nu s-a putut efectua! Nicio camera de tipul introdus nu este disponibila in intervalul specificat!")

        self.__repo.add_rezervare(rezervare)

        rezervari = self.get_all_rezervari()

        for rezervare in rezervari:
            if rezervare.get_tip() == rezervari.get_tip():
                pass