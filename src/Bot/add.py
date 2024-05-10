from abstract import AbstractBot
from src.models.record import Record
from src.models.RecordDocument import RecordDocument


class AddBot(AbstractBot):

    def handle(self, record: Record) -> None:
        """
        Add a contact to the database
        """
        contact_for_db = RecordDocument(
            name=str(record.name),
            phone=[str(phone) for phone in record.phone],
            email=str(record.email),
            tag=[str(tag) for tag in record.tags],
            address=str(record.address),
            company=str(record.company),
            birthday=str(record.birthday),
        )
        task = contact_for_db.save()
        if task:
            print("Contact added successfully")


AliceAddContact = AddBot()
