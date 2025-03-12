from exceptions.erorrs import ValidatorException, RepositoryException


class Console:
    def __init__(self, service):
        self.__service = service
        self.__menu = ("\nMenu:\n"
                       "1.read all students\n"
                       "2.add student\n"
                       "3.acordare bonus\n"
                       "exit\n"
                       "What's your command? \n")
        
    def run(self):
        while True:
            command = input(self.__menu)
            try:
                if command == "1":
                    self.__ui_real_all_students()
                elif command == "2":
                    self.__ui_add_student()
                elif command == "3":
                    self.__ui_acordare_bonus()
                elif command == "exit":
                    break
                else:
                    print("Invalid command!")
            except ValidatorException as ve:
                print(f"eroare validare: {ve}")
            except RepositoryException as re:
                print(f"eroare repository: {re}")

    def __ui_real_all_students(self):
        students = self.__service.get_all_students()
        if len(students) == 0:
            print("There are no students!")
            return
        for student in students:
            print(student)

    def __ui_add_student(self):
        try:
            id_student = int(input("the id of the student is: "))
            nume = input("the name of the student is:")
            numar_prezente = int(input("the number of prezente is:"))
            nota = int(input("the grade is:"))
            self.__service.add_student(id_student, nume, numar_prezente, nota)
        except ValueError:
            print("id_student, numar_prezente, nota should be a number!")
        except RepositoryException as re:
            print(f"eroare repository:{re}")
        except ValidatorException as ve:
            print(f"eroare validare:{ve}")

    def __ui_acordare_bonus(self):
        try:
            p = int(input("Minimul de prezente este: "))
            b = int(input("Bonusul este: "))
            self.__service.acordare_bonus(p, b)
        except ValueError:
            print("trebuie sa fie numere intregi!")




