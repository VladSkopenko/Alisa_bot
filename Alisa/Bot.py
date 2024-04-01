from abc import ABC, abstractmethod
from models.record import Record
from Address_book import AddressBook
from models.RecordDocument import RecordDocument


class AbstractBot(ABC):
    def __init__(self):
        self.address_book = AddressBook()

    @abstractmethod
    def handle(self, *args):
        pass

    @staticmethod
    def get_user_input_for_record_creation() -> Record:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        tag = input("Enter tag: ")
        email = input("Enter email: ")
        birthday = input("Enter birthday (YYYY-MM-DD): ")
        company = input("Enter company: ")
        address = input("Enter address: ")

        record = Record(
            name=name,
            phone=phone,
            tag=tag,
            email=email,
            birthday=birthday,
            company=company,
            address=address
        )
        return record

    def help(self):
        ...


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

    def handle(self, name: str, record: Record) -> None | str:
        """
        Edit a record in the database based on its ID.
        """
        record_from_db = RecordDocument.objects(name=name).first()
        if record_from_db:
            record_from_db.name = str(record.name)
            record_from_db.phone = [str(phone) for phone in record.phone]
            record_from_db.email = str(record.email)
            record_from_db.tag = [str(tag) for tag in record.tags]
            record_from_db.address = str(record.address)
            record_from_db.company = str(record.company)
            record_from_db.birthday = str(record.birthday)
            record_from_db.save()
            return "Record updated successfully"  # Залогіровать
        else:
            return "Record not found"  # Залогіровать


class FindBot(AbstractBot):

    def handle(self, name: str) -> None:
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
    ed = EditBot()
    p = Record(name="vlad",
               phone="380961630573",
               tag="student",
               email="exsam@fa.com",
               birthday="2000-01-28",
               company="go it",
               address="address231213"
               )
    ed.handle('Oleg', p)
