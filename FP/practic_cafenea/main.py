from repository.cafea_repo import CafeleRepo
from service.cafea_service import CafeleService
from ui.console import Console
from validator.cafea_validator import CafeaValidator

if __name__ == '__main__':
    repo = CafeleRepo()
    validator = CafeaValidator()
    service = CafeleService(repo, validator)
    console = Console(service)
    console.run()