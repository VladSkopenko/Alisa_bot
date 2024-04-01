from mongoengine import connect, get_db, disconnect
import configparser
from pathlib import Path
import os

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")
config = configparser.ConfigParser()
config.read(config_path)
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
secret = config.get('DEV_DB', 'SECRET')
disconnect(alias='default')
URI = f"mongodb+srv://{user}:{password}@{domain}.{secret}"
connect(db="MongoAlise", host=URI)
DB = get_db()




