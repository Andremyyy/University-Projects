from domain.validators import ArtistValidator
from repository.artist_file_repo import ArtistFileRepo
from service.artist_service import ArtistService
from ui.console import Console




if __name__ == '__main__':
    try:
        file_path = "C:\\Users\\ema_a\\pythonProject\\artist\\artist.txt"

        artist_validator = ArtistValidator()
        artist_file_repo = ArtistFileRepo(file_path)
        artist_service = ArtistService(artist_file_repo,artist_validator)
        console = Console(artist_service)
        console.run()
    except Exception as e:
        print(e)