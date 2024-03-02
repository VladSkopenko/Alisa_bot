from abc import ABC, abstractmethod
from datetime import datetime
from re import match

from colorama import Fore
from prettytable import PrettyTable


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


class DataField(Field):
    """
    Represents a field in a data record for name, address, company, or tag.
    """

    def validate(self, new_value: str) -> str:
        if not isinstance(new_value, str):
            raise ValueError(Fore.BLUE + "Value must be a string")
        return new_value.title()


class Phone(Field):
    """
    Represents a field for phone numbers and provides validation.
    """

    def validate(self, phone_number: str | list[str, ...]) -> str | list[str, ...]:
        if isinstance(phone_number, str):
            pattern = r"^\+?380([0-9]{9}$)|0([0-9]{9}$)"
            if match(pattern, phone_number):
                return phone_number
            else:
                raise ValueError(Fore.BLUE + "Invalid phone number")
        elif isinstance(phone_number, list):
            validated_numbers = []
            for number in phone_number:
                validated_numbers.append(self.validate(number))
            return validated_numbers
        else:
            raise ValueError("Phone must be a string or a list of strings")


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
    """
    The Record class represents a contact entry with information about a person, including their name, contact details
    """
    def __init__(self, name: str,
                 phone: str,
                 tag: str = "",
                 email: str = "",
                 birthday: str = "",
                 company: str = "",
                 address: str = "",
                 id_user: int = None
                 ):
        self.name = DataField(name)
        self.company = DataField(company) if company else ""
        self.address = DataField(address) if address else ""
        self.email = Email(email) if email else ""
        self.birthday = Birthday(birthday) if birthday else ""
        self.phone = []
        if isinstance(phone, str):
            self.phone.append(Phone(phone))
        elif isinstance(phone, list):
            self.phone.extend(Phone(phon) for phon in phone)
        self.tags = []
        if isinstance(tag, str):
            self.tags.append(DataField(tag))
        elif isinstance(tag, list):
            self.tags.extend(DataField(t) for t in tag)
        self.id_user = id_user

    def __str__(self):
        table = PrettyTable()
        table.field_names = ["Id", "Name", "Company", "Email", "Birthday", "Phone", "Tags", "Address"]

        table.add_row([
            self.id_user,
            self.name.value,
            self.company.value if self.company else "",
            self.email.value if self.email else "",
            self.birthday.value if self.birthday else "",
            ", ".join([phone.value for phone in self.phone]) if self.phone else "",
            ", ".join([tag.value for tag in self.tags]) if self.tags else "",
            self.address.value if self.address else ""
        ])

        return Fore.BLUE + str(table)

    def assign_id(self, id_value):
        self.id_user = id_value

    def to_dict(self):
        record_dict = {
            "id_user": self.id_user,
            "name": self.name.value,
            "phone": [phone.value for phone in self.phone],
            "tag": [tag.value for tag in self.tags],
            "email": self.email.value if self.email else None,
            "birthday": self.birthday.value if self.birthday else None,
            "company": self.company.value if self.company else None,
            "address": self.address.value if self.address else None
        }
        return record_dict

    def update_field(self, field_name: str, old_value: str, new_value: str) -> None:

        """
        A universal method, it takes a name and changes the values in the list, if any, while maintaining the validation
        """
        field = getattr(self, field_name)
        if field:
            if isinstance(field, list):
                for item in field:
                    if item.value == old_value:
                        item.value = new_value
                        return
            else:
                if field.value == old_value:
                    field.value = new_value
        else:
            raise AttributeError(f"Field {field_name} not found in record")


if __name__ == "__main__":
    test_contact = Record(
        name="Vlad",
        phone="0963610573",
        email="skoper@afkas.com",
        tag="Student",
        address="lavatorial 34",
        company="go it",
        birthday="2000-01-28",
        id_user=None,
    )
    print(test_contact)
