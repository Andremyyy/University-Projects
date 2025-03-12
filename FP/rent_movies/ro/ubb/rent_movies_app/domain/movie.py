class Movie:
    def __init__(self, id_movie, title, description, genre):
        self.__id_movie = id_movie
        self.__title = title
        self.__description = description
        self.__genre = genre

    def get_id_movie(self):
        return self.__id_movie

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_genre(self):
        return self.__genre

    def set_title(self, value):
        self.__title = value

    def set_description(self, value):
        self.__description = value

    def set_genre(self, value):
        self.__genre = value

    def __eq__(self, other):
        #todo: verifica daca tipul lui other e ac cu tipul lui self
        return self.__id_movie == other.__id_movie

    def __str__(self):
        return f"{self.__id_movie},{self.__title},{self.__description},{self.__genre}"