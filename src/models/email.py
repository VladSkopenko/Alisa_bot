from re import match

from colorama import Fore

from src.models.field import Field


class Email(Field):
    """
    Represents a field for email addresses and provides validation.
    """

    def validate(self, email: str) -> str:
        """
        The validate function takes in a string and checks if it is a valid email address.
        If the string is not an email, then it raises an error. If the string is an email,
        then it returns that same string.

        :param self: Represent the instance of the class
        :param email: str: Pass the email address to the function
        :return: The email address if it is valid, and raises an error otherwise
        :doc-author: Trelent
        """
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if match(pattern, email):
            return email
        else:
            raise ValueError(Fore.BLUE + "Invalid email")
