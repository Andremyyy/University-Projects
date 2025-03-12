from datetime import datetime

from exceptions.erori import PersoanaValidatorException, EvenimentValidatorException, InscriereValidatorException


class ValidatorPersoana:
    def validate(self, persoana):

        erori = ""

        if persoana.get_id() <= 0:
            erori += "id invalid"
        if len(persoana.get_nume()) < 2:
            erori += "nume invalid"
        else:
            lastname, firstname = persoana.get_nume().split(" ")
            if lastname[0].islower() or firstname[0].islower():
                erori += "nume invalid"
        if len(persoana.get_adresa()) > 30:
            erori += "adresa invalida"

        if len(erori) > 0:
            raise PersoanaValidatorException(erori)


class ValidatorEveniment:

    def validate(self, eveniment):

        erori = ""

        if eveniment.get_id() <= 0:
            erori += "id invalid"

        date_format = "%d.%m.%Y"

        if not datetime.strptime(eveniment.get_data(), date_format):
            erori += "data invalida"

        ora_format = "%H:%M"

        if not datetime.strptime(eveniment.get_ora(), ora_format):
            erori += "ora invalida"

        if len(eveniment.get_descriere()) > 30:
            erori += "descriere invalida"

        if len(erori) > 0:
            raise EvenimentValidatorException(erori)


class ValidatorInscriere:
    def validate(self, inscriere):
        erori = ""

        if inscriere.get_id_inscriere() <= 0:
            erori += "id invalid"

        if inscriere.get_pret() <= 0:
            erori += "pret invalid"

        if len(erori) > 0:
            raise InscriereValidatorException(erori)
