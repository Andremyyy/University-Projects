from domain.validators import ProdusValidator
from file_repo.battery_file_repo import BatteryFileRepo
from file_repo.produs_file_repo import ProdusFileRepo
from service.battery_Service import BatteryService
from service.produs_service import ProdusService
from ui.console import Console

if __name__ == '__main__':
    # try:
        file_path = "C:\\Users\\ema_a\\pythonProject\\magazin\\products.txt"
        battery_file_path = "C:\\Users\\ema_a\\pythonProject\\magazin\\battery_file_path.txt"
        produs_file_repo = ProdusFileRepo(file_path)
        produs_validator = ProdusValidator()
        produs_service = ProdusService(produs_file_repo, produs_validator)

        battery_file_repo = BatteryFileRepo(file_path, battery_file_path)
        battery_service = BatteryService(battery_file_repo, produs_service)
        console = Console(produs_service, battery_service)
        console.run()
    # except Exception as e:
    #     print(f"eroare:{e}")
