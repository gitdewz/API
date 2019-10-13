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
    users.insert_one({"user_id": ObjectId(), "email": "admin@test.com",
                      "password": "password", "first_name": "Powerful", "last_name": "User"})

    teams = db["Team"]
    canyon_id = ObjectId()
    ridge_id = ObjectId()
    peak_id = ObjectId()
    teams.insert_one({"team_id": canyon_id, "team_name": "Canyon",
                      "status": "Active", "date_created": datetime.datetime.now().isoformat()})
    teams.insert_one({"team_id": ObjectId(), "team_name": "Ridge",
                      "status": "Pending", "date_created": datetime.datetime.now().isoformat()})
    teams.insert_one({"team_id": ObjectId(), "team_name": "Peak",
                      "status": "Terminated", "date_created": datetime.datetime.now().isoformat()})

    projects = db["Project"]
    projects.insert_one({"project_id": ObjectId(), "project_name": "Red",
                         "team_id": canyon_id, "description": "Red project description."})
    projects.insert_one({"project_id": ObjectId(), "project_name": "Blue",
                         "team_id": ridge_id, "description": "Blue project description."})
    projects.insert_one({"project_id": ObjectId(), "project_name": "Gold",
                         "team_id": peak_id, "description": "Gold project description."})

    sprints = db["Sprint"]
    sprints.insert_one({"sprint_id": ObjectId(), "sprint_name": "Alpha", "goal": "Do some work on the project.",
                        "date_start": (datetime.datetime.now()+datetime.timedelta(days=-15)).isoformat(),
                        "date_end": (datetime.datetime.now()+datetime.timedelta(days=-1)).isoformat()})
    sprints.insert_one({"sprint_id": ObjectId(), "sprint_name": "Beta", "goal": "Do MORE work on the project!",
                        "date_start": (datetime.datetime.now()+datetime.timedelta(days=0)).isoformat(),
                        "date_end": (datetime.datetime.now()+datetime.timedelta(days=14)).isoformat()})
    sprints.insert_one({"sprint_id": ObjectId(), "sprint_name": "Gamma", "goal": "Keep doing work on the project.",
                        "date_start": (datetime.datetime.now()+datetime.timedelta(days=15)).isoformat(),
                        "date_end": (datetime.datetime.now()+datetime.timedelta(days=29)).isoformat()})
    sprints.insert_one({"sprint_id": ObjectId(), "sprint_name": "Delta", "goal": "Complete the project.",
                        "date_start": (datetime.datetime.now()+datetime.timedelta(days=30)).isoformat(),
                        "date_end": (datetime.datetime.now()+datetime.timedelta(days=44)).isoformat()})

    tickets = db["Ticket"]
    ticket_descriptions = [
        "Do some work in the app and make things talk to other things.",
        "Research that issue we talked about last week and leave notes on the job.",
        "Find out how to fix that bug and do it.",
        "Write unit tests for every function in the system.",
        "Write integration tests for every module in the system.",
        "Improve CSS throughout the entire react application.",
        "Update HTML to use semantic tags.",
        "Re-model the API structure so it makes sense.",
        "Research the best way to implement something then do it another way for no reason.",
        "Do some things with flask so we can have data and stuff.",
        "Create a component that looks good.",
        "Improve responsiveness of all components.",
        "Connect react routing to all page components.",
        "Create test and production environments.",
        "Setup continuous integration and delivery.",
        "Create global constants for mongoDB databases and collections.",
        "Research the best way to generate UUIDs.",
        "Create a ProjectSprint collection that links projects and sprints together.",
        "Find a secure way to handle CORS with GraphQL requests.",
    ]
    project_names = [
        "Red", "Blue", "Gold"
    ]
    sprint_names = [
        "Alpha", "Beta", "Gamma", "Delta"
    ]
    ticket_types = [
        "Enhancement", "Bug", "Research"
    ]
    priorities = [
        "Blocker", "Standard", "Minor"
    ]
    story_points = [
        1, 2, 3, 5, 8, 13, 21
    ]
    for description in ticket_descriptions:
        project = project_names[random.randint(0, len(project_names)-1)]
        ticket_number = collectionFunctions.findNextId(
            "Ticket", {"project_name": project}, "ticket_number")
        tickets.insert_one({
            "ticket_id": ObjectId(),
            "ticket_number": ticket_number,
            "project_name": project,
            "sprint_name": sprint_names[random.randint(0, len(sprint_names)-1)],
            "ticket_type": ticket_types[random.randint(0, len(ticket_types)-1)],
            "priority": priorities[random.randint(0, len(priorities)-1)],
            "story_points": story_points[random.randint(0, len(story_points)-1)],
            "description": description
        })

    # collection.drop()
    # collection.insert_one({"sessionID": "12345", "userID": "1", "authenticated": True})


if __name__ == '__main__':
    main()
