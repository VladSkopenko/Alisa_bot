from abstract import AbstractBot
from Alisa.models.record import Record
from Alisa.models.RecordDocument import RecordDocument


class EditBot(AbstractBot):

    def handle(self, name: str, record: Record) -> None | str:
        """
        Edit a record in the database based on its ID.
        """
        record_from_db = RecordDocument.objects(name=name).first()
        if record_from_db:
            record_from_db.name = str(record.name)
            record_from_db.phone = [str(phone) for phone in record.phone]
            record_from_db.email = str(record.email)
            record_from_db.tag = [str(tag) for tag in record.tags]
            record_from_db.address = str(record.address)
            record_from_db.company = str(record.company)
            record_from_db.birthday = str(record.birthday)
            record_from_db.save()
            return "Record updated successfully"  # TODO додати кольор
        else:
            return "Record not found"  # Todo you need to add the color


if __name__ == "__main__":
    ...
