from domain.validators import ProiectValidator
from repository.proiect_file_repo import ProiectFileRepo
from service.proeiect_service import ProiectService
from ui.console import Console

if __name__ == '__main__':

    try:
        filepath = "C:\\Users\\ema_a\\pythonProject\\companie_IT\\proiect.txt"
        proiect_validator = ProiectValidator()
        proiect_file_repo = ProiectFileRepo(filepath)
        proiect_service = ProiectService(proiect_file_repo,proiect_validator)
        console = Console(proiect_service)
        console.run()
    except Exception as e:
        print(e)