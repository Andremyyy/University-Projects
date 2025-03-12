from domain.entities import Produs


class ProdusService:
    def __init__(self, produs_file_repo, produs_validator):
        self.__produs_file_repo = produs_file_repo
        self.__produs_validator = produs_validator

    def show_products(self):
       return self.__produs_file_repo.show_products()

    def save(self, id, nume, pret):

        produs = Produs(id, nume, pret)
        self.__produs_validator.validate(produs)
        self.__produs_file_repo.save(produs)

    def delete_produs(self, id):
        self.__produs_file_repo.delete_produs(id)

    def update_produs(self, id, nume_nou, pret_nou):
        produs_nou = Produs(id, nume_nou, pret_nou)
        self.__produs_validator.validate(produs_nou)
        self.__produs_file_repo.update_produs(produs_nou)
