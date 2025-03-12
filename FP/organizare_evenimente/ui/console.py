# meniu cu comenzi
from exceptions.erori import EvenimentValidatorException, EvenimentRepoException, PersoanaValidatorException, \
    PersoanaRepoException, InscriereValidatorException, InscriereRepoException


class Console:
    def __init__(self, persoana_service, evenimente_service, inscriere_service):
        self.__persoana_service = persoana_service
        self.__evenimente_service = evenimente_service
        self.__inscriere_service = inscriere_service

    def run(self):
        comenzi = {
            "add_persoana": self.__add_persoana,
            "get_persoane": self.__get_persoane,
            "delete_persoana": self.__delete_persoana,
            "update_persoana": self.__update_persoana,
            "add_eveniment": self.__add_eveniment,
            "get_evenimente": self.__get_evenimente,
            "delete_eveniment": self.__delete_eveniment,
            "update_eveniment": self.__update_eveniment,
            "cautare_persoane": self.__cautare_persoane,
            "cautare_evenimente": self.__cautare_eveniment,
            "add_inscriere": self.__add_inscriere,
            "get_inscrieri": self.__get_inscrieri,
            #  Lista de evenimente la care participă o persoană ordonata alfabetic după descriere, după
            # dată ?????
            # #todo: cum se face!?!?
            "evenimente_persoana_dupa_descriere": self.__evenimente_persoana_dupa_descriere,

            #  Primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)
            "top20_evenimente": self.__top20_evenimnete,

            #  Persoane participante la cele mai multe evenimente (top 3 persoane)
            "top3_persoane_participante": self.__top3_persoane_participante
        }

        while True:
            self.__print_comanda(comenzi)
            try:
                comanda, argumente = self.__read_comenzi()
            except ValueError as ve:
                print(f"exception: {ve}")
                continue

            if comanda == "exit":
                break

            try:
                comenzi[comanda](*argumente)  # comenzi de comanda(cheia) de argumentele pe rand (valoriile din dictionar = *args)
            except KeyError as ke:
                print(f"optiunea nu exista inca: {ke}")

    def __print_comanda(self, comenzi):
        print("\n MENU: \n")
        print(*comenzi.keys(), "exit", sep="\n")

    def __read_comenzi(self):
        command = input("Alege comanda: \n")
        pos = command.find(" ")

        if pos == -1:
            return command, []  # [] pt ca nu exista argumente

        comanda = command[:pos]
        argumente = command[pos:]
        argumente = argumente.split(",")
        argumente = [element.strip() for element in argumente]  # elimina spatiile dintre argumente

        return comanda, argumente

    def __add_persoana(self, id, nume, adresa):
        try:
            id = int(id)
            self.__persoana_service.add_persoana(id, nume, adresa)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv!")
        except PersoanaValidatorException as ve:
            print(f"eroare validare: {ve}")
        except PersoanaRepoException as re:
            print(f"eroare repo: {re}")

    def __get_persoane(self):
        persoane = self.__persoana_service.get_persoane()
        if len(persoane) == 0:
            print("Nu exista persoane!")
            return
        for persoana in persoane:
            print(persoana)

    def __delete_persoana(self, id):
        try:
            id = int(id)
            self.__persoana_service.delete_persoana(id)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv!")
        except PersoanaRepoException as re:
            print(f"eroare repo: {re}")

    def __update_persoana(self, id, nume_nou, adresa_noua):
        try:
            id = int(id)
            self.__persoana_service.update_persoana(id, nume_nou, adresa_noua)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv!")
        except PersoanaValidatorException as ve:
            print(f"eroare validare: {ve}")
        except PersoanaRepoException as re:
            print(f"eroare repo: {re}")

    def __add_eveniment(self, id, data, ora, descriere):
        try:
            id = int(id)
            self.__evenimente_service.add_eveniment(id, data, ora, descriere)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv!")
        except EvenimentValidatorException as ve:
            print(f"eroare validare: {ve}")
        except EvenimentRepoException as re:
            print(f"eroare repo: {re}")

        # todo: de vazaut de ce da value error la toate, ci nu validator sau repo exception

    def __get_evenimente(self):
        evenimente = self.__evenimente_service.get_evenimente()

        if len(evenimente) == 0:
            print("Nu exista niciun eveniment")
            return

        for eveniment in evenimente:
            print(eveniment)

    def __delete_eveniment(self, id):
        try:
            id = int(id)
            self.__evenimente_service.delete_eveniment(id)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv!")
        except EvenimentRepoException as re:
            print(f"eroare repo: {re}")

    def __update_eveniment(self, id, data, ora, descriere):
        try:
            id = int(id)
            self.__evenimente_service.update_eveniment(id, data, ora, descriere)
        except ValueError:
            print("id-ul trebuie sa fie intreg pozitiv!")
        except EvenimentValidatorException as eve:
            print(f"eroare validare: {eve}")
        except EvenimentRepoException as re:
            print(f"eroare repo: {re}")

    def __cautare_persoane(self, adresa):

        new_list_adresa = self.__persoana_service.cautare_persoane(adresa)

        if len(new_list_adresa) == 0:
            print("Nu exista persoane cu adresa data!")
            return

        for persoana in new_list_adresa:
            print(persoana)

    def __cautare_eveniment(self, data):

        new_list_data = self.__evenimente_service.cautare_evenimente_dupa_data(data)

        if len(new_list_data) == 0:
            print("Nu exista evenimente cu data data!")
            return

        for eveniment in new_list_data:
            print(eveniment)

    def __add_inscriere(self, id_inscriere, id_persoana, id_eveniemnt, pret):
        try:
            id_inscriere = int(id_inscriere)
            id_persoana = int(id_persoana)
            id_eveniemnt = int(id_eveniemnt)
            pret = int(pret)
            self.__inscriere_service.add_inscriere(id_inscriere, id_persoana, id_eveniemnt, pret)
        except ValueError:
            print("trebuie sa fie numere intregi pozitive!")
        except InscriereValidatorException as ive:
            print(f"eroare validare: {ive}")
        except InscriereRepoException as ire:
            print(f"eroare repo: {ire}")
        except PersoanaRepoException as pre:
            print(f"eroare repo: {pre}")
        except EvenimentRepoException as ere:
            print(f"eroare repo: {ere} ")

    def __get_inscrieri(self):
        try:
            inscrieri = self.__inscriere_service.get_inscrieri()
            if len(inscrieri) == 0:
                print("Nu exista inscrieri!")
                return
            for inscriere in inscrieri:
                print(inscriere)
        except PersoanaRepoException as pre:
            print(f"eroare repo: {pre}")
        except EvenimentRepoException as ere:
            print(f"eroare repo: {ere}")

    def __evenimente_persoana_dupa_descriere(self, id_persoana):


        #todo: cum se face?!?!

        try:
            id_persoana = int(id_persoana)

            lista = self.__inscriere_service.evenimente_persoana_dupa_descriere(id_persoana)

            if len(lista) == 0:
                print("Nu exista evenimente la care participa persoana data.")
                return

            for element in lista:
                print(element)

        except ValueError:
            print("id_ul trb sa fie intreg pozitiv!")
        except PersoanaRepoException as pre:
            print(f"eroare repo: {pre}")
        except EvenimentRepoException as ere:
            print(f"eroare repo: {ere}")

    def __top20_evenimnete(self):

        top20_evenimente = self.__inscriere_service.top_20_evenimente()

        if len(top20_evenimente) == 0:
            print("Nu exista evenimente cu participanti!")
            return

        for eve in top20_evenimente:
            print(eve)

    def __top3_persoane_participante(self):

        top3_pers_part = self.__inscriere_service.top_3_pers_part()

        if len(top3_pers_part) == 0:
            print("Nu exista top persoane participante la evenimente!")
            return

        for pers in top3_pers_part:
            print(pers)
