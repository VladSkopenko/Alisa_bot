import re
from abc import ABC

from colorama import Fore


class Field(ABC):
    """
       This is a simple abstract class
    """
    def __init__(self, value: str) -> None:
        self._value = value

    def __str__(self):
        return f'{self._value}'


class DataField(Field):
    """
       This class is needed for contact fields, it will be used for name, address, company, tag
    """
    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        self._value = new_value


class Phone(Field):
    """
        This class is needed to validate the phone number and functionality associated with it
    """
    def __init__(self, value: str) -> None:
        super().__init__(self.valid_phone(value))

    @staticmethod
    def valid_phone(phone_number: str) -> str:
        pattern = r"^\+?380([0-9]{9}$)|0([0-9]{9}$)"
        if re.match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError(Fore.BLUE + "Invalid phone number")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_phone):
        valid_phone = self.valid_phone(new_phone)
        self._value = valid_phone


