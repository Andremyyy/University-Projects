import random

from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, service):
        self.__service = service
        self.__menu = ("\nMENU\n"
                       "1 Adaugare cafea\n"
                       "2 Afiseaza cafele\n"
                       "3 Afiseaza cafele sortate alfabetic dupa tara_de_origine\n"
                       "4 Filtreaza cafelele dupa tara de origine si pret\n"
                       "exit\n"
                       "Choose option: \n")

    def run(self):
        while True:
            command = input(self.__menu)
            try:
                if command == "1":
                    self.__ui_add_cafea()
                elif command == "2":
                    self.__ui_print_cafele()
                elif command == "3":
                    self.__ui_print_cafele_dupa_tara()
                elif command == "4":
                    self.__ui_filtreaza_tara_si_pret()
                elif command == "exit":
                    return
                else:
                    print("Invalid Command!!!")
            except ValidatorException as ve:
                print(ve)
            except RepoException as re:
                print(re)

    def __ui_add_cafea(self):
        try:
            id = random.randint(1, 20)
            nume = input("Care e numele cafelei?")
            tara_de_origine = input("Care e tara de origine?")
            pret = float(input("Care e pretul?"))
            self.__service.add_cafele(id, nume, tara_de_origine, pret)
        except ValueError:
            print("pretul trebuie sa fie float")
        except ValidatorException as ve:
            print(ve)
        except RepoException as re:
            print(re)

    def __ui_print_cafele(self):
        cafele = self.__service.get_all_cafele()
        if len(cafele) == 0:
            print("Nu exista cafele!")
        else:
            for cafea in cafele:
                print(cafea)

    def __ui_print_cafele_dupa_tara(self):
        cafele = self.__service.get_cafele_dupa_tara()
        if len(cafele) == 0:
            print("Nu exista cafele!")
        else:
            for cafea in cafele:
                print(cafea)

    def __ui_filtreaza_tara_si_pret(self):
        tara_de_origine = input("Tara de origine este:")
        pret = input("Pretul este:")

        if not tara_de_origine:
            cafele_filtrate = self.__service.get_cafele_dupa_pret(pret)
        else:
            if not pret:
                cafele_filtrate = self.__service.filtreaza_cafele_tara(tara_de_origine)
            else:
                try:
                    pret = float(pret)
                except ValueError:
                    print("pretul trebuie sa fie float!")
                cafele_filtrate = self.__service.get_cafele_filtrate(tara_de_origine, pret)

        if len(cafele_filtrate) == 0:
            print("Nu exista astfel de cafele")
        else:
            for cafea in cafele_filtrate:
                print(cafea)
