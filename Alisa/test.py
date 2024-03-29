from faker import Faker
from Connect_db import update_db, connect
from Record import Record
from Connect_db import RecordDocument

fake = Faker()


def generate_fake_phone_number():
    return '0' + str(fake.random_number(digits=9))

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
