class Rental:
    def __init__(self, id_rental, movie, client, day, month, year):
        self.__id_rental = id_rental
        self.__movie = movie
        self.__client = client
        self.__day = day
        self.__month = month
        self.__year = year

    def get_id_rental(self):
        return self.__id_rental

    def get_client(self):
        return self.__client

    def get_movie(self):
        return self.__movie

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def set_movie(self, value):
        self.__movie = value

    def set_client(self, value):
        self.__client = value

    def set_day(self, value):
        self.__day = value

    def set_month(self, value):
        self.__month = value

    def set_year(self, value):
        self.__year = value

    def __str__(self):
        return f"{self.__id_rental}.{self.__client.get_name()} has rented the movie {self.__movie.get_title()} on {self.__day}.{self.__month}.{self.__year}"
