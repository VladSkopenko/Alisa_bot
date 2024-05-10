from colorama import Fore

from abstract import AbstractBot
from src.models.RecordDocument import RecordDocument


class RemoveBot(AbstractBot):

    def handle(self, record_id) -> None:
        """
        Delete a record from the database based on its ID.
        """
        record = RecordDocument.objects(id=record_id).first()
        if record:
            record.delete()
            return print(Fore.LIGHTCYAN_EX + "Successfully deleted")


AliceRemoveBot = RemoveBot()
