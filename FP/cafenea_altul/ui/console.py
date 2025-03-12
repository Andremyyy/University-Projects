from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, cafea_service):
        self.__cafea_service = cafea_service

    def run(self):
        comenzi = self.__create_comenzi()

        while True:
            self.__print_comenzi(comenzi)

            comanda, argumente = self.__read_comanda()

            if comanda == "exit":
                break
            try:
                comenzi[comanda](*argumente)
            except KeyError:
                print("Nu este implementata inca aceasta comanda!")

    def __create_comenzi(self):
        return {
            "add_cafea": self.__add_cafea,
            "print_cafele": self.__get_all_cafele,
            "cresc_dupa_tara_si_pret": self.__cresc_dupa_tara_si_pret,
            "filtrati_tara_pret": self.__filtrati_dupa_tara_si_pret,
            "update_cafea": self.__update_cafea,
            "delete_cafea": self.__delete_cafea,
            "update_cafea_cu_tara_data": self.__update_cafea_cu_tara_data
        }

    def __print_comenzi(self, comenzi):
        print("\nComenzile disponibile sunt: \n")
        print(*comenzi.keys(), "exit", sep = "\n")

    def __read_comanda(self):
        comanda = input("Comanda ta este:")
        pos = comanda.find(" ")
        if pos == -1:
            return comanda, []

        cmd = comanda[:pos]
        args = comanda[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]

        return cmd, args

    def __add_cafea(self, id, nume, tara_de_origine, pret):
        try:
            id = int(id)
            pret = float(pret)
            self.__cafea_service.add_cafea(id, nume, tara_de_origine, pret)
        except ValueError:
            print("id-ul trebuie sa fie int, pretul trebuie sa fie float!")
        except ValidatorException as ve:
            print(f"eroare validare:{ve}")
        except RepoException as re:
            print(f"eraore repo: {re}")

    def __get_all_cafele(self):
        lista = self.__cafea_service.get_all_cafele()

        if len(lista) == 0:
            print("Nu exista cafele")
            return

        for cafea in lista:
            print(cafea)

    def __cresc_dupa_tara_si_pret(self):
        lista_sortata = self.__cafea_service.cresc_dupa_tara_si_pret()

        if len(lista_sortata) == 0:
            print("nu exista cafele!")
            return

        for cafea in lista_sortata:
            print(cafea)

    def __filtrati_dupa_tara_si_pret(self, tara, pret):

        if not pret:
            lista = self.__cafea_service.filtrati_dupa_tara(tara)
        elif not tara:
            try:
                pret = float(pret)
                lista = self.__cafea_service.filtrati_dupa_pret(pret)
            except ValueError:
                print("pretul trebuie sa fie intreg!")
        else:
            try:
                pret = float(pret)
                lista = self.__cafea_service.filtrati_dupa_tara_si_pret(tara, pret)

            except ValueError:
                print("pretul trebuie sa fie intreg!")
        if len(lista) == 0:
            print("Nu exista astfel de cafele!")
            return

        for cafea in lista:
            print(cafea)

    def __update_cafea(self, id, nume, tara, pret):
        try:
            id = int(id)
            pret = float(pret)
            self.__cafea_service.update_cafea(id, nume, tara, pret)
        except ValueError:
            print("data invalide")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")
        except RepoException as re:
            print(f"eroare repo: {re}")
    def __delete_cafea(self, id):

        try:
            id = int(id)
            self.__cafea_service.delete_cafea(id)
        except ValueError:
            print("id invalid!")
        except RepoException as re:
            print(f"eroare repo: {re}")

    def __update_cafea_cu_tara_data(self, tara):
        try:
            self.__cafea_service.update_cafea_cu_tara_data(tara)
        except RepoException as re:
            print(f"eroare repo: {re}")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")

