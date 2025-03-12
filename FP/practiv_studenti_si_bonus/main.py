from domain.validator_student import ValidatorStudent
from repository.students_file_repository import StudentsFileRepository
from service.students_service import StudentsService
from ui.console import Console

if __name__ == '__main__':
    repo = StudentsFileRepository("C:\\Users\\ema_a\\PycharmProjects\\practiv_studenti_si_bonus\\studenti.txt")
    validator = ValidatorStudent()
    filepath = "C:\\Users\\ema_a\\PycharmProjects\\practiv_studenti_si_bonus\\bonus.txt"
    service = StudentsService(repo, validator, filepath)
    console = Console(service)
    console.run()
