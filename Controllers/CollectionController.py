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

    def findMongoID(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.find_one({"id": int(item.id), "project": item.project})["_id"]

    def findItem(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.find_one({"id": int(item.id), "project": item.project}, {"_id": False})

    def insert(self, item):
        collection = self.db[item.__class__.__name__]
        collection.insert(item.toJson())

    def update(self, item):
        collection = self.db[item.__class__.__name__]
        # use this to filter out properties that are set to None, 
        # probably don't need to do that though should just load all values on item init
        # data = {k: v for k, v in vars(item) if v is not None}
        collection.find_one_and_update({"_id": self.findMongoID(item)}, {"$set": vars(item)})