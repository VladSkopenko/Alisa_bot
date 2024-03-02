import json

from tabulate import tabulate
from colorama import Fore
from faker import Faker

from Record import Record, Phone, DataField

fake = Faker()
contacts = []
for _ in range(5):

    test_contact = Record(
        name=fake.name(),
        phone="0963610573",
        email=fake.email(),
        tag=fake.word(),
        address=fake.address(),
        company=fake.company(),
        birthday=fake.date(),

    )
    test_contact.phone.append(Phone("0631324048"))
    test_contact.phone.append(Phone("380961210573"))
    test_contact.tags.append(DataField("developer"))
    contacts.append(test_contact.to_dict())
with open("Contacts.json", "w", encoding="utf-8") as file:
    json.dump(contacts, file, ensure_ascii=False, indent=2)

table = tabulate(contacts, headers="keys", tablefmt="grid")
print((Fore.LIGHTMAGENTA_EX + table))
