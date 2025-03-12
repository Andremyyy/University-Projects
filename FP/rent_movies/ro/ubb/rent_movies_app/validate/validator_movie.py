from ro.ubb.rent_movies_app.errors.exceptions import ValidationError


class ValidatorMovie:
    def validate_movie(self, movie):
        errors = ""
        if movie.get_id_movie() <= 0:
            errors += "The id is not valid!\n"
        if not (movie.get_title() and movie.get_title()[0].isupper()):
            errors += "The title is not valid!\n"
        if len(movie.get_description()) > 30:
            errors += "The description is not valid!\n"
        if not (movie.get_genre()):
            errors += "The genre is not valid!"

        if len(errors):
            raise ValidationError(errors)
