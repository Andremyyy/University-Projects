from domain.entities import Battery


class BatteryService:
    def __init__(self, battery_file_repo, produs_service):
        self.__battery_file_repo = battery_file_repo
        self.__produs_service = produs_service

    def show_products(self):
        return self.__produs_service.show_products()

    def save(self, id, nume, pret, rechargeable):
        battery = Battery(id, nume, pret, rechargeable)

        self.__produs_service.save(id, nume, pret)

        self.__battery_file_repo.save(battery)
