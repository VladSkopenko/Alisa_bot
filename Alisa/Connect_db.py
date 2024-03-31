from mongoengine import connect, get_db
import configparser


file_config = 'config.ini'
config = configparser.ConfigParser()
config.read(file_config)
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'domain')

URI = f"mongodb+srv://{user}:{password}@{domain}.x6ks5fo.mongodb.net/?retryWrites=true&w=majority"
connect(db="MongoAlise", host=URI)
DB = get_db()




