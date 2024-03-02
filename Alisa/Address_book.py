from collections import UserList
import json
from Record import Record, DataField
from Decorators.Table_decorator import table_decorator


class AddressBook(UserList):
    def __init__(self, file_name):
        super().__init__()
        self.load_from_json(file_name)

    def load_from_json(self, file_name):
        with open(f'{file_name}.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            for contact_data in data:
                contact = Record(**contact_data)
                self.append(contact)

    def save(self, file_name):
        with open(f'{file_name}.json', "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    def save_to_json_with_tag(self, file_name, tag=None):
        filtered_contacts = self if tag is None else [contact for contact in self if tag in contact.tags]
        with open(f"{file_name}.json", "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in filtered_contacts], file, ensure_ascii=False, indent=4)

    def to_dict(self):
        return [contact.to_dict() for contact in self]

    @table_decorator
    def __str__(self):
        return self

    def append(self, record):
        record.assign_id(len(self) + 1)
        super().append(record)


if __name__ == "__main__":
    ad = AddressBook("Contacts")
    ad.save_to_json_with_tag('contacts_developer', tag=DataField('after'))
    ad.load_from_json('contacts_developer')
    ad.save("all_file")
    print(ad)
