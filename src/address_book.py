from collections import UserList

from src.datebase.connect_db import connect
from src.datebase.connect_db import DB
from src.datebase.connect_db import db
from src.datebase.connect_db import URI
from src.decorators.table_decorator import table_decorator
from src.models.record_document import RecordDocument


class AddressBook(UserList):
    __headers = [
        "id",
        "name",
        "phone",
        "tags",
        "email",
        "birthday",
        "company",
        "address",
    ]

    def __init__(self):
        super().__init__()
        self.load_records_from_db()

    def load_records_from_db(self):
        connect(db=db, host=URI)
        records_from_db = RecordDocument.objects().all()
        self.extend(records_from_db)

    def to_dict(self):
        return [contact.to_dict() for contact in self]

    @staticmethod
    def clear_base():
        collections = DB.list_collection_names()
        for collection in collections:
            DB.drop_collection(collection)

    @table_decorator()
    def __str__(self):
        data = []
        for record in self:
            record_dict = record.to_mongo().to_dict()
            if record_dict:
                data.append(record_dict)
        return data