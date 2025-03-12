from exceptions.erori import ValidatorException


class CafeaValidator:
    def validate(self, cafea):

        erori = ""
        if cafea.get_pret() <= 0:
            erori +="pret invalid"

        if len(erori) > 0:
            raise ValidatorException(erori)