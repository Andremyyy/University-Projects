from domain.enitities import Student
from exceptions.erorrs import RepositoryException


class StudentsFileRepository:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__students = {}

    def __read_all_from_file(self):
        with open(self.__filepath, "r") as f:
            self.__students.clear()
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0])
                    nume = parts[1]
                    numar_prezente = int(parts[2])
                    nota = int(parts[3])
                    student = Student(id_student, nume, numar_prezente, nota)
                    self.__students[id_student] = student

    def get_all_students(self):
        self.__read_all_from_file()
        return self.__students.values()

    def add_student(self, student):
        """
        Adauga un student in dictionarul students si il scrie in fisier daca are id-ul unic
        :param student: obiect de tip clasa Student
        :return: None
        :raises: RepositoryException daca exista un alt student cu acel id
        """
        if student.get_id() in self.__students:
            raise RepositoryException("Duplicate id!")
        self.__students[student.get_id()] = student
        with open(self.__filepath, "a") as f:
            f.write(f"{student.get_id()},{student.get_nume()},{student.get_numar_prezente()},{student.get_nota()}\n")

    def update_student_nota(self, student_nou):
        self.__read_all_from_file()
        self.__students[student_nou.get_id()] = student_nou
        self.__save_to_file()

    def __save_to_file(self):
        with open(self.__filepath, "w") as f:
            for student in self.__students.values():
                line = f"{student.get_id()},{student.get_nume()},{student.get_numar_prezente()},{student.get_nota()}"
                f.write(line)
                f.write("\n")


