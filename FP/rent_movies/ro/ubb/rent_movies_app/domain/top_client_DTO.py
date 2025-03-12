class TopClientDTO:
    def __init__ (self, id_client, client_name, number_of_movies):
        self.__id_client = id_client
        self.__client_name = client_name
        self.__number_of_movies = number_of_movies

    def get_id_client(self):
        return self.__id_client

    def get_client_name(self):
        return self.__client_name

    def get_number_of_movies(self):
        return self.__number_of_movies

    def __str__(self):
        return f"{self.__id_client}:{self.__client_name} has rented {self.__number_of_movies} movies."
