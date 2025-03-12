from exceptions.erori import ValidatorException


class CafeaValidator:
    def validate(self, cafea):
        """
        Valideaza un obiect de tip Cafea
        :param cafea: obiect de tip Cafea
        :return: None
        :raises: ValidatorException daca pretul este invalid.
        """
        erori = ""
        if cafea.get_pret() <= 0.0:
            erori += "pret invalid"

        if len(erori) > 0:
            raise ValidatorException(erori)