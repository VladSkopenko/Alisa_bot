from src.bot.abstract import AbstractBot
from src.models.record import Record


class FindBot(AbstractBot):

    def handle(self, name: str) -> None:
        """
        The handle function takes a name as an argument and prints the record of that person.


        :param self: Access the class attributes and methods
        :param name: str: Specify the name of the record that we want to print
        :return: The record of the person whose name is passed as an argument
        :doc-author: Trelent
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
                    address=record_doc.address,
                )
                print(record)


AliceFindContact = FindBot()
