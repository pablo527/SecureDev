import pymongo
import os

class MongoDB:
    USER_DB = os.environ['USER_DB']
    PASSWORD_DB = os.environ['PASSWORD_DB']
    MONGO_URI = 'mongodb://{user}:{password}@192.168.10.10:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=my_db&appName=mongosh+1.6.0'.format(
        user=USER_DB, password=PASSWORD_DB)

    def __init__(self):
        try:
            self.client = pymongo.MongoClient(self.MONGO_URI)
            self.client.server_info()
        except pymongo.errors as err:
            print('Ocurrio un error: ', err)

    def connetTo(self, dbName, collection):
        try:
            self.db = self.client.get_database(dbName)
            self.collection = self.db.get_collection(collection)
        except pymongo.errors as err:
            print('Ocurrio un error: ', err)

    def insertOneData(self, data):
        try:
            self.collection.insert_one(data)
        except pymongo.errors as err:
            print('Ocurrio un error: ', err)            

    def closeConnection(self):
        self.client.close()
