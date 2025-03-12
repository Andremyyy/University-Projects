from repository.rezervari_repo import RezervariRepo
from service.rezervari_service import RezervariService
from ui.console import Console
from validator.validate import RezervareValidator

if __name__ == '__main__':

    filepath = "C:\\Users\\ema_a\\PycharmProjects\\hotel_restanta\\rezervari.txt"
    repo = RezervariRepo(filepath)
    validator = RezervareValidator()
    service = RezervariService(repo,validator)
    console = Console(service)
    console.run()