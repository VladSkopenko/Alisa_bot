from mongoengine import connect
from mongoengine import disconnect
from mongoengine import get_db

from Alisa.datebase.config import settings

disconnect(alias='default')

URI = settings.MONGO_URL
db = settings.MONGO_INITDB_DATABASE

connect(db=db, host=URI)
DB = get_db()
