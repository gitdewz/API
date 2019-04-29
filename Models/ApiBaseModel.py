import pymongo
from Controllers.CollectionController import CollectionController

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["test"]

class ApiBaseModel:
    def __init__(self):
        collection = db[self.__class__.__name__]
        if collection.count() == 0:
            self.id = 1
        else:
            self.id = collection.find_one(sort=[("id",-1)])["id"] + 1

    def toJson(self):
        return vars(self)

    def insert(self):
        collectionController = CollectionController()
        collectionController.insert(self)
