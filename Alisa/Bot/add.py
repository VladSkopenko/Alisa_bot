import sys
import os

from Alisa.Bot import abstract
from Alisa.models.record import Record
from Alisa.models.RecordDocument import RecordDocument

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(module_path)


class AddBot(abstract.AbstractBot):

    def handle(self, record: Record) -> None:
        """
        Add a contact to the database
        """
        contact_for_db = RecordDocument(
            name=str(record.name),
            phone=[str(phone) for phone in record.phone],
            email=str(record.email),
            tag=[str(tag) for tag in record.tags],
            address=str(record.address),
            company=str(record.company),
            birthday=str(record.birthday),
        )
        contact_for_db.save()


if __name__ == "__main__":
    add = AddBot()
    add.get_user_input_for_record_creation()

