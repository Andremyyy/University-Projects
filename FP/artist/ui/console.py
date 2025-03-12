from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, service):
        self.__service = service

    def run(self):
        comenzi = self.__create_comenzi()

        while True:
            self.__print_comenzi(comenzi)
            cmd,args = self.__read_comanda()

            if cmd == "exit":
                break
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("comanda neimplementata!")

    def __create_comenzi(self):
        return {
            "add_artist": self.__add_artist,
            "print_artist": self.__print_artist,
            "afiseaza_categorie_descr_tarif": self.__categorie_descr_tarif
        }

    def __add_artist(self, id, nume, categorie, tarif):
        try:
            id = int(id)
            tarif = float(tarif)
            self.__service.add_artist(id, nume, categorie, tarif)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg, tariful trebuie sa fie numar real!")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")
        except RepoException as re:
            print(f"eroare repo: {re}")

    def __print_artist(self):
        lista = self.__service.get_all_artists()

        if len(lista) == 0:
            print("Nu exista artisti!")
            return

        for artist in lista:
            print(artist)

    def __print_comenzi(self, comenzi):
        print("Comenzi disponibile:\n")
        print(*comenzi.keys(), "exit", sep ="\n")

    def __read_comanda(self):
        comanda = input("Comanda ta este:\n")
        pos = comanda.find(" ")

        if pos == -1:
            return comanda, []


        cmd = comanda[:pos]
        args = comanda[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]

        return cmd, args

    def __categorie_descr_tarif(self, categorie):
        lista = self.__service.categorie_descr_tarif(categorie)

        if len(lista) == 0:
            print("Nu exista artisti din categoria data!")
            return

        for artist in lista:
            print(artist)

