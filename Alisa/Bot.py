from abc import ABC, abstractmethod
from models.record import Record
from Address_book import AddressBook
from models.RecordDocument import RecordDocument


class AbstractBot(ABC):
    def __init__(self):
        self.address_book = AddressBook()

    @abstractmethod
    def handle(self):
        pass


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
        contact_for_db.save()


class RemoveBot(AbstractBot):

    def handle(self, record_id) -> None:
        """
        Delete a record from the database based on its ID.
        """
        record = RecordDocument.objects(id=record_id).first()
        if record:
            record.delete()


class EditBot(AbstractBot):
    ...


class FindBot(AbstractBot):
    ...


if __name__ == "__main__":
    ad = AddBot()
    per = Record(name="Liuda",
                 phone="380961630573",
                 tag="mentor",
                 email="exsam@fa.com",
                 birthday="1990-12-18",
                 company="soft",
                 address="address231213"
                 )
    rm = RemoveBot()
    rm.handle("6609ecc0db3f7ece52a472ca")
