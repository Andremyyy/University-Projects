from ro.ubb.rent_movies_app.domain.rental_DTO import RentalDTO
from ro.ubb.rent_movies_app.errors.exceptions import RepositoryError


class RepoRentals:

    def __init__(self):
        self._all_rentals = {}

    def add_rental(self, rental):
        id_rental = rental.get_id_rental()
        if id_rental in self._all_rentals:
            raise RepositoryError("Rental duplicate id!")
        self._all_rentals[id_rental] = rental

    def __len__(self):
        return len(self._all_rentals)

    def get_all_rentals(self):
        return [self._all_rentals[id_rental] for id_rental in self._all_rentals]



class FileRepoRentals(RepoRentals):
    def __init__(self, rentals_file_paths):
        self.__rentals_file_path = rentals_file_paths
        RepoRentals.__init__(self)

    def add_rental(self, rental):
        self.__read_all_rentals_from_file()
        RepoRentals.add_rental(self, rental)
        self.__append_rental_to_file(rental)

    def __read_all_rentals_from_file(self):
        #trebuie folosit rentalDTO
        #in fisier tin doar id-urile
        with open(self.__rentals_file_path, "r") as f:
            self._all_rentals.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(",")
                id_rental = int(parts[0])
                id_movie = int(parts[1])
                id_client = int(parts[2])
                day = int(parts[3])
                month = int(parts[4])
                year = int(parts[5])
                #fac un obiect de tip DTO!!!
                self._all_rentals[id_rental] = RentalDTO(id_rental, id_movie, id_client, day, month, year)

    def __append_rental_to_file(self, rental):
        with open(self.__rentals_file_path, "a") as f:
            f.write(str(rental)+"\n")

    def __len__(self):
        self.__read_all_rentals_from_file()
        return RepoRentals.__len__(self)

    def get__all_rentals(self):
        self.__read_all_rentals_from_file()
        return RepoRentals.get_all_rentals(self)
