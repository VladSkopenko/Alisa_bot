from faker import Faker
from Record import Record
from Connect_db import RecordDocument
from random import choice

fake = Faker('uk_UA')


def generate_fake_phone_number():
    list_phone = ["380961610573", "0961234586", "380631034048"]
    return choice(list_phone)


def fake_seed():
    for _ in range(10):
        valid_contact = Record(
            name=fake.name(),
            phone=generate_fake_phone_number(),
            email=fake.email(),
            tag=fake.word(),
            address=fake.address(),
            company=fake.company(),
            birthday=fake.date(),
        )
        contact_for_db = RecordDocument(
            name=str(valid_contact.name),
            phone=[str(phone) for phone in valid_contact.phone],
            email=str(valid_contact.email),
            tag=[str(tag) for tag in valid_contact.tags],
            address=str(valid_contact.address),
            company=str(valid_contact.company),
            birthday=str(valid_contact.birthday),
        )
        contact_for_db.save()


if __name__ == "__main__":
    for _ in range(3):
        fake_seed()
