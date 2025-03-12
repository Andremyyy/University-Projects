from ro.ubb.rent_movies_app.errors.exceptions import ValidationError


class ValidatorRental:
    def validate_rental(self, rental):
        errors = ""

        year = rental.get_year()
        month = rental.get_month()
        day = rental.get_day()
        # anul apartine [0, 2023]
        if year < 0 or year > 2023:
            errors += "The year is not valid!"

        # luna apartine [1,12]
        if month > 12 or month < 1:
            errors += "The month is not valid!"

        # #ziua apartine [1,31]
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # AN BISECT:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[2] = 29

        if day < 1 or day > days_in_month[month]:
            errors += "The day is not valid!"

        if len(errors):
            raise ValidationError(errors)
