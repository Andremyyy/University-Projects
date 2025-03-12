class Movie:
    def __init__(self, id, title, director, year, genres, rating):
        self.__id = id
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genres = genres
        self.__rating = rating

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_director(self):
        return self.__director

    def get_year(self):
        return self.__year

    def get_genres(self):
        return self.__genres

    def get_rating(self):
        return self.__rating

    def __str__(self):
        return f"{self.__id}, {self.__title}, {self.__director},{self.__year},{self.__genres}, {self.__rating}."