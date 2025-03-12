from exceptions.erori import ValidatorException


class ArtistValidator:
    def validate(self, artist):

        erori = ""

        if artist.get_id() < 0:
            erori += "id invalid"

        if not artist.get_nume()[0].isupper():
            erori += "nume invalid"

        if len(artist.get_categorie()) > 15:
            erori += "categorie invalida"

        if artist.get_tarif() < 0:
            erori += "tarif invalid"

        if len(erori) > 0:
            raise ValidatorException(erori)