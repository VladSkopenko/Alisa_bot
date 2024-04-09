from colorama import Fore

from abstract import AbstractBot
from Alisa.models.RecordDocument import RecordDocument


class RemoveBot(AbstractBot):

    def handle(self, record_id) -> None:
        """
        Delete a record from the database based on its ID.
        """
        record = RecordDocument.objects(id=record_id).first()
        if record:
            record.delete()
            return print(Fore.LIGHTCYAN_EX + "Successfully deleted")


if __name__ == "__main__":
    deli = RemoveBot()
    deli.handle("66147ce5bc4d3616c757fc44")
