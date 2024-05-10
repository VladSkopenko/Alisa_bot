from colorama import Fore

from src.bot.abstract import AbstractBot
from src.models.record import Record
from src.models.record_document import RecordDocument


class EditBot(AbstractBot):

    def handle(self, name: str, record: Record = None) -> None | str:
        """
        The handle function is responsible for updating a record in the database.
            It takes two arguments:
                name (str): The name of the record to be updated.
                record (Record): A Record object containing all information about the new version of this contact.

        :param self: Represent the instance of the class
        :param name: str: Pass the name of the record to be updated
        :param record: Record: Pass the record object to the function
        :return: None | str
        :doc-author: Trelent
        """
        if not record:
            record = self.get_user_input_for_record_creation()
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
