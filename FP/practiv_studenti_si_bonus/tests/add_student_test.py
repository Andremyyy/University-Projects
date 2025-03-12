import unittest

from domain.validator_student import ValidatorStudent
from exceptions.erorrs import RepositoryException, ValidatorException
from repository.students_file_repository import StudentsFileRepository
from service.students_service import StudentsService


class AddStudentTestCase(unittest.TestCase):
    def setUp(self):
        self.__repo =StudentsFileRepository("C:\\Users\\ema_a\\PycharmProjects\\practiv_var_2\\tests\\add_student_test")
        self.__validator = ValidatorStudent
        self.__filepath = "C:\\Users\\ema_a\\PycharmProjects\\practiv_var_2\\bonus.txt"
        self.__service = StudentsService(self.__repo, self.__validator, self.__filepath)

    def test_add_student(self):
        students = self.__service.get_all_students()
        self.assertEqual(len(students), 3)

        # with self.assertRaises(ValidatorException):
        #     self.__service.add_student(4, "Ionescu", 15, 7)

        duplicate_id_student = 2
        duplicate_name_student = "Margona Maria"
        duplicate_numar_prezente_student = 13
        duplicate_nota = 2

        with self.assertRaises(RepositoryException):
            self.__service.add_student(duplicate_id_student, duplicate_name_student, duplicate_numar_prezente_student,
                                       duplicate_nota)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()