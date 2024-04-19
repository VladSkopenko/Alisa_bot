from re import match

from colorama import Fore

from src.models.field import Field


class Phone(Field):
    """
    Represents a field for phone numbers and provides validation.
    """

    def validate(self, phone_number: str | list[str, ...]) -> str | list[str, ...]:
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
            raise ValueError("Phone must be a string or a list of strings")  # TODO For student


if __name__ == "__main__":
    ...
