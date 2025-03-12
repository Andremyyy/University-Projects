from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, produs_service, battery_service):
        self.__produs_service = produs_service
        self.__battery_service = battery_service

    def run(self):
        comenzi = self.__create_comenzi()

        while True:
            self.__print_comenzi(comenzi)

            cmd, args = self.__read_comanda()

            if cmd == "exit":
                return
            try:
                comenzi[cmd](*args)
            except KeyError:
                print("comanda neimplementata!")

    def __create_comenzi(self):
        return {
            "show-products": self.__show_products,
            "save": self.__save,
            "delete-product": self.__delete_product,
            "update-product": self.__update_product
        }

    def __show_products(self):
        lista = self.__produs_service.show_products()

        if len(lista) == 0:
            print("Nu exista produse")
            return

        for produs in lista:
            print(produs)

    def __print_comenzi(self, comenzi):
        print("\nMenu: \n")
        print(*comenzi, "exit", sep = "\n")

    def __read_comanda(self):
        comanda = input("Alege comanda: \n")
        pos = comanda.find(" ")
        if pos == -1:
            return comanda, []

        cmd = comanda[:pos]
        args = comanda[pos:]
        args = args.split(",")
        args = [s.strip() for s in args]

        return cmd, args

    def __save(self, id, nume, pret):
        try:
            id = int(id)
            pret = float(pret)
            self.__produs_service.save(id, nume, pret)
        except ValueError:
            print("id-ul trebuie sa fie int, pretul trebuie sa fie float!!!")
        except ValidatorException as ve:
            print(f"eroare validare:{ve}")
        except RepoException as re:
            print(f"eroare repo: {re}")

    # def __save(self, id, nume, pret, rechargeable):
    #     try:
    #         id = int(id)
    #         pret = float(pret)
    #         rechargeable = bool(rechargeable)
    #         self.__produs_service.save(id, nume, pret)
    #         self.__battery_service.save(id,nume,pret, rechargeable)
    #     except ValueError:
    #         print("id-ul trebuie sa fie int, pretul trebuie sa fie float, rechargeable de tip bool!!!")
    #     except ValidatorException as ve:
    #         print(f"eroare validare:{ve}")
    #     except RepoException as re:
    #         print(f"eroare repo: {re}")
    def __delete_product(self, id):
        try:
            id = int(id)
            self.__produs_service.delete_produs(id)
        except ValueError:
            print("id invalid!")
        except RepoException as re:
            print(f"eroare repo: {re}")

    def __update_product(self, id, nume_nou, pret_nou):
        try:
            id = int(id)
            pret_nou = float(pret_nou)
            self.__produs_service.update_produs(id, nume_nou, pret_nou)
        except ValueError:
            print("date invalide")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")
        except RepoException as re:
            print(f"eroare repo: {re}")




