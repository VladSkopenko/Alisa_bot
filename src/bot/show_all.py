from src.bot.abstract import AbstractBot
from src.models.record import Record


class ShowAllBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        """
        The handle function is the main function of this class. It loads all records from the database and prints them to stdout.

        :param self: Reference the object that is calling the method
        :param record: Record: Pass in a record to the handle function
        :return: Nothing
        :doc-author: Trelent
        """
        self.address_book.load_records_from_db()
        print(self.address_book)


AliceShowAll = ShowAllBot()
