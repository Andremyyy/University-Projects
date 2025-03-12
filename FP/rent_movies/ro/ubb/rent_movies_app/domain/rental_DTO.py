class RentalDTO:
    def __init__(self, id_rental, id_movie, id_client, day, month, year):
        self.__id_rental = id_rental
        self.__id_movie = id_movie
        self.__id_client = id_client
        self.__day = day
        self.__month = month
        self.__year = year

    def get_id_rental(self):
        return self.__id_rental

    def get_id_movie(self):
        return self.__id_movie

    def get_id_client(self):
        return self.__id_client

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"{self.__id_rental},{self.__id_movie},{self.__id_client},{self.__day}, {self.__month}, {self.__year}"
