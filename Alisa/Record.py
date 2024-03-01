from abc import ABC, abstractmethod


class Field(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def __str__(self):
        pass


