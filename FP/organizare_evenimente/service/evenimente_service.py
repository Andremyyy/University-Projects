from domain.enitities import Eveniment


class EvenimentService:
    def __init__(self, evenimente_file_repo, evenimente_valiodator):
        self.__evenimente_file_repo = evenimente_file_repo
        self.__evenimente_validator = evenimente_valiodator

    def add_eveniment(self, id, data, ora, descriere):

        eveniment = Eveniment(id, data, ora, descriere)

        self.__evenimente_validator.validate(eveniment)

        self.__evenimente_file_repo.add_eveniment(eveniment)

    def get_evenimente(self):
        return self.__evenimente_file_repo.get_evenimente()

    def delete_eveniment(self, id):
        self.__evenimente_file_repo.delete_eveniment(id)

    def update_eveniment(self, id, data, ora, descriere):

        eveniment_nou = Eveniment(id, data, ora, descriere)

        self.__evenimente_validator.validate(eveniment_nou)

        self.__evenimente_file_repo.update_eveniment(eveniment_nou)

    def cautare_evenimente_dupa_data(self, data):

        evenimente = self.__evenimente_file_repo.get_evenimente()

        new_list_evenimente = []

        for eveniment in evenimente:
            if eveniment.get_data().strip() == data:
                new_list_evenimente.append(eveniment)

        return new_list_evenimente
