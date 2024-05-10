from colorama import Fore

from src.models.field import Field


class DataField(Field):
    """
    Represents a field in a data record for name, address, company, or tag.
    """

    def validate(self, new_value: str) -> str:
        """
        The validate function is used to ensure that the value being set for a property
        is of the correct type.  In this case, we are ensuring that it is a string.
        If it isn't, then we raise an exception.

        :param self: Reference the instance of the class
        :param new_value: str: Pass the new value to be validated
        :return: The new_value
        :doc-author: Trelent
        """
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        return new_value.title()
