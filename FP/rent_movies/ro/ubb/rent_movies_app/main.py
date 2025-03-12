"""
Scrieți o aplicație pentru o firmă de închiriere de filme.
Aplicația stochează:
 filme: <id>,<titlu>,<descriere>,<gen>,etc
 clienți: <id>, <nume>, <CNP>,etc
Creați o aplicație care permite:
 gestiunea listei de filme și clienți.
 adaugă, șterge, modifică, lista de filme, lista de clienți
 căutare film, căutare clienți.
 Închiriere/returnare filme
 Rapoarte:
 Clienți cu filme închiriate ordonate dupa: nume, după numărul de filme închiriate
 Cele mai inchiriate filme.
 Primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
"""
from ro.ubb.rent_movies_app.repository.repo_clients import FileRepoClients
from ro.ubb.rent_movies_app.repository.repo_movies import FileRepoMovies
from ro.ubb.rent_movies_app.repository.repo_rentals import FileRepoRentals
from ro.ubb.rent_movies_app.service.service_clients import ServiceClients
from ro.ubb.rent_movies_app.service.service_movies import ServiceMovies
from ro.ubb.rent_movies_app.service.service_rentals import ServiceRentals
from ro.ubb.rent_movies_app.tests.tests import Teste
from ro.ubb.rent_movies_app.ui.console import Console
from ro.ubb.rent_movies_app.validate.validator_client import ValidatorClient
from ro.ubb.rent_movies_app.validate.validator_movie import ValidatorMovie
from ro.ubb.rent_movies_app.validate.validator_rental import ValidatorRental

if __name__ == '__main__':

    tests = Teste()
    tests.run_all_tests()

    movie_file_path = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\data\\movies.csv"
    validator_movie = ValidatorMovie()
    repo_movies = FileRepoMovies(movie_file_path)

    client_file_path = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\data\\clients.csv"
    validator_client = ValidatorClient()
    repo_clients = FileRepoClients(client_file_path)

    rental_file_path = "C:\\Users\\ema_a\\PycharmProjects\\rent_movies\\data\\rentals.csv"
    validator_rental = ValidatorRental()
    repo_rentals = FileRepoRentals(rental_file_path)

    service_movies = ServiceMovies(repo_movies, validator_movie)
    service_clients = ServiceClients(repo_clients, validator_client)
    service_rentals = ServiceRentals(repo_rentals, repo_movies, repo_clients, validator_rental)

    ui = Console(service_movies, service_clients, service_rentals)

    ui.run()

    #todo: de revazut meniu si de implementat help command!