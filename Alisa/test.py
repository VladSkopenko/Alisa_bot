from Record import Record
from faker import Faker
import json
from tabulate import tabulate
from colorama import Fore
from Record import Phone

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
        birthday=fake.date()
    )
    test_contact.phone.append(Phone("0631934048"))
    test_contact.phone.append(Phone("380961210573"))
    contacts.append(test_contact.to_dict())
with open("Contacts.json", "w", encoding="utf-8") as file:
    json.dump(contacts, file, ensure_ascii=False, indent=5)


headers = ["Name", "Phone", "Tag", "Email", "Birthday", "Company", "Address"]
tab = tabulate([[contact.get(header.lower(), '') for header in headers] for contact in contacts], headers=headers, tablefmt="grid")
print(Fore.LIGHTMAGENTA_EX + tab)
