from src.bot.abstract import AbstractBot
from src.models.record import Record
from src.utils.intro import help_alice


class HelpBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        """
        The handle function is the main function of a handler.
        It takes in a record and returns nothing.


        :param self: Access the attributes and methods of the class
        :param record: Record: Pass the record to the handler
        :return: None
        :doc-author: Trelent
        """
        help_alice()


AliceHelp = HelpBot()
