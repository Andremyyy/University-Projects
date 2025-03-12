from ro.ubb.rent_movies_app.domain.client import Client


class ServiceClients:
    def __init__(self, __repo_clients, __validator_client):
        self.__repo_clients = __repo_clients
        self.__validator_client = __validator_client

    def number_of_clients(self):
        return len(self.__repo_clients)

    def add_client(self, id_client, name, cnp):
        client = Client(id_client, name, cnp)
        self.__validator_client.validate_client(client)
        self.__repo_clients.add_client(client)

    def find_client_by_id(self, id_client):
        return self.__repo_clients.find_client_by_id(id_client)

    def get_all_clients(self):
        return self.__repo_clients.get_all_clients()
