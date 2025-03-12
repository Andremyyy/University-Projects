from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, service):
        self.__service = service
        self.__menu = ("\nMenu\n"
                       "1. Rezervarea unei camere sau apartament.\n"
                       "exit\n"
                       "Choose option:\n")

    def run(self):
        while True:
            command = input(self.__menu)
            try:
                if command == '1':
                    self.__ui_rezervare()
                elif command == "exit":
                    return
                else:
                    print("Invalid Command")
            except:
                pass

    def __ui_rezervare(self):
        try:
            id = int(input("Id-ul rezerverii este:"))
            tip = input("Tipul este:")
            check_in = int(input("Check-in date este:"))
            numar_zile = int(input("Numarul de zile este:"))
            self.__service.add_rezervare(id, tip, check_in, numar_zile)
        except ValueError:
            print("trebuie sa fie numere intregi!")
        except ValidatorException as ve:
            print(ve)
        except RepoException as re:
            print(re)