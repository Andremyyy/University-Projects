from exceptions.erori import ValidatorException


class ProdusValidator:
    def validate(self, produs):
        erori = ""

        if produs.get_pret() < 0:
            erori += "pret invalid"

        if len(erori) > 0:
            raise ValidatorException(erori)