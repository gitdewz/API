import os
from Helpers.CollectionFunctions import CollectionFunctions
import datetime
import random
from mongoengine import connect
from Models.Project import Project as ProjectModel
from Models.Sprint import Sprint as SprintModel
from Models.SprintProject import SprintProject as SprintProjectModel
from Models.User import User as UserModel
from Models.UserTeam import UserTeam as UserTeamModel
from Models.Team import Team as TeamModel
from Models.Ticket import Ticket as TicketModel
from bson import ObjectId
from hashlib import sha224
from GLOBAL import CLIENT_ENV_KEY, DB_NAME


def main():
    os.environ[CLIENT_ENV_KEY] = "mongodb://localhost:27017/"
    collectionFunctions = CollectionFunctions()
    connect(DB_NAME, host=os.environ[CLIENT_ENV_KEY],
            alias="default")

    admin_id = ObjectId()
    test_user_id = ObjectId()
    user = UserModel(id=admin_id, email="admin@test.com", password=sha224(
        b"admin").hexdigest(), first_name="Admin", last_name="User")
    user.save()
    user = UserModel(id=test_user_id, email="test_user@test.com", password=sha224(
        b"password").hexdigest(), first_name="Test", last_name="User")
    user.save()

    canyon_id = ObjectId()
    ridge_id = ObjectId()
    peak_id = ObjectId()
    team = TeamModel(id=canyon_id, team_name="Canyon",
                     status="Active", date_created=datetime.datetime.now())
    team.save()
    team = TeamModel(id=ridge_id, team_name="Ridge",
                     status="Pending", date_created=datetime.datetime.now())
    team.save()
    team = TeamModel(id=peak_id, team_name="Peak",
                     status="Terminated", date_created=datetime.datetime.now())
    team.save()

    userTeam = UserTeamModel(
        id=ObjectId(), user_id=admin_id, team_id=canyon_id)
    userTeam.save()
    userTeam = UserTeamModel(
        id=ObjectId(), user_id=test_user_id, team_id=canyon_id)
    userTeam.save()

    red_id = ObjectId()
    blue_id = ObjectId()
    gold_id = ObjectId()
    project = ProjectModel(id=red_id, project_name="RED",
                           team_id=canyon_id, description="Red project description.")
    project.save()
    project = ProjectModel(id=blue_id, project_name="BLUE",
                           team_id=ridge_id, description="Blue project description.")
    project.save()
    project = ProjectModel(id=gold_id, project_name="GOLD",
                           team_id=peak_id, description="Gold project description.")
    project.save()

    alpha_id = ObjectId()
    beta_id = ObjectId()
    gamma_id = ObjectId()
    delta_id = ObjectId()
    sprint = SprintModel(id=alpha_id, sprint_name="Alpha", date_start=datetime.datetime.now(
    )+datetime.timedelta(days=-15), date_end=datetime.datetime.now()+datetime.timedelta(days=-1))
    sprint.save()
    sprint = SprintModel(id=beta_id, sprint_name="Beta", date_start=datetime.datetime.now(
    )+datetime.timedelta(days=0), date_end=datetime.datetime.now()+datetime.timedelta(days=14))
    sprint.save()
    sprint = SprintModel(id=gamma_id, sprint_name="Gamma", date_start=datetime.datetime.now(
    )+datetime.timedelta(days=15), date_end=datetime.datetime.now()+datetime.timedelta(days=29))
    sprint.save()
    sprint = SprintModel(id=delta_id, sprint_name="Delta", date_start=datetime.datetime.now(
    )+datetime.timedelta(days=30), date_end=datetime.datetime.now()+datetime.timedelta(days=44))
    sprint.save()

    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=alpha_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=alpha_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=alpha_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=beta_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=beta_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=beta_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=gamma_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=gamma_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=gamma_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=delta_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=delta_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=ObjectId(), sprint_id=delta_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()

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
        "RED", "BLUE", "GOLD"
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
        ticket = TicketModel(id=ObjectId(), ticket_number=ticket_number, project_name=project,
                             sprint_name=sprint_names[random.randint(
                                 0, len(sprint_names)-1)],
                             ticket_type=ticket_types[random.randint(
                                 0, len(ticket_types)-1)],
                             priority=priorities[random.randint(
                                 0, len(priorities)-1)],
                             story_points=story_points[random.randint(
                                 0, len(story_points)-1)],
                             description=description)
        ticket.save()


if __name__ == '__main__':
    main()
