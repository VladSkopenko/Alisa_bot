from re import match
from abc import ABC, abstractmethod
from datetime import datetime

from colorama import Fore


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



class DataField(Field):
    """
        Represents a field in a data record for name, address, company, or tag.
    """

    def validate(self, new_value: str) -> str:
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        return new_value


class Phone(Field):
    """
    Represents a field for phone numbers and provides validation.
    """

    def validate(self, phone_number: str) -> str:
        pattern = r"^\+?380([0-9]{9}$)|0([0-9]{9}$)"
        if match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError(Fore.BLUE + "Invalid phone number")


class Email(Field):
    """
    Represents a field for email addresses and provides validation.
    """

    def validate(self, email: str) -> str:
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if match(pattern, email):
            return email
        else:
            raise ValueError(Fore.BLUE + "Invalid email")


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
                raise ValueError("Birthday date cannot be in the future")
            return birthday
        except ValueError:
            raise ValueError(Fore.BLUE + "Invalid birthday date, format Year-month-day")


class Record:
    def __init__(self, name: str,
                 phone: str,
                 tag: str = "",
                 email: str = "",
                 birthday: str = "",
                 company: str = "",
                 address: str = ""):
        self.name = DataField(name)
        self.company = DataField(company) if company else ""
        self.address = DataField(address) if address else ""
        self.email = Email(email) if email else ""
        self.birthday = Birthday(birthday) if birthday else ""
        self.phone = []
        self.phone.append(Phone(phone))
        self.tags = []
        self.tags.append(DataField(tag))

    def __str__(self):
        info = f"**Name:** {self.name.value}\n"
        if self.company:
            info += f"**Company:** {self.company.value}\n"
        if self.address:
            info += f"**Address:** {self.address.value}\n"
        if self.email:
            info += f"**Email:** {self.email.value}\n"
        if self.birthday:
            info += f"**Birthday:** {self.birthday.value}\n"
        if self.phone:
            info += f"**Phone:** {', '.join([phone.value for phone in self.phone])}\n"
        if self.tags:
            info += f"**Tags:** {', '.join([tag.value for tag in self.tags])}\n"
        return Fore.BLUE + info

    def to_dict(self):
        record_dict = {
            "name": self.name.value,
            "phone": [phone.value for phone in self.phone],
            "tag": [tag.value for tag in self.tags],
            "email": self.email.value if self.email else None,
            "birthday": self.birthday.value if self.birthday else None,
            "company": self.company.value if self.company else None,
            "address": self.address.value if self.address else None
        }
        return record_dict
