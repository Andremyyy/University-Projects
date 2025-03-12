from exceptions.errors import ValidatorException


class CafeaValidator:
    def validate(self, cafea):
        erori = ""
        if len(cafea.get_nume()) < 3 or not cafea.get_nume()[0].isupper():
            erori += "nume invalid\n"
        if cafea.get_pret() < 0:
            erori += "pret invalid\n"
        if cafea.get_tara()[0].islower():
            erori += "tara invalida\n"

        if len(erori) > 0:
            raise ValidatorException(erori)