from ro.ubb.rent_movies_app.errors.exceptions import ValidationError


class ValidatorClient:
    def validate_client(self, client):
        errors = ""
        if client.get_id_client() <= 0:
            errors += "The id is not valid!\n"
        if not (client.get_name() and client.get_name()[0].isupper()): #e gol sau nu are prima litera mare
            errors += "The name is not valid!\n"
        # pt cnp:
        cnp_is_valid = True
        # lungime cnp:
        if len(client.get_cnp()) != 13:
            # errors += "The CNP is not valid"
            cnp_is_valid = False

        if cnp_is_valid:
            # prima cifra apartine [1,8]
            if int(client.get_cnp()[0]) <= 0 or int(client.get_cnp()[0]) > 8:
                # errors += "The CNP is not valid!"
                cnp_is_valid = False

            year = int(client.get_cnp()[1:3])
            month = int(client.get_cnp()[3:5])
            day = int(client.get_cnp()[5:7])
            # anul apartine [01,99]
            if year == 0:
                # errors += "The CNP is not valid!"
                cnp_is_valid = False

            # luna apartine [01,12]
            if month > 12 or month < 1:
                # errors += "The CNP is not valid!"
                cnp_is_valid = False

            # #ziua apartine [01,31]
            # if day > 31 or int(client.get_cnp()[3:5]) < 1:
            #     errors += "The CNP is not valid!"

            days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # AN BISECT:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month[2] = 29

            if day < 1 or day > days_in_month[month]:
                # errors += "The CNP is not valid!"
                cnp_is_valid = False

        if not cnp_is_valid:
            errors += "The cnp is not valid!"

        if len(errors):
            raise ValidationError(errors)
