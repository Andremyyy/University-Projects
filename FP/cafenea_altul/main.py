from domain.validator import CafeaValidator
from repository.cafea_file_repo import CafeaFileRepo
from service.cafea_service import CafeaService
from ui.console import Console


if __name__ == '__main__':
    try:
        file_path = "C:\\Users\\ema_a\\pythonProject\\cafenea_altul\\cafea.txt"

        cafea_validator = CafeaValidator()
        cafea_file_repo = CafeaFileRepo(file_path)
        cafea_service = CafeaService(cafea_file_repo, cafea_validator)
        console = Console(cafea_service)
        console.run()
    except Exception as e:
        print(e)