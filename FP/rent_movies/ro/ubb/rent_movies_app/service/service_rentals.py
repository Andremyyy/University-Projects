import math

from ro.ubb.rent_movies_app.domain.most_rented_movies_DTO import MostRentedMoviesDTO
from ro.ubb.rent_movies_app.domain.rental import Rental
from ro.ubb.rent_movies_app.domain.rental_DTO import RentalDTO
from ro.ubb.rent_movies_app.domain.top_client_DTO import TopClientDTO


class ServiceRentals:
    def __init__(self, repo_rentals, repo_movies, repo_clients, validator_rental):
        self.__repo_rentals = repo_rentals
        self.__repo_movies = repo_movies
        self.__repo_clients = repo_clients
        self.__validator_rental = validator_rental

    def add_rental(self, id_rental, id_movie, id_client, day, month, year):
        #prima data verific daca exista filmul si clientul:
        self.__repo_movies.find_movie_by_id(id_movie)
        self.__repo_clients.find_client_by_id(id_client)
        #daca trece de liniile precedente fara sa arunce eroare => am filmul si clientul pentru care vreau sa adaug o inchiriere

        rental = RentalDTO(id_rental, id_movie, id_client, day, month, year)
        #validez:
        self.__validator_rental.validate_rental(rental)
        self.__repo_rentals.add_rental(rental)

    def number_of_rentals(self):
        return len(self.__repo_rentals)

    def get_all_rentals(self):
        rentals_dtos = self.__repo_rentals.get_all_rentals()
        result = []
        for rental_dto in rentals_dtos:
            movie = self.__repo_movies.find_movie_by_id(rental_dto.get_id_movie())
            client = self.__repo_clients.find_client_by_id(rental_dto.get_id_client())
            rental = Rental(rental_dto.get_id_rental(), movie, client, rental_dto.get_day(), rental_dto.get_month(), rental_dto.get_year())
            result.append(rental)
        return result

    def __calculate_all_movies_client(self):
        all_movies_clients = {}
        rentals_dtos = self.__repo_rentals.get_all_rentals()
        for rental_dto in rentals_dtos:
            id_client = rental_dto.get_id_client()
            if id_client not in all_movies_clients:
                all_movies_clients[id_client] = 0
            all_movies_clients[id_client] += 1
        return all_movies_clients

    def top_30_percentage_clients(self):
        all_movies_clients = self.__calculate_all_movies_client()
        result = []
        for id_client in all_movies_clients:
            client_number_of_movies = all_movies_clients[id_client]
            client_name = self.__repo_clients.find_client_by_id(id_client).get_name()
            top_k_client_dto = TopClientDTO(id_client, client_name, client_number_of_movies)
            result.append(top_k_client_dto)

        result.sort(key=lambda x: x.get_number_of_movies(), reverse=True)

        top_30_percentage_clients_index = math.ceil(len(result) * 0.3)

        return result[:top_30_percentage_clients_index]

    def top_rented_movies(self):
        all_movies = self.__calculate_top_rented_movies()
        result = []
        for id_movie in all_movies:
            number_of_rentals = all_movies[id_movie]
            movie_title = self.__repo_movies.find_movie_by_id(id_movie).get_title()
            all_movies_dto = MostRentedMoviesDTO(id_movie, movie_title, number_of_rentals)
            result.append(all_movies_dto)

        result.sort(key=lambda x: x.get_number_of_rentals(), reverse = True)

        return result[:1]

    def __calculate_top_rented_movies(self):

        all_movies = {}
        rentals_dtos = self.__repo_rentals.get_all_rentals()
        for rental_dto in rentals_dtos:
            id_movie = rental_dto.get_id_movie()
            if id_movie not in all_movies:
                all_movies[id_movie] = 0
            all_movies[id_movie] += 1
        return all_movies




