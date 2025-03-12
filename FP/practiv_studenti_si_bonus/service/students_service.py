from domain.enitities import Student


class StudentsService():
    def __init__(self, repo, validator, filepath):
        self.__repo = repo
        self.__validator = validator
        self.__filepath = filepath

    def get_all_students(self):
        return self.__repo.get_all_students()

    def add_student(self, id_student, nume, numar_prezente, nota):
        """
        Creeaza un student de tip Student si il valideaza
        :param id_student: int
        :param nume: string
        :param numar_prezente: int
        :param nota: int
        :return: None
        """
        student = Student(id_student, nume, numar_prezente, nota)
        self.__validator.validate(student)
        self.__repo.add_student(student)

    def acordare_bonus(self, p, b):
        new_students = {}
        for student in self.get_all_students():
            if student.get_numar_prezente() >= p:
                new_students[student.get_id()] = student

        if len(new_students) == 0:
            print(f"Nu exista studenti cu numarul minim de prezente egal cu {p}")
        else:
            for student in new_students.values():
                copie = b
                nota = student.get_nota()
                ok = False
                while nota < 10 and copie > 0:
                    ok = True
                    nota = nota + 1
                    copie -= 1
                if ok:
                    student_nou = Student(student.get_id(), student.get_nume(), student.get_numar_prezente(), nota)
                    # print(student_nou)
                    self.__validator.validate(student_nou)
                    self.__repo.update_student_nota(student_nou)

                    self.__append_to_file(student_nou)

                else:
                    self.__repo.update_student_nota(student)

    def __append_to_file(self, student_nou):
        with open(self.__filepath, "a") as f:
            line = f'{student_nou.get_id()}, {student_nou.get_nota()}'
            f.write(line)
            f.write("\n")