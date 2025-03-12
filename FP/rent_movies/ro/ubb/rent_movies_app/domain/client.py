class Client:

    def __init__(self, __id_client, __name, __cnp):
        self.__id_client = __id_client
        self.__name = __name
        self.__cnp = __cnp

    def get_id_client(self):
        return self.__id_client

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def set_name(self, value):
        self.__name = value

    def set_cnp(self, value):
        self.__cnp = value

    def __eq__(self, other):
        return self.__id_client == other.__id_client

    def __str__(self):
        return f"{self.__id_client},{self.__name},{self.__cnp}"

