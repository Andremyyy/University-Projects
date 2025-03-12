class Rezervare:
    def __init__(self, id, tip, check_in_date, numar_zile):
        self.__id = id
        self.__tip = tip
        self.__check_in_date = check_in_date
        self.__numar_zile = numar_zile

    def get_tip(self):
        return self.__tip

    def get_id(self):
        return self.__id

    def get_check_in_date(self):
        return self.__check_in_date

    def get_numar_zile(self):
        return self.__numar_zile

    def __str__(self):
        return f"{self.__id} Camera {self.__tip} a fost rezervata de pe {self.__check_in_date} iulie pentru {self.__numar_zile} zile"