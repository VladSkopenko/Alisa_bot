from src.bot.abstract import AbstractBot
from src.models.record import Record
from src.utils.intro import exit_alice


class ExitBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        """
        The handle function is the main function of a skill.
        It takes in an optional record object, which contains information about the user's request.
        The handle function should return None if it was successful or raise an exception otherwise.

        :param self: Represent the instance of the class
        :param record: Record: Pass in the record that is being processed
        :return: None
        :doc-author: Trelent
        """
        exit_alice()


AliceExit = ExitBot()
