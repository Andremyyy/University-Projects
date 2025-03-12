from exceptions.errors import ValidatorException, RepoException


class Console:
    def __init__(self, service):
        self.__service = service
        self.__menu = ("\nMenu:\n"
                       "1. Afiseaza toate cafelele \n"
                       "2. Filetreaza cafele dupa tara \n"
                       "3. Adauga cafea \n"
                       "exit\n\n"
                       "Alege optiune:\n")

    def run(self):
        while True:
            try:
                command = input(self.__menu)
                if command == "1":
                    self.__print_all()
                elif command == "2":
                    self.__filtreaza_tara()
                elif command == "3":
                    self.__add_cafea()
                elif command == "exit":
                    return
                else:
                    print("Comanda invalida!")
            except ValidatorException as ve:
                print(f"eroare validare: {ve}")
            except RepoException as re:
                print(f"eroare repo: {re}")

    def __print_all(self):
        lista = self.__service.print_all()

        if len(lista) == 0:
            print("Nu exista cafele inca!")
            return

        for cafea in lista:
            print(cafea)

    def __filtreaza_tara(self):

        tara = input("tara cafelelor cautate este:")
        if len(tara) == 0:
            print("numele tarii este invalid!")
            return

        lista = self.__service.filtreaza_tara(tara)

        if len(lista) == 0:
            print("Nu exista cafele din tara data!")
            return

        for cafea in lista:
            print(cafea)

    def __add_cafea(self):
        try:
            id = int(input("id-ul este: "))
            nume = input("numele este: ")
            tara = input("tara de orginine este: ")
            pret = float(input("pretul este:"))
            self.__service.add_cafea(id, nume, tara, pret)
        except ValueError:
            print("id-ul este numar intreg, pretul este numar real")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")
        except RepoException as re:
            print(f"eroare repo: {re}")
