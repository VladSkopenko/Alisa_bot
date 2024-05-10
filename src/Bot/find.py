from src.Bot.abstract import AbstractBot
from src.models.record import Record


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
                    address=record_doc.address,
                )
                print(record)


AliceFindContact = FindBot()
