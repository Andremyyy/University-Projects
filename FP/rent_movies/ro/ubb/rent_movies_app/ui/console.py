from ro.ubb.rent_movies_app.errors.exceptions import ValidationError, RepositoryError, UIError


class Console:
    def __ui_add_movie(self, params):
        if len(params) != 4:
            raise UIError("wrong number of parameters!")
        try:
            id_movie = int(params[0])
            title = params[1]
            description = params[2]
            genre = params[3]
            self.__service_movies.add_movie(id_movie, title, description, genre)
        except ValueError:
            raise UIError("invalid numerical value!")

    def __ui_print_all_movies(self, params):
        movies = self.__service_movies.get_all_movies()
        if len(movies) == 0:
            raise UIError("no movies yet")
        for movie in movies:
            print(movie)

    def __ui_add_client(self, params):
        if len(params) != 3:
            raise UIError("wrong number of parameters!")
        try:
            id_client = int(params[0])
            name = params[1]
            cnp = params[2]
            self.__service_clients.add_client(id_client, name, cnp)
        except ValueError:
            raise UIError("invalid numerical value!")

    def __ui_print_all_clients(self, params):
        clients = self.__service_clients.get_all_clients()
        if len(clients) == 0:
            raise UIError("no clients yet")
        for client in clients:
            print(client)

    def __ui_add_rental(self, params):
        if len(params) != 6:
            raise UIError("wrong number of parameters!")
        try:
            id_rental = int(params[0])
            id_movie = int(params[1])
            id_client = int(params[2])
            day = int(params[3])
            month = int(params[4])
            year = int(params[5])
            self.__service_rentals.add_rental(id_rental, id_movie, id_client, day, month, year)
        except ValueError:
            raise UIError("invalid numerical value!")

    def __ui_print_all_rentals(self,params):
        rentals = self.__service_rentals.get_all_rentals()
        if len(rentals) == 0:
            raise UIError("no rentals yet")
        for rental in rentals:
            print(rental)

    def __ui_top_30_percentage_clients(self,params):
        if len(params) != 0:
            raise UIError("wrong number of parameters!")

        top_30_percentage_clients = self.__service_rentals.top_30_percentage_clients()
        if len(top_30_percentage_clients) == 0:
            raise UIError("no top clients!")
        for client in top_30_percentage_clients:
            print(client)

    def __ui_most_rented_movies(self,params):
        if len(params) != 0:
            raise UIError("wrong number of parameters!")

        top_most_rented_movies = self.__service_rentals.top_rented_movies()
        if len(top_most_rented_movies) == 0:
            raise UIError("no top most rented movie!")
        for movie in top_most_rented_movies:
            print(movie)

    def __ui_update_movie(self,params):
        if len(params) != 4:
            raise UIError("wrong number of parameters!")
        try:
            id_movie = int(params[0])
            new_title = params[1]
            new_description = params[2]
            new_genre = params[3]
            self.__service_movies.update_movie(id_movie,new_title,new_description,new_genre)
        except ValueError:
            raise UIError("invalid numerical value!")

    def __ui_delete_movie_by_id(self,params):
        if len(params) != 1:
            raise UIError("wrong number of parameters!")
        try:
            id_movie = int(params[0])
            self.__service_movies.delete_movie_by_id(id_movie)
        except ValueError:
            raise UIError("invalid numerical value!")

    def __ui_search_movie_by_title(self,params):
        if len(params) != 1:
            raise UIError("wrong number of parameters!")
        title = params[0]
        new_movie_list = self.__service_movies.search_movie_by_title(title)
        for movie in new_movie_list:
            print(f"{movie.get_id_movie()},{movie.get_title()},{movie.get_description()},{movie.get_genre()}")

    def __init__(self, service_movies, service_clients, service_rentals):

        self.__service_movies = service_movies
        self.__service_clients = service_clients
        self.__service_rentals = service_rentals
        # dictionar de comezni acceptate de sistem:
        # cheia va fi un string care reprezinta codul de comanda,
        # iar valoarea va fi numele functiei din python care se va ocupa de fiecare comanda
        self.__commands = {
            "add_movie": self.__ui_add_movie,
            "print_all_movies": self.__ui_print_all_movies,
            "update_movie": self.__ui_update_movie,
            "delete_movie_by_id": self.__ui_delete_movie_by_id,
            "search_movie_by_title": self.__ui_search_movie_by_title,
            "add_client": self.__ui_add_client,
            "print_all_clients": self.__ui_print_all_clients,
            "add_rental": self.__ui_add_rental,
            "print_all_rentals": self.__ui_print_all_rentals,
            "top_30_percentage_clients": self.__ui_top_30_percentage_clients,
            "most_rented_movies": self.__ui_most_rented_movies,
            # "help": self.__ui_help
        }

    def run(self):
        commands = self.__create_commands()
        while True:

            # command = input(">>>>>>>>  Hello!!!  <<<<<<<<<<\n"
            #                 "Please introduce your command: \n")
            self.__print_all_commands(commands)
            # command = command.strip()

            try:
                command, parts = self.__read_command()
            except ValueError as ve:
                print("exception in read command: ", ve)
                continue

            if command == "":    # daca utilizatorul nu a introdus nimic
                continue
            if command == "exit":
                break

            # impart comanda acceptat de sistem in parti:
            # parts = command.split()     # spatiu default daca nu am parametru la split => impart dupa spatiu

            # command_name = parts[0]

            # restul vor fi parametrii:
            # params = parts[1:]

            if command in self.__commands:
                # apelez functia respectiva:
                try:
                    commands[command](parts)
                except ValidationError as ve:
                    print(f"validation error: {ve}")
                except RepositoryError as re:
                    print(f"repository error: {re}")
                except UIError as ue:
                    print(f"UI error: {ue}")
            else:
                print("Invalid command!!!")

    def __print_all_commands(self, command):
        print("\n>>>>>>>>  Hello!!!  <<<<<<<<<<\n\n","Please choose your command!" )
        print(*command.keys(), "exit", sep=" --- ")
        # print("For HELP type: help <command>. E.g: help add")

    def __create_commands(self):
        return {
            "add_movie": self.__ui_add_movie,
            "print_all_movies": self.__ui_print_all_movies,
            "update_movie": self.__ui_update_movie,
            "delete_movie_by_id": self.__ui_delete_movie_by_id,
            "search_movie_by_title": self.__ui_search_movie_by_title,
            "add_client": self.__ui_add_client,
            "print_all_clients": self.__ui_print_all_clients,
            "add_rental": self.__ui_add_rental,
            "print_all_rentals": self.__ui_print_all_rentals,
            "top_30_percentage_clients": self.__ui_top_30_percentage_clients,
            "most_rented_movies": self.__ui_most_rented_movies,
            # "help":self.__ui_help
        }

    def __read_command(self):
        command = input("Your command = ")
        pos = command.find(" ")

        if pos == -1:
            return command, []

        cmd = command[:pos]
        args = command[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]
        return cmd, args

    # def __ui_help(self, cmd):
    #     help_commands = {"add_movie": "Usage: add_movie <id_movie>,<movie_title>,<movie_decription>,<movie_genre>. E.g: add_movie 1,Snow-White,A-movie-for-kids, Animation",
    #                      "print_all_movies": "Usage: print_all_movies",
    #                      "add_client": "Usage: add_client <id_client>,<client_name>,<client_cnp>. E.g: add_client 1,Popescu-Alex,5021215456321",
    #                      "print_all_clients": "Usage: print_all_clients",
    #                      "add_rental": "Usage: add_rental <id_rental>,<id_movie>,<id_client>,<day>, <month>,<year>. E.g: add_rental 1,1,1,15,03,2001",
    #                      "print_all_rentals": "Usage: print_all_rentals",
    #                      "top_30_percentage_clients": "Usage: top_30_percentage_clients",
    #                      "most_rented_movies": "Usage: most_rented_movies",
    #                      "exit": "Usage: exit"}
    #     try:
    #         print(help_commands[cmd], "\n")
    #     except KeyError:
    #         print("no help for command={0}".format(cmd))

