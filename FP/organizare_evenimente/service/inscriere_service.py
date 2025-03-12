import math

from domain.DTO import InscriereDTO, Top20EvenDTO, Top3PersDTO
from domain.enitities import Inscriere


class InscriereService:
    def __init__(self, inscriere_file_repo, inscriere_validator, persoana_file_repo, eveniment_file_repo):
        self.__inscriere_file_repo = inscriere_file_repo
        self.__inscriere_validator = inscriere_validator
        self.__persoana_file_repo = persoana_file_repo
        self.__eveniment_file_repo = eveniment_file_repo

    def add_inscriere(self, id_inscriere, id_persoana, id_eveniment, pret):

        # prima data verific daca exista PERSOANA si EVENIMENTUL:
        self.__persoana_file_repo.gaseste_persoana_dupa_id(id_persoana)
        self.__eveniment_file_repo.find_eveniment_by_id(id_eveniment)

        # daca trece de liniile precedente fara sa arunce eroare => am persoana si evenimentul pentru care vreau sa adaug o inchiriere

        inscriere = InscriereDTO(id_inscriere, id_persoana, id_eveniment, pret)

        # validez:
        self.__inscriere_validator.validate(inscriere)
        self.__inscriere_file_repo.add_inscriere(inscriere)

    def get_inscrieri(self):
        inscrieri_dtos = self.__inscriere_file_repo.get_inscrieri()
        result = []
        for inscriere_dto in inscrieri_dtos:
            persoana = self.__persoana_file_repo.gaseste_persoana_dupa_id(inscriere_dto.get_id_persoana())
            eveniment = self.__eveniment_file_repo.find_eveniment_by_id(inscriere_dto.get_id_eveniment())
            inscriere = Inscriere(inscriere_dto.get_id_inscriere(), persoana, eveniment, inscriere_dto.get_pret())
            result.append(inscriere)
        return result

    def evenimente_persoana_dupa_descriere(self, id_persoana):

        #todo:nu stiu cum se face!

        # evenimnete_per_persoana = {}
        #
        # inscrieri_dtos = self.__inscriere_file_repo.get_inscrieri()
        #
        # for inscriere in inscrieri_dtos:
        #     id_participant = inscriere.get_id_persoana()
        #     if id_participant not in evenimnete_per_persoana:
        #         evenimnete_per_persoana[id_participant] = []
        #     evenimnete_per_persoana[id_participant].append(inscriere.get_id_eveniment)
        #
        # print(inscrieri_dtos)
        pass

    def top_20_evenimente(self):

        toti_partic_even = self.__calculate_toti_participanti_per_eveniment()

        result = []

        for id_eveniment in toti_partic_even:
            eveniment_numar_participanti = toti_partic_even[id_eveniment]

            eveniment_data = self.__eveniment_file_repo.find_eveniment_by_id(id_eveniment).get_data()
            eveniment_ora = self.__eveniment_file_repo.find_eveniment_by_id(id_eveniment).get_ora()
            eveniment_descriere = self.__eveniment_file_repo.find_eveniment_by_id(id_eveniment).get_descriere()

            top_20_evenimente_dto = Top20EvenDTO(id_eveniment, eveniment_data, eveniment_ora, eveniment_descriere,
                                                 eveniment_numar_participanti)
            result.append(top_20_evenimente_dto)

        result.sort(key=lambda x: x.get_numar_participanti(), reverse=True)

        top_20_evenimente_index = math.ceil(len(result) * 0.2)

        return result[:top_20_evenimente_index]

    def top_3_pers_part(self):
        toate_evenimentele_per_participant = self.__calculate_toate_evenimentele_per_participant()
        result = []

        for id_persoana in toate_evenimentele_per_participant:
            nr_evenimente_persoana = toate_evenimentele_per_participant[id_persoana]
            persoana_nume = self.__persoana_file_repo.gaseste_persoana_dupa_id(id_persoana).get_nume()

            top_3_pers_dto = Top3PersDTO(id_persoana, persoana_nume, nr_evenimente_persoana)

            result.append(top_3_pers_dto)

        result.sort(key=lambda x: x.get_evenimente_persoana(), reverse=True)

        result = result[:3]

        return result

    def __calculate_toti_participanti_per_eveniment(self):

        toti_partc_per_even = {}
        inscrieri_dtos = self.__inscriere_file_repo.get_inscrieri()

        for inscriere in inscrieri_dtos:
            id_eveniment = inscriere.get_id_eveniment()
            if id_eveniment not in toti_partc_per_even:
                toti_partc_per_even[id_eveniment] = 0
            toti_partc_per_even[id_eveniment] += 1

        return toti_partc_per_even

    def __calculate_toate_evenimentele_per_participant(self):
        toti_participantii_pentru_fiecare_eveniment = {}

        inscrieri_dtos = self.__inscriere_file_repo.get_inscrieri()

        for inscriere in inscrieri_dtos:
            id_participant = inscriere.get_id_persoana()
            if id_participant not in toti_participantii_pentru_fiecare_eveniment:
                toti_participantii_pentru_fiecare_eveniment[id_participant] = 0
            toti_participantii_pentru_fiecare_eveniment[id_participant] += 1

        return toti_participantii_pentru_fiecare_eveniment
