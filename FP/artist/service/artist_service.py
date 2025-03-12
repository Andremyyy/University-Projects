from domain.entities import Artist


class ArtistService:
    def __init__(self, file_repo, validator):
        self.__file_repo = file_repo
        self.__validator = validator

    def add_artist(self, id, nume, categorie, tarif):

        artist = Artist(id, nume, categorie, tarif)
        self.__validator.validate(artist)
        self.__file_repo.add_artist(artist)

    def get_all_artists(self):
        return self.__file_repo.get_all_artists()

    def categorie_descr_tarif(self, categorie):
        lista_toti_artisti = self.__file_repo.get_all_artists()
        lista_nesortata = []

        for artist in lista_toti_artisti:
            if artist.get_categorie() == categorie:
                lista_nesortata.append(artist)

        lista_sortata = sorted(lista_nesortata, key = lambda x:x.get_tarif(), reverse = True)

        return lista_sortata
