from domain.entities import Movie
from exceptions.erori import RepoException


class MovieFileRepo:
    def __init__(self, action_file_path, thriller_file_path, drama_file_path):
        self.__action_file_path = action_file_path
        self.__thriller_file_path = thriller_file_path
        self.__drama_file_path = drama_file_path

        self.__movies = {}

    def get_all_movies(self):

        self.__movies.clear()
        self.__read__action_from_file()
        self.__read__drama_from_file()
        self.__read_thriller_from_file()

        return list(self.__movies.values())

    def __read__action_from_file(self):
        with open(self.__action_file_path, "r") as f:
            # self.__movies.clear()
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                title = parts[1]
                director = parts[2]
                year = int(parts[3])
                genres = (parts[4])
                rating = float(parts[5])



                movie = Movie(id, title, director, year, genres, rating)

                if id not in self.__movies:
                    self.__movies[id] = movie

    def __read__drama_from_file(self):
        with open(self.__drama_file_path, "r") as f:
            # self.__movies.clear()
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                title = parts[1]
                director = parts[2]
                year = int(parts[3])
                genres = parts[4]
                rating = float(parts[5])


                movie = Movie(id, title, director, year, genres, rating)

                if id not in self.__movies:
                    self.__movies[id] = movie

    def __read_thriller_from_file(self):
        with open(self.__thriller_file_path, "r") as f:
            # self.__movies.clear()
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id = int(parts[0])
                title = parts[1]
                director = parts[2]
                year = int(parts[3])
                genres = parts[4]
                rating = float(parts[5])


                movie = Movie(id, title, director, year, genres, rating)

                if id not in self.__movies:
                    self.__movies[id] = movie


    def add(self, movie):

        if movie.get_id() in self.__movies:
            raise RepoException("id duplicat!")

        if "Action" in movie.get_genres():
            self.__read__action_from_file()
            if movie.get_id() in self.__movies:
                raise RepoException("id duplicat!")
            self.__movies[movie.get_id] = movie
            with open(self.__action_file_path, "a") as f:
                f.write(f"{movie.get_id()},{movie.get_title()},{movie.get_director()},{movie.get_year()},{movie.get_genres()},{movie.get_rating()} \n")

        if "Drama" in movie.get_genres():
            self.__read__drama_from_file()
            if movie.get_id() in self.__movies:
                raise RepoException("id duplicat!")
            self.__movies[movie.get_id] = movie
            with open(self.__drama_file_path, "a") as f:
                f.write(f"{movie.get_id()},{movie.get_title()},{movie.get_director()},{movie.get_year()},{movie.get_genres()},{movie.get_rating()} \n")

        if "Thriller" in movie.get_genres():
            self.__read_thriller_from_file()
            if movie.get_id() in self.__movies:
                raise RepoException("id duplicat!")
            self.__movies[movie.get_id] = movie
            with open(self.__thriller_file_path, "a") as f:
                f.write(f"{movie.get_id()},{movie.get_title()},{movie.get_director()},{movie.get_year()},{movie.get_genres()},{movie.get_rating()} \n")




