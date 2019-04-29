import pymongo

class CollectionController:
    def __init__(self):
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = mongo_client["test"]

    def doesCollectionExist(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.count() > 0

    def findMax(self, item, field):
        collection = self.db[item.__class__.__name__]
        return collection.find_one(sort=[(field,-1)])[field]

    def insert(self, item):
        collection = self.db[item.__class__.__name__]
        collection.insert(item.toJson())