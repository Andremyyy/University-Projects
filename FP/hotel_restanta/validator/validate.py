from exceptions.erori import ValidatorException


class RezervareValidator:

    def validate(self, rezervare):
        erori = ""

        if rezervare.get_id() <= 0:
            erori += "id invalid"

        if rezervare.get_tip() not in ["single", "double", "apartament"]:
            erori += "tip invalid"

        if rezervare.get_check_in_date() < 1 or rezervare.get_check_in_date > 31:
            erori += "check-in date invalida"

        if len(erori) > 0:
            raise ValidatorException(erori)
