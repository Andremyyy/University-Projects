from repository.cafea_file_repo import CafeaFileRepo
from service.cafea_service import CafeaService
from ui.console import Console
from validator.cafea_validator import CafeaValidator

if __name__ == '__main__':

    file_path = "C:\\Users\\ema_a\\pythonProject\\cafenea_practic_v2\\coffee.txt"

    file_repo = CafeaFileRepo(file_path)
    validator = CafeaValidator()

    service = CafeaService(file_repo, validator)

    console = Console(service)
    console.run()
