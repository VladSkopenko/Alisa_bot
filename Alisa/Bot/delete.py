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


if __name__ == "__main__":
    ...
