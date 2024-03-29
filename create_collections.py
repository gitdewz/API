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
from Models.TicketStatus import TicketStatus as TicketStatusModel
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

    alpha_red_id = ObjectId()
    alpha_blue_id = ObjectId()
    alpha_gold_id = ObjectId()
    beta_red_id = ObjectId()
    beta_blue_id = ObjectId()
    beta_gold_id = ObjectId()
    gamma_red_id = ObjectId()
    gamma_blue_id = ObjectId()
    gamma_gold_id = ObjectId()
    delta_red_id = ObjectId()
    delta_blue_id = ObjectId()
    delta_gold_id = ObjectId()
    sprintProject = SprintProjectModel(
        id=alpha_red_id, sprint_id=alpha_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=alpha_blue_id, sprint_id=alpha_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=alpha_gold_id, sprint_id=alpha_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=beta_red_id, sprint_id=beta_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=beta_blue_id, sprint_id=beta_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=beta_gold_id, sprint_id=beta_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=gamma_red_id, sprint_id=gamma_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=gamma_blue_id, sprint_id=gamma_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=gamma_gold_id, sprint_id=gamma_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=delta_red_id, sprint_id=delta_id, project_id=red_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=delta_blue_id, sprint_id=delta_id, project_id=blue_id, goal="Do some work on the project.")
    sprintProject.save()
    sprintProject = SprintProjectModel(
        id=delta_gold_id, sprint_id=delta_id, project_id=gold_id, goal="Do some work on the project.")
    sprintProject.save()

    status_one_id = ObjectId()
    status_two_id = ObjectId()
    status_three_id = ObjectId()
    status_four_id = ObjectId()
    status_five_id = ObjectId()
    status_six_id = ObjectId()
    status_seven_id = ObjectId()
    status_eight_id = ObjectId()
    status_nine_id = ObjectId()
    status_ten_id = ObjectId()
    status_eleven_id = ObjectId()
    status_twelve_id = ObjectId()
    ticketStatus = TicketStatusModel(
        status_id=status_one_id, status_order=1, status_label="To Do", project_id=red_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_two_id, status_order=2, status_label="In Progress", project_id=red_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_three_id, status_order=3, status_label="Review", project_id=red_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_four_id, status_order=4, status_label="Done", project_id=red_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_five_id, status_order=1, status_label="To Do", project_id=blue_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_six_id, status_order=2, status_label="In Progress", project_id=blue_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_seven_id, status_order=3, status_label="Review", project_id=blue_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_eight_id, status_order=4, status_label="Done", project_id=blue_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_nine_id, status_order=1, status_label="To Do", project_id=gold_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_ten_id, status_order=2, status_label="In Progress", project_id=gold_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_eleven_id, status_order=3, status_label="Review", project_id=gold_id)
    ticketStatus.save()
    ticketStatus = TicketStatusModel(
        status_id=status_twelve_id, status_order=4, status_label="Done", project_id=gold_id)
    ticketStatus.save()

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
        "Make everything more responsive!"
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
    status_ids = [
        status_one_id, status_two_id, status_three_id, status_four_id,
        status_five_id, status_six_id, status_seven_id, status_eight_id,
        status_nine_id, status_ten_id, status_eleven_id, status_twelve_id
    ]
    sprint_project_ids = {
        "AlphaRED": alpha_red_id,
        "AlphaBLUE": alpha_blue_id,
        "AlphaGOLD": alpha_gold_id,
        "BetaRED": beta_red_id,
        "BetaBLUE": beta_blue_id,
        "BetaGOLD": beta_gold_id,
        "GammaRED": gamma_red_id,
        "GammaBLUE": gamma_blue_id,
        "GammaGOLD": gamma_gold_id,
        "DeltaRED": delta_red_id,
        "DeltaBLUE": delta_blue_id,
        "DeltaGOLD": delta_gold_id,
        "Backlog": None,
    }
    i = 0
    count = 1
    while i < 15:
        for description in ticket_descriptions:
            project_index = random.randint(0, len(project_names)-1)
            project = project_names[project_index]
            ticket_number = collectionFunctions.findNextId(
                "Ticket", {"project_name": project}, "ticket_number")
            sprint = sprint_names[random.randint(
                0, len(sprint_names)-1)]
            status_index = (project_index * int(len(status_ids) / len(project_names))) + \
                random.randint(0, len(project_names))
            sprint_project_id = sprint_project_ids[sprint+project]
            ticket = TicketModel(id=ObjectId(), ticket_number=ticket_number, project_name=project,
                                 sprint_name=sprint,
                                 ticket_type=ticket_types[random.randint(
                                     0, len(ticket_types)-1)],
                                 priority=priorities[random.randint(
                                     0, len(priorities)-1)],
                                 story_points=story_points[random.randint(
                                     0, len(story_points)-1)],
                                 description=description,
                                 title="Ticket " + str(count),
                                 status_id=status_ids[status_index],
                                 )
            if random.randint(1, 8) != 4:
                ticket.sprint_project_id = sprint_project_id
            ticket.save()
            count += 1
        i += 1


if __name__ == '__main__':
    main()
