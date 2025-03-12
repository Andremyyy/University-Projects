from repo.movie_file_repo import MovieFileRepo
from service.movie_service import MovieService
from ui.console import Console

if __name__ == '__main__':
    try:
        action_movies_file = "C:\\Users\\ema_a\\pythonProject\\PRACTIC\\action-movies.txt"
        thriller_movies_file = "C:\\Users\\ema_a\\pythonProject\\PRACTIC\\thriller-movies.txt"
        drama_movies_file = "C:\\Users\\ema_a\\pythonProject\\PRACTIC\\drama-movies.txt"

        movie_file_repo = MovieFileRepo(action_movies_file,thriller_movies_file,drama_movies_file)
        movie_service = MovieService(movie_file_repo)
        console = Console(movie_service)
        console.run()
    except Exception as e:
        print(e)