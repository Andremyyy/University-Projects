from ro.ubb.rent_movies_app.domain.movie import Movie
from ro.ubb.rent_movies_app.errors.exceptions import RepositoryError


class RepoMovies:
    # CRUD -> create, return, update, delete
    def __init__(self):
        self._all_movies = {}

    def __len__(self):
        return len(self._all_movies)

    def add_movie(self, movie):
        if movie.get_id_movie() in self._all_movies:
            raise RepositoryError("Movie duplicate id!")
        self._all_movies[movie.get_id_movie()] = movie

    def find_movie_by_id(self, id_movie):
        if id_movie not in self._all_movies:
            raise RepositoryError("This movie does not exist!")
        return self._all_movies[id_movie]

    def get_all_movies(self):
        #lista de elemenete!
        return [self._all_movies[id_student] for id_student in self._all_movies]

    def update_movie(self, movie):
        if self.find_movie_by_id(movie.get_id_movie()) is None:
            raise RepositoryError("The movie does not exist!")
        self._all_movies[movie.get_id_movie()] = movie

    def delete_movie_by_id(self, id_movie):
        if self.find_movie_by_id(id_movie) is None:
            raise RepositoryError("The movie does not exist!")
        del self._all_movies[id_movie]


class FileRepoMovies(RepoMovies):

    def __init__(self, movies_file_path):
        # super().__init__()
        RepoMovies.__init__(self)
        self.__movies_file_path = movies_file_path

    def __len__(self):
        self.__read_all_movies_from_file()
        return RepoMovies.__len__(self)

    def add_movie(self, movie):
        self.__read_all_movies_from_file()
        RepoMovies.add_movie(self, movie)
        self.__append_movie_to_file(movie)

    def find_movie_by_id(self, id_movie):
        self.__read_all_movies_from_file()
        return RepoMovies.find_movie_by_id(self, id_movie)

    def __read_all_movies_from_file(self):
        with open(self.__movies_file_path, 'r') as f:
            self._all_movies.clear()
            lines = f.readlines()    # functie care citeste liniile din fisier
            for line in lines:
                line = line.strip()     # sterge caractele spatiu, \n etc.
                if line != "":
                    pieces = line.split(",")     # separata in parti dupa caracterul virgula "," (csv)
                    #consider ca fisierul nu este corupt si are date valide din punct de vedere al tipului ( int-ul e int etc.)
                    id_movie = int(pieces[0])
                    title = pieces[1]
                    description = pieces[2]
                    genre = pieces[3]
                    #!!!! nu folosi functia de adauga student, CI adauga de mana
                    movie = Movie(id_movie, title, description, genre)
                    self._all_movies[id_movie] = movie

    def __append_movie_to_file(self, movie):
        with open(self.__movies_file_path, "a") as f:
            f.write(str(movie) + "\n")

    def get_all_movies(self):
        self.__read_all_movies_from_file()
        return RepoMovies.get_all_movies(self)

    def update_movie(self, movie):
        self.__read_all_movies_from_file()
        RepoMovies.update_movie(self,movie)
        self.__append_movie_to_file(movie)

    def delete_movie_by_id(self, id_movie):
        self.__read_all_movies_from_file()
        RepoMovies.delete_movie_by_id(self, id_movie)
        self.__save_all_movies_to_file()

    def __save_all_movies_to_file(self):
        with open(self.__movies_file_path, 'w') as f:  # 'w' de la write
            for element in RepoMovies.get_all_movies(self):
                line = f'{element.get_id_movie()},{element.get_title()}, {element.get_description()},{element.get_genre()}'
                f.write(line)
                f.write("\n")

