from re import match

from colorama import Fore

from src.models.field import Field


class Phone(Field):
    """
    Represents a field for phone numbers and provides validation.
    """

    def validate(self, phone_number: str | list[str, ...]) -> str | list[str, ...]:
        """
        The validate function takes a phone number as an argument and checks if it is valid.
        If the phone number is valid, it returns the same phone number. If not, it raises a ValueError.

        :param self: Represent the instance of the class
        :param phone_number: str | list[str: Check if the phone number is a string or a list of strings
        :param ...]: Specify that the list can contain any number of elements
        :return: A string or a list of strings
        :doc-author: Trelent
        """
        if isinstance(phone_number, str):
            pattern = r"^\+?380([0-9]{9}$)|0([0-9]{9}$)"
            if match(pattern, phone_number):
                return phone_number
            else:
                raise ValueError(Fore.BLUE + "Invalid phone number")
        elif isinstance(phone_number, list):
            validated_numbers = []
            for number in phone_number:
                validated_numbers.append(self.validate(number))
            return validated_numbers
        else:
            raise ValueError(
                Fore.LIGHTRED_EX + "Phone must be a string or a list of strings"
            )


if __name__ == "__main__":
    ...
