from abstract import AbstractBot
from src.models.record import Record


class ShowAllBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        """
        Show all records in the database
        """
        print(self.address_book)


AliceShowAll = ShowAllBot()
