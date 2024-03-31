from mongoengine import connect, get_db
import configparser
from Alisa.models.record import Record
from models.RecordDocument import RecordDocument


file_config = 'config.ini'
config = configparser.ConfigParser()
config.read(file_config)
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'domain')

URI = f"mongodb+srv://{user}:{password}@{domain}.x6ks5fo.mongodb.net/?retryWrites=true&w=majority"
connect(db="MongoAlise", host=URI)
DB = get_db()


def update_db(record: Record):
    contact_for_db = RecordDocument(
        name=str(record.name),
        phone=[str(phone) for phone in record.phone],
        email=str(record.email),
        tag=[str(tag) for tag in record.tags],
        address=str(record.address),
        company=str(record.company),
        birthday=str(record.birthday),
    )
    contact_for_db.save()

