import os
import pymongo
import datetime
import random
from bson import ObjectId
from GLOBAL import (CLIENT_ENV_KEY, DB_NAME, PROJECT_COLLECTION, SPRINT_COLLECTION, SPRINT_PROJECT_COLLECTION,
                    TEAM_COLLECTION, TICKET_COLLECTION, USER_COLLECTION, USER_TEAM_COLLECTION)
from Helpers.CollectionFunctions import CollectionFunctions
collectionFunctions = CollectionFunctions()


def main():
    mongo_client = pymongo.MongoClient(os.environ[CLIENT_ENV_KEY])
    db = mongo_client[DB_NAME]

    users = db[USER_COLLECTION]
    users.drop()

    teams = db[TEAM_COLLECTION]
    teams.drop()

    user_teams = db[USER_TEAM_COLLECTION]
    user_teams.drop()

    projects = db[PROJECT_COLLECTION]
    projects.drop()

    sprints = db[SPRINT_COLLECTION]
    sprints.drop()

    sprint_projects = db[SPRINT_PROJECT_COLLECTION]
    sprint_projects.drop()

    tickets = db[TICKET_COLLECTION]
    tickets.drop()


if __name__ == '__main__':
    main()
