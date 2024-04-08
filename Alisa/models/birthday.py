from datetime import datetime

from colorama import Fore

from Alisa.models.field import Field


class Birthday(Field):
    """
    Represents a field for birthday dates and provides validation.
    """

    def validate(self, birthday: str) -> str:
        """
        Validates the provided birthday date.
        """
        try:
            date_format = "%Y-%m-%d"
            parsed_date = datetime.strptime(birthday, date_format).date()
            if parsed_date > datetime.now().date():
                raise ValueError("Birthday date cannot be in the future")  # todo add color
            return birthday
        except ValueError:
            raise ValueError(Fore.BLUE + "Invalid birthday date, format Year-month-day")
