class MostRentedMoviesDTO:

    def __init__(self, id_movie, movie_title, number_of_rentals):
        self.__id_movie = id_movie
        self.__movie_title = movie_title
        self.__number_of_rentals = number_of_rentals

    def get_id_movie(self):
        return self.__id_movie

    def get_movie_title(self):
        return self.__movie_title

    def get_number_of_rentals(self):
        return self.__number_of_rentals

    def __str__(self):
        return f"{self.__id_movie}: The movie {self.__movie_title} has been rented by {self.__number_of_rentals} clients."
