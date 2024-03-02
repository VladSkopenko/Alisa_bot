from collections import UserList
import json
from Record import Record
from Decorators.Table_decorator import table_decorator


class AddressBook(UserList):
    def __init__(self, file_name):
        super().__init__()
        self.load_from_json(file_name)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            for contact_data in data:
                contact = Record(**contact_data)
                self.append(contact)

    def save_to_json(self, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    def to_dict(self):
        return [contact.to_dict() for contact in self]

    @table_decorator
    def __str__(self):
        return self

if __name__ == "__main__":
    ad = AddressBook("Contacts.json")
    ad.save_to_json("test_save.json")
    print(ad)
