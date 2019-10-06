import pymongo


class CollectionFunctions:
    def __init__(self):
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

        # TODO - create global db name const
        self.db = mongo_client["mongoengine"]

    def doesCollectionExist(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.count() > 0

    # TODO
    # 1. Create findMax function that takes in multiple fields
    #    this will allow findMax by project name and ticket number
    def findMax(self, collectionName, field):
        collection = self.db[collectionName]
        return collection.find_one(sort=[(field, -1)])[field]

    def findMongoID(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.find_one({"id": int(item.id), "project": item.project})["_id"]

    def findItem(self, collectionName, entryFilter, attributeFilter):
        collection = self.db[collectionName]
        return collection.find_one(entryFilter, attributeFilter)

    def findUser(self, credentials):
        print(credentials)
        collection = self.db["User"]
        return collection.find_one({"username": credentials["username"], "password": credentials["password"]}, {"_id": False, "password": False})

    def doesItemExist(self, collectionName, key, value):
        return self.db[collectionName].count({key: value}) > 0

    def insert(self, item):
        collection = self.db[item.__class__.__name__]
        print(collection.name)
        print(item.toJson())
        collection.insert(item.toJson())

    def update(self, item):
        collection = self.db[item.__class__.__name__]
        # use this to filter out properties that are set to None,
        # probably don't need to do that though should just load all values on item init
        # data = {k: v for k, v in vars(item) if v is not None}
        collection.find_one_and_update(
            {"_id": self.findMongoID(item)}, {"$set": vars(item)})
