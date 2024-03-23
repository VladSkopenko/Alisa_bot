from Alisa.models.Field import Field
from colorama import Fore


class DataField(Field):
    """
    Represents a field in a data record for name, address, company, or tag.
    """

    def validate(self, new_value: str) -> str:
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        return new_value.title()
