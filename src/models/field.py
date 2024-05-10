from abc import ABC
from abc import abstractmethod


class Field(ABC):
    """
    Abstract class in which the main logic is implemented
    """

    def __init__(self, value: str) -> None:
        """
        The __init__ function is the constructor for a class. It is called when an object of that class
        is instantiated, and it sets up the attributes of that object. In this case, we are setting up
        the attribute _value to be equal to whatever value was passed in as an argument.

        :param self: Represent the instance of the class
        :param value: str: Set the value of the object
        :return: None
        :doc-author: Trelent
        """
        self._value = self.validate(value)

    def __str__(self) -> str:
        """
        The __str__ function is called when you call str() on an object.
        It should return a string representation of the object.
        This is typically used for debugging, so it's common to have a verbose version and a concise one that's used in production.

        :param self: Refer to the current instance of the class
        :return: A string representation of the object
        :doc-author: Trelent
        """
        return f"{self._value}"

    @property
    def value(self) -> str:
        """
        The value function returns the value of a given card.

        :param self: Represent the instance of the class
        :return: A string
        :doc-author: Trelent
        """
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        """
        The value function sets the value of a given instance of the class.
            It takes in a string and returns None.


        :param self: Represent the instance of the class
        :param new_value: str: Pass in a new value to the setter
        :return: A new value for the attribute
        :doc-author: Trelent
        """
        self._value = self.validate(new_value)

    @abstractmethod
    def validate(self, value: str) -> str:
        """
        The validate function is used to validate the value of a parameter.

        :param self: Represent the instance of the class
        :param value: str: Pass the value of the field to be validated
        :return: A string
        :doc-author: Trelent
        """
        pass

    def __eq__(self, other):
        """
        The __eq__ function is a special function that allows us to compare two objects.
        In this case, we are comparing two Field objects.  The __eq__ function returns True if the values of the fields are equal, and False otherwise.

        :param self: Refer to the current instance of a class
        :param other: Compare the value of the current instance with another instance
        :return: True if the two objects are equal, false otherwise
        :doc-author: Trelent
        """
        return isinstance(other, Field) and self._value.lower() == other.value.lower()
