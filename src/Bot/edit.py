from abstract import AbstractBot
from src.models.record import Record
from src.models.RecordDocument import RecordDocument
from colorama import Fore


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
            return Fore.LIGHTBLUE_EX + "Record updated successfully"
        else:
            return Fore.LIGHTRED_EX + "Record not found"


AliceEditContact = EditBot()
