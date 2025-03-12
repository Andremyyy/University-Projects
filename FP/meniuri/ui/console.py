class Console:
    def __init__(self, service):
        self.__service = service

    #MENIU CU COMENZI:

    def run(self):
        commands = self.__create_commands()

        while True:
            self.__print_all_commands(commands)
            cmd, args = self.__read_commands()

            if cmd == "exit":
                break
            try:
                commands[cmd](*args)
            except KeyError as ke:
                print("Option is not implemented yet!!", ke)

            # commands[cmd](*args)


    def __create_commands(self):
        return {
            "add_student": self.__add_student,
            "print_all_students": self.__print_students
        }

    def __add_student(self, id, nume, nr_prezente, nota):
        try:
            id = int(id)
            nr_prezente = int(nr_prezente)
            nota = int(nota)
        except ValueError:
            print("datele trebuie sa fie intregi!!!")

    def __print_students(self):
        pass

    def __print_all_commands(self, commands):
        print("\nChoose command:\n")
        print(*commands.keys(), "exit", sep = "\n")

    def __read_commands(self):
        command = input("Your command is:\n")

        pos = command.find(" ")

        if pos == -1:
            return command, []

        cmd = command[:pos]
        args = command[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]

        return cmd, args

    #MENIU FARA COMENZI:

    #def __init__(self, service)
        # self.__service = service
        # self.__menu = ("\nMenu\n"
        #                "1 Adauga student"
        #                "....."
        #                "exit"
        #                "Comanda ta este: \n")

    # def run(self):
    #
    #     while True:
    #         command = input(self.__menu)
    #
    #         if command == "1":
    #             self.__add_student()
    #         elif command == "exit":
    #             break
    #         else:
    #             print("Comanda nu este implementata inca!")



