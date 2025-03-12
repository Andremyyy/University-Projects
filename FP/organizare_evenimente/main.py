# Scrieți o aplicație pentru organizarea de evenimente
# Aplicația stochează:
#  persoane: <personID>, <nume>, <adresă>
#  evenimente: <ID>, <dată>, <ora>, <descriere>
# Creați o aplicație care permite:
#  gestiunea listei de persoane și evenimente.
#  adaugă, șterge, modifică, lista de persoane, lista de evenimente
#  căutare persoane, căutare evenimente
#  Înscriere persoană la eveniment.
#  Rapoarte:
#  Primele 20% evenimente cu cei mai mulți participanți (data,ora, număr participanți)
#  Persoane participante la cele mai multe evenimente (top 3 persoane)

#todo:cum se face???
#  Lista de evenimente la care participă o persoană ordonata alfabetic după descriere, după
# dată



from domain.validators import ValidatorPersoana, ValidatorEveniment, ValidatorInscriere
from repository.eveniment_file_repo import EvenimentFileRepo
from repository.inscriere_file_repo import InscriereFileRepo
from repository.persoana_file_repo import PersoanaFileRepo
from service.evenimente_service import EvenimentService
from service.inscriere_service import InscriereService
from service.persoana_service import PersoanaService
from ui.console import Console


if __name__ == '__main__':

    persoana_filepath = "C:\\Users\\ema_a\\PycharmProjects\\organizare_evenimente\\persoana.csv"
    eveniment_filepath = "C:\\Users\\ema_a\\PycharmProjects\\organizare_evenimente\\evenimente.csv"
    inscriere_filepath = "C:\\Users\\ema_a\\pythonProject\\organizare_evenimente\\inscriere.csv"

    persoana_file_repo = PersoanaFileRepo(persoana_filepath)
    eveniment_file_repo = EvenimentFileRepo(eveniment_filepath)
    inscriere_file_repo = InscriereFileRepo(inscriere_filepath)

    validator_persoana = ValidatorPersoana()
    validator_eveniment = ValidatorEveniment()
    validator_inscriere = ValidatorInscriere()

    persoana_service = PersoanaService(persoana_file_repo, validator_persoana)
    eveniment_service = EvenimentService(eveniment_file_repo, validator_eveniment)
    inscriere_service = InscriereService(inscriere_file_repo, validator_inscriere, persoana_file_repo, eveniment_file_repo)

    console = Console(persoana_service, eveniment_service, inscriere_service)
    console.run()
