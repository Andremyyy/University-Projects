from ro.ubb.rent_movies_app.domain.client import Client
from ro.ubb.rent_movies_app.domain.movie import Movie
from ro.ubb.rent_movies_app.errors.exceptions import ValidationError, RepositoryError
from ro.ubb.rent_movies_app.repository.repo_clients import  FileRepoClients
from ro.ubb.rent_movies_app.repository.repo_movies import FileRepoMovies
from ro.ubb.rent_movies_app.service.service_clients import ServiceClients
from ro.ubb.rent_movies_app.service.service_movies import ServiceMovies
from ro.ubb.rent_movies_app.validate.validator_client import ValidatorClient
from ro.ubb.rent_movies_app.validate.validator_movie import ValidatorMovie


class Teste:
    def __init__(self):
        pass

    def run_all_tests(self):
        print("starting tests....")
        self.__run_tests_domain_movie()
        self.__run_tests_validate_movie()
        self.__run_tests_add_movie_repo()
        self.__run_tests_add_movie_service()
        self.__run_tests_get_all_movies_repo()
        self.__run_tests_get_all_movies_service()
        self.__run_tests_domain_client()
        self.__run_tests_validate_client()
        self.__run_tests_add_client_repo()
        self.__run_tests_add_client_service()
        self.__run_tests_get_all_clients_repo()
        self.__run_tests_get_all_clients_service()

    def __run_tests_domain_movie(self):
        print("starting movie domain tests...")
        self.__id_movie = 1
        self.__title = "Alba"
        self.__description = "Film"
        self.__genre = "Animatie"
        self.__movie = Movie(self.__id_movie, self.__title, self.__description, self.__genre)

        assert self.__movie.get_id_movie() == self.__id_movie
        assert self.__movie.get_title() == self.__title
        assert self.__movie.get_description() == self.__description
        assert self.__movie.get_genre() == self.__genre

        self.__another_title = "Barbie"
        self.__another_description = "Alt"
        self.__another_genre = "Papusi"

        self.__another_movie_same_id = Movie(self.__id_movie, self.__another_title, self.__another_description,
                                             self.__another_genre)

        # assert self.__movie == self.__another_movie_same_id
        assert Movie.__eq__(self.__movie, self.__another_movie_same_id)
        # assert self.__movie.__eq__(self.__another_movie_same_id)
        # cele 3 linii anterioare fac acelasi lucru

        print("movie domain tests finished successfully!")

    def __run_tests_validate_movie(self):
        print("starting movie validation tests...")
        self.__validator_movie = ValidatorMovie()
        self.__validator_movie.validate_movie(self.__movie)

        self.__id_movie_not_valid = -1
        self.__title_not_valid = "mamma"  # incepe cu litera mica
        self.__description_not_valid = "Ceva descriere foarte lunga care are mai mult de 30 de caractere"
        self.__genre_not_valid = ""  # e gol

        self.__movie_not_valid = Movie(self.__id_movie_not_valid, self.__title_not_valid, self.__description_not_valid,
                                       self.__genre_not_valid)
        try:
            self.__validator_movie.validate_movie(self.__movie_not_valid)
            assert False
        except ValidationError as ve:
            assert str(
                ve) == "The id is not valid!\nThe title is not valid!\nThe description is not valid!\nThe genre is not valid!"

        print("movie validation tests finished successfully!")

    def __run_tests_add_movie_repo(self):
        print("starting movie add to repo tests...")
        # self.__repo_movies = RepoMovies()
        movies_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_movies.csv"
        self.__clear_file(movies_path_name)
        self.__repo_movies = FileRepoMovies(movies_path_name)
        assert len(self.__repo_movies) == 0
        self.__repo_movies.add_movie(self.__movie)
        movie_found = self.__repo_movies.find_movie_by_id(self.__id_movie)
        assert movie_found == self.__movie
        assert movie_found.get_title() == self.__movie.get_title()
        assert movie_found.get_description() == self.__movie.get_description()
        assert movie_found.get_genre() == self.__movie.get_genre()

        assert len(self.__repo_movies) == 1

        try:
            self.__repo_movies.add_movie(self.__another_movie_same_id)
            assert False
        except RepositoryError as re:
            assert str(re) == "Movie duplicate id!"

        print("movie add to repo tests finished successfully!")

    def __run_tests_add_movie_service(self):
        print("starting movie add service tests... ")

        movies_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_movies.csv"
        self.__clear_file(movies_path_name)
        self.__repo_movies = FileRepoMovies(movies_path_name)

        self.__service_movies = ServiceMovies(self.__repo_movies, self.__validator_movie)

        assert self.__service_movies.number_of_movies() == 0
        self.__service_movies.add_movie(self.__id_movie, self.__title, self.__description, self.__genre)
        assert self.__service_movies.number_of_movies() == 1

        movie_found = self.__service_movies.find_by_id(self.__id_movie)
        assert movie_found == self.__movie
        assert movie_found.get_title() == self.__movie.get_title()
        assert movie_found.get_description() == self.__movie.get_description()
        assert movie_found.get_genre() == self.__movie.get_genre()

        try:
            self.__service_movies.add_movie(self.__id_movie, self.__another_title, self.__another_description,
                                            self.__another_genre)
            assert False
        except RepositoryError as re:
            assert str(re) == "Movie duplicate id!"

        try:
            self.__service_movies.add_movie(self.__id_movie_not_valid, self.__title_not_valid,
                                            self.__description_not_valid, self.__genre_not_valid)
            assert False
        except ValidationError as ve:
            assert str(ve) == "The id is not valid!\nThe title is not valid!\nThe description is not valid!\nThe genre is not valid!"

        print("movie add service tests finished successfully!")

    def __clear_file(self, movies_path_name):
        with open(movies_path_name, 'w') as f:  # 'w' de la write
            f.write("")

    def __run_tests_get_all_movies_service(self):
        print("starting movie get all service tests...")
        movies_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_movies.csv"
        self.__clear_file(movies_path_name)
        self.__repo_movies = FileRepoMovies(movies_path_name)

        self.__service_movies = ServiceMovies(self.__repo_movies, self.__validator_movie)
        assert self.__service_movies.number_of_movies() == 0

        self.__another_id_movie = 24
        self.__service_movies.add_movie(self.__another_id_movie, self.__another_title, self.__another_description,
                                        self.__another_genre)
        self.__service_movies.add_movie(self.__id_movie, self.__title, self.__description,
                                        self.__genre)
        movies = self.__service_movies.get_all_movies()
        assert len(movies) == 2

        # sortare dupa id:
        movies.sort(key=lambda x: x.get_id_movie())

        assert movies[0].get_id_movie() == self.__id_movie
        assert movies[1].get_id_movie() == self.__another_id_movie

        assert movies[0].get_title() == self.__title
        assert movies[0].get_description() == self.__description
        assert movies[0].get_genre() == self.__genre

        assert movies[1].get_title() == self.__another_title
        assert movies[1].get_description() == self.__another_description
        assert movies[1].get_genre() == self.__another_genre

        print("movies get all service tests finished successfully!")

    def __run_tests_get_all_movies_repo(self):
        print("starting movie get all repo tests...")
        movies_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_movies.csv"
        self.__clear_file(movies_path_name)
        self.__repo_movies = FileRepoMovies(movies_path_name)
        assert len(self.__repo_movies) == 0

        self.__repo_movies.add_movie(self.__movie)
        self.__another_id_movie = 24
        self.__another_movie = Movie(self.__another_id_movie, self.__another_title, self.__another_description,
                                     self.__another_genre)
        self.__repo_movies.add_movie(self.__another_movie)

        movies = self.__repo_movies.get_all_movies()
        assert len(movies) == 2

        # sortare dupa id:
        movies.sort(key=lambda x: x.get_id_movie())

        assert movies[0].get_id_movie() == self.__id_movie
        assert movies[1].get_id_movie() == self.__another_id_movie

        assert movies[0].get_title() == self.__title
        assert movies[0].get_description() == self.__description
        assert movies[0].get_genre() == self.__genre

        assert movies[1].get_title() == self.__another_title
        assert movies[1].get_description() == self.__another_description
        # assert movies[1].get_genre() == self.__another_genre

        print("movies get all repo tests finished successfully!")

    def __run_tests_domain_client(self):
        print("starting client domain tests...")
        self.__id_client = 12
        self.__name = "Popescu George"
        self.__cnp = "5021116352987"
        self.__client = Client(self.__id_client, self.__name, self.__cnp)
        assert self.__client.get_id_client() == self.__id_client
        assert self.__client.get_name() == self.__name
        assert self.__client.get_cnp() == self.__cnp

        self.__another_name = "Ionescu Anca"
        self.__another_cnp = "6011218453627"

        self.__another_client_same_id = Client(self.__id_client, self.__another_name, self.__another_cnp)

        # assert self.__movie == self.__another_movie_same_id
        assert Client.__eq__(self.__client, self.__another_client_same_id)

        print("client domain tests finished successfully!")

    def __run_tests_validate_client(self):
        print("starting client validation tests...")

        self.__validator_client = ValidatorClient()
        self.__validator_client.validate_client(self.__client)

        self.__id_client_not_valid = -1
        self.__name_not_valid = "popa marius"  # incepe cu litera mica
        self.__cnp_not_valid = "12345" #lungime invalida
        #todo: pune si alte exemple de cnp invalide!!!

        self.__client_not_valid = Client(self.__id_client_not_valid, self.__name_not_valid, self.__cnp_not_valid)

        try:
            self.__validator_client.validate_client(self.__client_not_valid)
            assert False
        except ValidationError as ve:
            assert str(ve) == "The id is not valid!\nThe name is not valid!\nThe cnp is not valid!"

        print("client validation tests finished successfully!")

    def __run_tests_add_client_repo(self):
        print("starting client add to repo tests...")
        # self.__repo_clients = RepoClients()
        clients_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_clients.csv"
        self.__clear_file(clients_path_name)
        self.__repo_clients = FileRepoClients(clients_path_name)

        assert len(self.__repo_clients) == 0
        self.__repo_clients.add_client(self.__client)
        client_found = self.__repo_clients.find_client_by_id(self.__id_client)
        assert client_found == self.__client
        assert client_found.get_name() == self.__client.get_name()
        assert client_found.get_cnp() == self.__client.get_cnp()

        assert len(self.__repo_clients) == 1

        try:
            self.__repo_clients.add_client(self.__another_client_same_id)
            assert False
        except RepositoryError as re:
            assert str(re) == "Client duplicate id!"

        print("client add to repo tests finished successfully!")

    def __run_tests_add_client_service(self):
        print("starting client add service tests... ")

        clients_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_clients.csv"
        self.__clear_file(clients_path_name)
        self.__repo_clients = FileRepoClients(clients_path_name)

        self.__service_clients = ServiceClients(self.__repo_clients, self.__validator_client)

        assert self.__service_clients.number_of_clients() == 0
        self.__service_clients.add_client(self.__id_client, self.__name, self.__cnp)
        assert self.__service_clients.number_of_clients() == 1

        client_found = self.__service_clients.find_client_by_id(self.__id_client)
        assert client_found == self.__client
        assert client_found.get_name() == self.__client.get_name()
        assert client_found.get_cnp() == self.__client.get_cnp()

        try:
            self.__service_clients.add_client(self.__id_client, self.__another_name, self.__another_cnp)
            assert False
        except RepositoryError as re:
            assert str(re) == "Client duplicate id!"

        try:
            self.__service_clients.add_client(self.__id_client_not_valid, self.__name_not_valid, self.__cnp_not_valid)
            assert False
        except ValidationError as ve:
            assert str(ve) == "The id is not valid!\nThe name is not valid!\nThe cnp is not valid!"

        print("client add service tests finished successfully!")

    def __run_tests_get_all_clients_repo(self):
        print("starting client get all repo tests...")
        clients_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_clients.csv"
        self.__clear_file(clients_path_name)
        self.__repo_clients = FileRepoClients(clients_path_name)
        assert len(self.__repo_clients) == 0

        self.__repo_clients.add_client(self.__client)
        self.__another_id_client = 24
        self.__another_client = Client(self.__another_id_client, self.__another_name, self.__another_cnp)
        self.__repo_clients.add_client(self.__another_client)

        clients = self.__repo_clients.get_all_clients()
        assert len(clients) == 2

        # sortare dupa id:
        clients.sort(key=lambda x: x.get_id_client())

        assert clients[0].get_id_client() == self.__id_client
        assert clients[1].get_id_client() == self.__another_id_client

        assert clients[0].get_name() == self.__name
        assert clients[0].get_cnp() == self.__cnp

        assert clients[1].get_name() == self.__another_name
        assert clients[1].get_cnp() == self.__another_cnp

        print("clients get all repo tests finished successfully!")


    def __run_tests_get_all_clients_service(self):
        print("starting clients get all service tests...")
        clients_path_name = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\ro\\ubb\\rent_movies_app\\tests\\test_clients.csv"
        self.__clear_file(clients_path_name)
        self.__repo_client = FileRepoClients(clients_path_name)

        self.__service_clients = ServiceClients(self.__repo_clients, self.__validator_client)
        assert self.__service_clients.number_of_clients() == 0

        self.__another_id_client = 24
        self.__service_clients.add_client(self.__another_id_client, self.__another_name, self.__another_cnp)
        self.__service_clients.add_client(self.__id_client, self.__name, self.__cnp)
        clients = self.__service_clients.get_all_clients()
        assert len(clients) == 2

        # sortare dupa id:
        clients.sort(key=lambda x: x.get_id_client())

        assert clients[0].get_id_client() == self.__id_client
        assert clients[1].get_id_client() == self.__another_id_client

        assert clients[0].get_name() == self.__name
        assert clients[0].get_cnp() == self.__cnp

        assert clients[1].get_name() == self.__another_name
        assert clients[1].get_cnp() == self.__another_cnp

        print("clients get all service tests finished successfully!")








