from abc import ABC, abstractmethod

from colorama import Fore
from Decorators.Error_handler import error_handler


class Field(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Name(Field):
    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        self.__value = value

    def __str__(self) -> str:
        return f"{self.__value}"

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        self.__value = new_name



