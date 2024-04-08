from mongoengine import Document
from mongoengine import ListField
from mongoengine import StringField


class RecordDocument(Document):
    name = StringField()
    phone = ListField(StringField(), auto_creation=True)
    tag = ListField(StringField(), auto_creation=True)
    email = StringField()
    birthday = StringField()
    company = StringField()
    address = StringField()
