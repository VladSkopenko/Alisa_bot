import re
from abc import ABC, abstractmethod

from colorama import Fore


class Field(ABC):
    """
    Abstract class in which the main logic is implemented
    """

    def __init__(self, value: str) -> None:
        self._value = self.validate(value)

    def __str__(self) -> str:
        return f"{self._value}"

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        self._value = self.validate(new_value)

    @abstractmethod
    def validate(self, value: str) -> str:
        pass


class DataField(Field):
    """
        Represents a field in a data record for name, address, company, or tag.
    """

    def validate(self, new_value: str) -> str:
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        return new_value


class Phone(Field):
    """
    Represents a field for phone numbers and provides validation.
    """

    def validate(self, phone_number: str) -> str:
        pattern = r"^\+?380([0-9]{9}$)|0([0-9]{9}$)"
        if re.match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError(Fore.BLUE + "Invalid phone number")


class Email(Field):
    """
    Represents a field for email addresses and provides validation.
    """

    def validate(self, email: str) -> str:
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            raise ValueError(Fore.BLUE + "Invalid email")



