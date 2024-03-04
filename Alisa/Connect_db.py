from mongoengine import Document, connect, StringField, ListField
import configparser
from Record import Record

file_config = 'config.ini'
config = configparser.ConfigParser()
config.read(file_config)
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'domain')

URI = f"mongodb+srv://{user}:{password}@{domain}.x6ks5fo.mongodb.net/?retryWrites=true&w=majority"
connect(db="MongoAlise", host=URI)


def update_db():
    valid_contact = Record(
        name="Vlad",
        phone="+380961610573",
        email="skopirka2k17@mail.com",
        tag="student",
        address="Filatova 345",
        company="go it",
        birthday="2000-01-28",
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


class RecordDocument(Document):
    name = StringField()
    phone = ListField(StringField(), auto_creation=True)
    tag = ListField(StringField(), auto_creation=True)
    email = StringField()
    birthday = StringField()
    company = StringField()
    address = StringField()



