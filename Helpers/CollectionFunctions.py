import pymongo
from GLOBAL import DB_NAME

# TODO
# 1. Create constants for db / collections


class CollectionFunctions:
    def __init__(self):
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

        # TODO - create global db name const
        self.db = mongo_client[DB_NAME]

    def doesCollectionExist(self, collectionName, whereClause):
        collection = self.db[collectionName]
        return collection.find(whereClause).count() > 0

    # TODO
    # 1. Create findMax function that takes in multiple fields
    #    this will allow findMax by project name and ticket number
    def findMax(self, collectionName, whereClause, field):
        collection = self.db[collectionName]
        return collection.find_one(whereClause, sort=[(field, -1)])[field]

    def findNextId(self, collectionName, whereClause, field):
        nextId = 1
        if self.doesCollectionExist(collectionName, whereClause):
            nextId = self.findMax(collectionName, whereClause, field) + 1
        return nextId

    def findMongoID(self, item):
        collection = self.db[item.__class__.__name__]
        return collection.find_one({"id": int(item.id), "project": item.project})["_id"]

    def findItem(self, collectionName, entryFilter, attributeFilter):
        collection = self.db[collectionName]
        return collection.find_one(entryFilter, attributeFilter)

    def findUser(self, email, password):
        collection = self.db["User"]
        return collection.find_one({"email": email, "password": password})

    def validateLogin(self, email, password):
        collection = self.db["User"]
        return collection.find({"email": email, "password": password}).count() == 1

    def doesItemExist(self, collectionName, key, value):
        return self.db[collectionName].count({key: value}) > 0

    def insert(self, collectionName, item):
        collection = self.db[collectionName]
        collection.insert(item)

    def update(self, item):
        collection = self.db[item.__class__.__name__]
        # use this to filter out properties that are set to None,
        # probably don't need to do that though should just load all values on item init
        # data = {k: v for k, v in vars(item) if v is not None}
        collection.find_one_and_update(
            {"_id": self.findMongoID(item)}, {"$set": vars(item)})

    def authenticate(self, token):
        print(token)
        session = self.findItem(
            "session", {"sessionID": token.replace("-", "")}, None)
        print(session)
        return session and session["authenticated"]
