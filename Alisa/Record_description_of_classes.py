from abc import ABC, abstractmethod
from Decorators.Error_handler import error_handler


class Field(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def change_value(self, new_value):
        pass


class Name(Field):
    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError
        super().__init__(value)

    def __str__(self) -> str:
        return f"{self.value}"

    @error_handler
    def change_value(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise ValueError
        self.value = new_name
