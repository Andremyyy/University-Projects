from ro.ubb.rent_movies_app.domain.movie import Movie


class ServiceMovies:
    def __init__(self, __repo_movies, __validator_movie):
        self.__repo_movies = __repo_movies
        self.__validator_movies = __validator_movie

    def add_movie(self, id_movie, title, description, genre):
        movie = Movie(id_movie, title, description, genre)
        #trebuie validate datele:
        self.__validator_movies.validate_movie(movie)
        self.__repo_movies.add_movie(movie)

    def number_of_movies(self):
        return len(self.__repo_movies)

    def find_by_id(self, id_movie):
        return self.__repo_movies.find_movie_by_id(id_movie)

    def get_all_movies(self):
        return self.__repo_movies.get_all_movies()

    def delete_movie_by_id(self, id_movie):
        self.__repo_movies.delete_movie_by_id(id_movie)

    def update_movie(self, id_movie, title, description, genre):
        new_movie = Movie(id_movie, title, description, genre)
        self.__validator_movies.validate_movie(new_movie)
        self.__repo_movies.update_movie(new_movie)
    
    def search_movie_by_title(self, title):
        new_movie_list = []
        for movie in self.__repo_movies.get_all_movies():
            if movie.get_title() == title:
                new_movie_list.append(movie)
        if not new_movie_list:
            raise ValueError("There are no movies with this title")
        return new_movie_list

