import pymongo

class CollectionController:
    def __init__(self):
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = mongo_client["test"]

    def insert(self, item):
        collection = self.db[item.__class__.__name__]
        collection.insert(item.toJson())