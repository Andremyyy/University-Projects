from ro.ubb.rent_movies_app.domain.client import Client
from ro.ubb.rent_movies_app.errors.exceptions import RepositoryError


class RepoClients:
    def __init__(self):
        self._all_clients = {}

    def __len__(self):
        return len(self._all_clients)

    def add_client(self, client):
        id_client = client.get_id_client()
        if id_client in self._all_clients:
            raise RepositoryError("Client duplicate id!")
        self._all_clients[id_client] = client

    def find_client_by_id(self, id_client):
        if id_client not in self._all_clients:
            raise RepositoryError("This client does not exist!")
        return self._all_clients[id_client]

    def get_all_clients(self):
        # lista de element
        return [self._all_clients[id_client] for id_client in self._all_clients]

class FileRepoClients(RepoClients):
    def __init__(self, clients_file_path):
        # super().__init__()
        RepoClients.__init__(self)
        self.__clients_file_path = clients_file_path

    def __len__(self):
        self.__read_all_clients_from_file()
        return RepoClients.__len__(self)

    def __read_all_clients_from_file(self):
        with open(self.__clients_file_path, "r") as f:
            self._all_clients.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                id_client = int(parts[0])
                name = parts[1]
                cnp = parts[2]
                self._all_clients[id_client] = Client(id_client, name, cnp)

    def add_client(self, client):
        self.__read_all_clients_from_file()
        RepoClients.add_client(self,client)
        self.__append_client_to_file(client)

    def __append_client_to_file(self, client):
        with open(self.__clients_file_path, 'a') as f: #'a' de la append
            f.write(str(client)+"\n")

    def find_client_by_id(self, id_client):
        self.__read_all_clients_from_file()
        return RepoClients.find_client_by_id(self, id_client)

    def get_all_clients(self):
        self.__read_all_clients_from_file()
        return RepoClients.get_all_clients(self)