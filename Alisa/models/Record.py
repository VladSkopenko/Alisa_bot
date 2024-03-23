from DataField import DataField
from Birthday import Birthday
from Email import Email
from Phone import Phone
from Alisa.Decorators.Table_decorator import table_decorator



class Record:
    """
    The Record class represents a contact entry with information about a person, including their name, contact details
    """
    __headers = ["Name", "Company", "Email", "Birthday", "Phone", "Tags", "Address"]

    def __init__(self, name: str,
                 phone: str,
                 tag: str = "",
                 email: str = "",
                 birthday: str = "",
                 company: str = "",
                 address: str = "",
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

    @table_decorator(__headers)
    def __str__(self):
        return [
            [self.name,
             self.company,
             self.email,
             self.birthday,
             [phone.value for phone in self.phone],
             [tag.value for tag in self.tags],
             self.address]
        ]

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
