from exceptions.erorrs import ValidatorException


class ValidatorStudent:
    def validate(self, student):
        """
        Valideaza un student
        :param student: obiect de tip clasa Student
        :return: None
        :raises ValidatorException daca numele sau numarul de prezente sau nota este invalida
        """
        errors = ""
        if len(student.get_nume().split()) < 2:
            errors += "nume invalid!\n"
        else:
            last_name, first_name = student.get_nume().split(" ")
            if len(last_name) < 3 or len(first_name) < 3:
                errors += "nume invalid!\n"

        if student.get_numar_prezente() < 0:
            errors += "numar prezente invalid!\n"

        if (student.get_nota() > 10) or (student.get_nota() < 0):
            errors += "nota invalida!\n"

        if len(errors) > 0:
            raise ValidatorException(errors)
