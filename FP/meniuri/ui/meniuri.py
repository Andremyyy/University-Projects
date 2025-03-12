class Console:
    def __init__(self, service):
        self.__service = service

    def run(self):
        comenzi = self.__create_comenzi()

        while True:
            self.__print_comenzi(comenzi)
            cmd, args = self.__read_comanda()

            if cmd == "exit":
                break
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("comanda neimplementata!")

    def __create_comenzi(self):
        return {
            "add_student": self.__add_student,

        }

    def __print_comenzi(self, comenzi):
        print("Alege comanda: \n ")
        print(*comenzi.keys(), "exit", sep = "\n")

    def __read_comanda(self):
        comanda = input("Comanda ta este:\n")

        pos = comanda.find(" ")

        if pos == -1:
            return comanda,[]

        cmd = comanda[:pos]
        args = comanda[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]

        return cmd, args








