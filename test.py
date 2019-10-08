import pymongo

def main():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo_client["mongoengine"]
    db.coll
    collection = db["session"]
    collection.drop()
    collection.insert_one({"sessionID": "12345", "userID": "1", "authenticated": True})

if __name__ == '__main__':
    main()
