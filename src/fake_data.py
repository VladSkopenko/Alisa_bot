from random import choice

from faker import Faker

from datebase.connect_db import DB
from models.record_document import RecordDocument
from old_file.Record import Record

fake = Faker()
datebase = DB


def generate_fake_phone_number():
    """
    The generate_fake_phone_number function generates a fake phone number.
        Args:
            None

    :return: A random phone number from the list
    :doc-author: Trelent
    """
    list_phone = ["380961610573", "0961234586", "380631034048"]
    return choice(list_phone)


def seed():
    """
    The seed function will create 10 fake contacts and save them to the database.
        The seed function is called in the main() function, which is called at the bottom of this file.

    :return: A list of recorddocument objects
    :doc-author: Trelent
    """
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
    seed()
