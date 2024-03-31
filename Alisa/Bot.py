from abc import ABC, abstractmethod
from models.record import Record
from Address_book import AddressBook
from models.RecordDocument import RecordDocument
from Decorators.Table_decorator import table_decorator


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

    def handle(self, name: str) -> list[Record]:
        """
        Find records in the database by name.
        """
        for record_doc in self.address_book:
            if record_doc.name.lower() == name.lower():
                record = Record(
                    name=record_doc.name,
                    phone=record_doc.phone,
                    tag=record_doc.tag,
                    email=record_doc.email,
                    birthday=record_doc.birthday,
                    company=record_doc.company,
                    address=record_doc.address
                )
                print(record)


if __name__ == "__main__":
    ...

