from abc import ABC, abstractmethod


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

    def __eq__(self, other):
        return isinstance(other, Field) and self._value.lower() == other.value.lower()
