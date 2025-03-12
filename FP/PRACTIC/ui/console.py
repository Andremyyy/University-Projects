from exceptions.erori import RepoException


class Console:
    def __init__(self, movie_service):
        self.__movie_service = movie_service


    def run(self):
        comenzi = self.__create_comenzi()

        while True:
            self.__print_comenzi(comenzi)

            cmd, args = self.__read_comanda()

            if cmd == "exit":
                break
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("Comanda neimplementata!!")


    def __afiseaza_filme(self):
        lista = self.__movie_service.get_all_movies()

        if len(lista) == 0:
            print("Nu exista filme!")
            return

        for film in lista:
            print(film)

    def __create_comenzi(self):
        return {
            "print_movies": self.__afiseaza_filme,
            "add": self.__add_file,
            "search": self.__search

        }

    def __print_comenzi(self, comenzi):
        print("Meniu:\n")
        print(*comenzi.keys(), "exit", sep = "\n")

    def __read_comanda(self):
        comanda_ta = input("Comanda ta este:")
        pos = comanda_ta.find(" ")
        if pos == -1:
            return comanda_ta, []

        cmd = comanda_ta[:pos]
        args = comanda_ta[pos:]
        args = args.split("-")
        args = [s.strip() for s in args]

        return cmd, args

    def __add_file(self, id, title, director, year, rating, genre1, genre2, genre3):
        try:
            id = int(id)
            year = int(year)
            rating = float(rating)

            self.__movie_service.add(id, title,director,year,rating,genre1,genre2,genre3)

        except ValueError:
            print("Date invalide pt id, year, rating")
        except RepoException as re:
            print(f"eroare repo: {re}")

    def __search(self, title, year):

        try:
            year = int(year)
            lista = self.__movie_service.search(title,year)

            if len(lista) == 0:
                print("Nu exista filme din anul dat!")
                return

            for film in lista:
                print(f"{film.get_id()},{film.get_title()},{film.get_genres()} ")
        except ValueError:
            print("anul trebuie sa fie tip int")
