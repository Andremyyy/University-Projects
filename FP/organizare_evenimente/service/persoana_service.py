from domain.enitities import Persoana


class PersoanaService:
    def __init__(self, file_repo, validator_persoana):
        self.__file_repo = file_repo
        self.__validator_persoana = validator_persoana

    def add_persoana(self, id, nume, adresa):
        persoana = Persoana(id, nume, adresa)
        self.__validator_persoana.validate(persoana)
        self.__file_repo.add_persoana(persoana)

    def get_persoane(self):
        return self.__file_repo.get_persoane()

    def delete_persoana(self, id):
        self.__file_repo.delete_persoana(id)

    def update_persoana(self, id, nume, adresa):
        persoana_noua = Persoana(id, nume, adresa)
        self.__validator_persoana.validate(persoana_noua)
        self.__file_repo.update_persoana(persoana_noua)

    def cautare_persoane(self, adresa):

        persoane = self.__file_repo.get_persoane()

        new_list_persoane_adresa = []

        for persoana in persoane:
            if persoana.get_adresa().strip() == adresa:
                new_list_persoane_adresa.append(persoana)

        return new_list_persoane_adresa
