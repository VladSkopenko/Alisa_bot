from src.bot.abstract import AbstractBot
from src.models.record import Record
from src.models.record_document import RecordDocument


class AddBot(AbstractBot):

    def handle(self, record: Record) -> None:
        """
        The handle function is the main function of this class. It takes a Record object as an argument and saves it to the database.

        :param self: Represent the instance of the class
        :param record: Record: Pass the record object to the handle function
        :return: None
        :doc-author: Trelent
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
