from abc import ABC, abstractmethod
from Decorators.Error_handler import error_handler


class Field(ABC):

    def __init__(self, value):
        self._value = value

    @abstractmethod
    def __str__(self):
        pass


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self._value = value

    def __str__(self) -> str:
        return f"{self._value}"

    @property
    def get_value(self) -> str:
        return self._value

    @get_value.setter
    @error_handler
    def get_value(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise ValueError()
        self._value = new_name
