from domain.entities import Artist
from exceptions.erori import RepoException


class ArtistFileRepo:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__artisti = {}

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self.__artisti.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    return
                parts = line.split(",")
                id = int(parts[0])
                nume = parts[1]
                categorie = parts[2]
                tarif = float(parts[3])

                artist = Artist(id, nume, categorie, tarif)

                self.__artisti[id] = artist

    def add_artist(self, artist):
        self.__read_all_from_file()
        if artist.get_id() in self.__artisti:
            raise RepoException("id duplicat!")
        self.__artisti[artist.get_id()] = artist
        with open(self.__file_path, "a") as f:
            f.write(f"{artist.get_id()},{artist.get_nume()},{artist.get_categorie()},{artist.get_tarif()}\n")

    def get_all_artists(self):
        self.__read_all_from_file()
        return list(self.__artisti.values())