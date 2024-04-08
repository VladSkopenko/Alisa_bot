from re import match

from colorama import Fore

from Alisa.models.field import Field


class Email(Field):
    """
    Represents a field for email addresses and provides validation.
    """

    def validate(self, email: str) -> str:
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if match(pattern, email):
            return email
        else:
            raise ValueError(Fore.BLUE + "Invalid email")
