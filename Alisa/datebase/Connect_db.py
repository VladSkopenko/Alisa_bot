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
domain = config.get('DEV_DB', 'domain')
disconnect(alias='default')
URI = f"mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net/?retryWrites=true&w=majority"
connect(db="MongoAlise", host=URI)
DB = get_db()




