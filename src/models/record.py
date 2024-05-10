from colorama import Fore

from src.decorators.table_decorator import table_decorator
from src.models.birthday import Birthday
from src.models.data_field import DataField
from src.models.email import Email
from src.models.phone import Phone


class Record:
    """
    The Record class represents a contact entry with information about a person, including their name, contact details
    """

    __headers = ["Name", "Company", "Email", "Birthday", "Phone", "Tags", "Address"]

    def __init__(
        self,
        name: str,
        phone: str,
        tag: str = "",
        email: str = "",
        birthday: str = "",
        company: str = "",
        address: str = "",
    ):
        """
        The __init__ function is the constructor for a class. It initializes all of the attributes
        of an object when it is created. The __init__ function takes in parameters that are used to
        initialize each attribute of an object.

        :param self: Refer to the object itself
        :param name: str: Set the name of the contact
        :param phone: str: Create a new phone object, which is then appended to the phone list
        :param tag: str: Create a list of tags
        :param email: str: Set the email attribute of the contact class
        :param birthday: str: Create a birthday object
        :param company: str: Create a datafield object with the company name
        :param address: str: Create an address object
        :param : Create a new instance of the class
        :return: An object of type contact
        :doc-author: Trelent
        """
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

    @table_decorator(__headers)
    def __str__(self):
        """
        The __str__ function is a special function in Python that defines the &quot;informal&quot; or nicely printable string representation of an object.
        This means that if you type the name of an instance of your class at the Python prompt, it will call __str__() and print the return value.
        It's also used by functions and methods that convert objects to strings such as str().

        :param self: Represent the instance of the class
        :return: The name, company, email, birthday and address of the contact
        :doc-author: Trelent
        """
        return [
            [
                self.name,
                self.company,
                self.email,
                self.birthday,
                [phone.value for phone in self.phone],
                [tag.value for tag in self.tags],
                self.address,
            ]
        ]

    def to_dict(self):
        """
        The to_dict function takes a Record object and returns a dictionary representation of the record.
        The dictionary has the following keys:
            name: The value of the Name field in this record.
            phone: A list containing all Phone fields in this record, as strings. If there are no Phone fields,
                then an empty list is returned instead (i.e., []). Each string should be formatted like so:
                &quot;type=value&quot; where type is one of &quot;home&quot;, &quot;work&quot;, or &quot;mobile&quot;. For example, if there were two
                phone numbers for a contact with types home and mobile

        :param self: Refer to the instance of the class
        :return: A dictionary of the record's information
        :doc-author: Trelent
        """
        record_dict = {
            "name": self.name.value,
            "phone": [phone.value for phone in self.phone],
            "tag": [tag.value for tag in self.tags],
            "email": self.email.value if self.email else None,
            "birthday": self.birthday.value if self.birthday else None,
            "company": self.company.value if self.company else None,
            "address": self.address.value if self.address else None,
        }
        return record_dict

    def update_field(self, field_name: str, old_value: str, new_value: str) -> None:
        """
        The update_field function takes three arguments:
            1. field_name - the name of the field to be updated
            2. old_value - the value that is currently in that field
            3. new_value - what you want to replace it with

        :param self: Refer to the object itself
        :param field_name: str: Identify the field to be updated
        :param old_value: str: Find the field that needs to be updated
        :param new_value: str: Update the value of a field
        :return: None
        :doc-author: Trelent
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
            raise AttributeError(
                Fore.LIGHTRED_EX + f"Field {field_name} not found in record"
            )
