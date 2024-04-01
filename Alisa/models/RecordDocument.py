from mongoengine import Document, StringField, ListField


class RecordDocument(Document):
    name = StringField()
    phone = ListField(StringField(), auto_creation=True)
    tag = ListField(StringField(), auto_creation=True)
    email = StringField()
    birthday = StringField()
    company = StringField()
    address = StringField()
