from datetime import datetime

from colorama import Fore

from src.models.field import Field


class Birthday(Field):
    """
    Represents a field for birthday dates and provides validation.
    """

    def validate(self, birthday: str) -> str:
        """
        The validate function is used to validate the birthday date.
            It checks if the date is in a valid format and if it's not in the future.


        :param self: Represent the instance of the class
        :param birthday: str: Pass the birthday date to the function
        :return: The birthday string if the date is valid, otherwise it raises a valueerror
        :doc-author: Trelent
        """
        try:
            date_format = "%Y-%m-%d"
            parsed_date = datetime.strptime(birthday, date_format).date()
            if parsed_date > datetime.now().date():
                raise ValueError(
                    Fore.LIGHTRED_EX + "Birthday date cannot be in the future"
                )
            return birthday
        except ValueError:
            raise ValueError(Fore.BLUE + "Invalid birthday date, format Year-month-day")
