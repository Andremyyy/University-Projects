from exceptions.erori import ValidatorException, RepoException


class Console:
    def __init__(self, proiect_service):
        self.__proiect_service = proiect_service
        self.__menu = (
            "\nMenu:\n"
            "1 Adaugare proiect\n"
            "2 Afiseaza proiect\n"
            "3 Afisarea proiectelor in ord descrescatoare in functie de numarul de ore necesare\n"
            "exit\n"
            "4 Update proiect\n"
            "5 Delete proiect\n"
            "Alege comanda:\n"
        )

    def run(self):

        while True:
            comanda = input(self.__menu)

            if comanda == "1":
                self.__add_proiect()
            elif comanda == '2':
                self.__print_proiecte()
            elif comanda == "3":
                self.__sort_proiecte_dupa_ore()
            elif comanda == "4":
                self.__update_proiect()
            elif comanda == "5":
                self.__delete_proiect()
            elif comanda == "exit":
                break
            else:
                print("Comanda neimplementata!")
    def __add_proiect(self):
        try:
            id = int(input("Id-ul proiectului:"))
            nume = input("numele proiectului:")
            numar_de_ore_necesare = int(input("numarul de ore necesare:"))
            buget_per_colaborator = int(input("bugetul per colaborator:"))
            nume_client = input("nume client:")
            self.__proiect_service.add_proiect(id,nume,numar_de_ore_necesare,buget_per_colaborator,nume_client)
        except ValueError:
            print("datele trebuie sa fie intregi!!!")
        except ValidatorException as ve:
            print(f"eroare validare:{ve}")
        except RepoException as re:
            print(f"eroare repo:{re}")


    def __print_proiecte(self):
        lista = self.__proiect_service.print_proiecte()

        if len(lista) == 0:
            print("Nu exista proiecte!")
            return

        for proiect in lista:
            print(proiect)

    def __sort_proiecte_dupa_ore(self):
        lista = self.__proiect_service.sort_proiecte_dupa_ore()

        if len(lista) == 0:
            print("Nu exista proiecte!")
            return

        for proiect in lista:
            print(proiect)

    def __update_proiect(self):
        try:
            id = int(input("id-ul proiectului de modificat este:"))
            nume_nou = input("numele proiectului:")
            numar_de_ore_necesare_nou = int(input("numarul de ore necesare:"))
            buget_per_colaborator_nou = int(input("bugetul per colaborator:"))
            nume_client_nou = input("nume client:")
            self.__proiect_service.update_proiect(id, nume_nou,numar_de_ore_necesare_nou,buget_per_colaborator_nou,nume_client_nou)
        except ValueError:
            print("id-ul, numar de ore si bugetul trebuie sa fie intregi!")
        except RepoException as re:
            print(f"eroare repo: {re}")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")

    def __delete_proiect(self):
        try:
            id = int(input("id-ul proiectului de modificat este:"))
            self.__proiect_service.delete_proiect(id)
        except ValueError:
            print("id-ul trebuie sa fie intreg!")
        except RepoException as re:
            print(f"eroare repo: {re}")
        except ValidatorException as ve:
            print(f"eroare validare: {ve}")
