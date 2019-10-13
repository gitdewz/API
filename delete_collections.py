import pymongo
import datetime
import random
from bson import ObjectId
from GLOBAL import DB_NAME
from Helpers.CollectionFunctions import CollectionFunctions
collectionFunctions = CollectionFunctions()


def main():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo_client[DB_NAME]

    users = db["User"]
    users.drop()

    teams = db["Team"]
    teams.drop()

    projects = db["Project"]
    projects.drop()

    sprints = db["Sprint"]
    sprints.drop()

    tickets = db["Ticket"]
    tickets.drop()


if __name__ == '__main__':
    main()
