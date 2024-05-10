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
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and it's where you put any code that needs to be run before anything else in your class.

        :param self: Represent the instance of the class
        :return: The object of the class
        :doc-author: Trelent
        """
        super().__init__()
        self.load_records_from_db()

    def load_records_from_db(self):
        """
        The load_records_from_db function is a method of the RecordList class.
        It takes no arguments and returns nothing. It connects to the database,
        retrieves all records from it, and appends them to self (a list of records).


        :param self: Refer to the class instance itself
        :return: A list of recorddocument objects
        :doc-author: Trelent
        """
        connect.connect(db=db, host=URI)
        records_from_db = RecordDocument.objects().all()
        self.extend(records_from_db)

    def to_dict(self):
        """
        The to_dict function returns a list of dictionaries, where each dictionary
        represents the attributes of a single contact. This is useful for converting
        the ContactList object into JSON format.

        :param self: Refer to the current instance of the class
        :return: A list of dictionaries, where each dictionary is a contact
        :doc-author: Trelent
        """
        return [contact.to_dict() for contact in self]

    @staticmethod
    def clear_base():
        """
        The clear_base function clears the database of all collections.


        :return: The list of collections in the database
        :doc-author: Trelent
        """
        collections = DB.list_collection_names()
        for collection in collections:
            DB.drop_collection(collection)

    @table_decorator()
    def __str__(self):
        """
        The __str__ function is used to return a string representation of the object.
        This function is called when you use print(object) or str(object).
        The __str__ method should return a string that can be understood by humans.

        :param self: Represent the instance of the object itself
        :return: A list of dictionaries
        :doc-author: Trelent
        """
        data = []
        for record in self:
            record_dict = record.to_mongo().to_dict()
            if record_dict:
                data.append(record_dict)
        return data
