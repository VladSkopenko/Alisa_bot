from collections import UserList

from Decorators.Table_decorator import table_decorator
from Connect_db import RecordDocument, connect, URI


class AddressBook(UserList):
    __headers = ["id", "name", "phone", "tags", "email", "birthday", "company", "address"]

    def __init__(self):
        super().__init__()
        self.load_records_from_db()

    def load_records_from_db(self):
        connect(db="MongoAlise", host=URI)

        records_from_db = RecordDocument.objects().all()
        self.extend(records_from_db)

    def to_dict(self):
        return [contact.to_dict() for contact in self]

    @table_decorator()
    def __str__(self):
        data = []
        for record in self:
            record_dict = record.to_mongo().to_dict()
            if record_dict:
                data.append(record_dict)
        return data


if __name__ == "__main__":
    ad = AddressBook()
    print(ad)
