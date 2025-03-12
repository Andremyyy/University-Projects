from domain.entities import Movie


class MovieService:
    def __init__(self, movie_file_repo):
        self.__movie_file_repo = movie_file_repo

    def get_all_movies(self):
        return self.__movie_file_repo.get_all_movies()

    def add(self, id, title, director, year, rating, genre1, genre2, genre3):
        if genre2 != "" and genre3 != "":
            list_genres = genre1 + " "+ genre2 + " "+ genre3
        elif genre2 == "" and genre3 != "":
            list_genres = genre1+" "+genre3
        elif genre2 != "" and genre3 == "":
            list_genres = genre1 + " "+ genre2
        else:
            list_genres = genre1

        movie = Movie(id, title, director, year, list_genres, rating)
        self.__movie_file_repo.add(movie)

    def search(self,title,year):

        lista_completa = self.__movie_file_repo.get_all_movies()

        result = []

        for film in lista_completa:
            if film.get_year() == year and title in film.get_title():
                result.append(film)

        result = sorted(result, key=lambda x:len(x.get_genres()))

        return result

