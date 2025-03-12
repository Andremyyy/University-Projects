from exceptions.erori import ValidatorException


class ProiectValidator:
    def validate(self,proiect):
        erori = ""

        if proiect.get_numar_de_ore() < 0:
            erori += "numar de ore invalid"

        if proiect.get_buget() < 0:
            erori += "buget invalid"

        if len(erori) > 0:
            raise ValidatorException(erori)