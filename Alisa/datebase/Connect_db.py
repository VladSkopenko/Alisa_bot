from mongoengine import connect, get_db, disconnect
import configparser


file_config = 'config.ini'
config = configparser.ConfigParser()
config.read(file_config)
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'domain')
disconnect(alias='default')
URI = f"mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net/?retryWrites=true&w=majority"
connect(db="MongoAlise", host=URI)
DB = get_db()




