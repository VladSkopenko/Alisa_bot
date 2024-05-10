from colorama import Fore

from src.bot.abstract import AbstractBot
from src.models.record_document import RecordDocument


class RemoveBot(AbstractBot):

    def handle(self, record_id) -> None:
        """
        The handle function is the entry point for this command.
        It will be called by the CLI with a record_id argument, which it then uses to delete a record from the database.


        :param self: Represent the instance of the class
        :param record_id: Identify the record that is to be deleted
        :return: None
        :doc-author: Trelent
        """
        record = RecordDocument.objects(id=record_id).first()
        if record:
            record.delete()
            return print(Fore.LIGHTCYAN_EX + "Successfully deleted")


AliceRemoveBot = RemoveBot()
