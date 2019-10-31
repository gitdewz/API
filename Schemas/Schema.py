import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Project import Project as ProjectModel
from Models.Sprint import Sprint as SprintModel
from Models.SprintProject import SprintProject as SprintProjectModel
from Models.Team import Team as TeamModel
from Models.Ticket import Ticket as TicketModel
from Models.TicketStatus import TicketStatus as TicketStatusModel
from Models.User import User as UserModel
from Models.UserTeam import UserTeam as UserTeamModel
from Schemas.ProjectSchema import CreateProject, DeleteProject, UpdateProject, ProjectSchema
from Schemas.SprintSchema import CreateSprint, DeleteSprint, UpdateSprint, SprintSchema
from Schemas.SprintProjectSchema import CreateSprintProject, DeleteSprintProject, UpdateSprintProject, SprintProjectSchema
from Schemas.TeamSchema import CreateTeam, DeleteTeam, UpdateTeam, TeamSchema
from Schemas.TicketSchema import CreateTicket, DeleteTicket, UpdateTicket, TicketSchema
from Schemas.TicketStatusSchema import CreateTicketStatus, DeleteTicketStatus, UpdateTicketStatus, TicketStatusSchema
from Schemas.UserSchema import CreateUser, DeleteUser, LoginUser, UpdateUser, UserSchema
from Schemas.UserTeamSchema import CreateUserTeam, DeleteUserTeam, UpdateUserTeam, UserTeamSchema
from bson import ObjectId
from GLOBAL import SPRINT_COLLECTION, PROJECT_COLLECTION, TICKET_COLLECTION, USER_COLLECTION, USER_TEAM_COLLECTION


class TicketObject(graphene.ObjectType):
    ticket_id = graphene.ID()
    ticket_number = graphene.Int()
    project_name = graphene.String()
    sprint_name = graphene.String()
    ticket_type = graphene.String()
    priority = graphene.String()
    story_points = graphene.Int()
    description = graphene.String()
    active_user_id = graphene.ID()
    status_id = graphene.ID()
    sprint_project_id = graphene.ID()


class SprintProjectJoin(graphene.ObjectType):
    sprint_project_id = graphene.ID()
    sprint_name = graphene.String()
    project_name = graphene.String()
    goal = graphene.String()
    tickets = graphene.List(TicketObject)


class TeamMember(graphene.ObjectType):
    user_id = graphene.ID()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()


class UserTeamJoin(graphene.ObjectType):
    team_id = graphene.ID()
    team_name = graphene.String()
    status = graphene.String()
    team_members = graphene.List(TeamMember)
    date_created = graphene.DateTime()


class Query(graphene.ObjectType):
    # Project Queries
    projects = MongoengineConnectionField(ProjectSchema)

    all_projects = graphene.List(ProjectSchema)

    def resolve_all_projects(self, info):
        return list(ProjectModel.objects().all())

    project = graphene.Field(
        ProjectSchema, project_name=graphene.String())

    def resolve_project(self, info, project_name):
        return ProjectModel.objects.get(project_name__iexact=project_name)

    # Sprint Queries
    sprints = MongoengineConnectionField(SprintSchema)

    all_sprints = graphene.List(SprintSchema)

    def resolve_all_sprints(self, info):
        return list(SprintModel.objects().all())

    sprint = graphene.Field(
        SprintSchema, sprint_name=graphene.String())

    def resolve_sprint(self, info, sprint_name):
        return SprintModel.objects.get(sprint_name__iexact=sprint_name)

    # SprintProject Queries
    sprint_projects = MongoengineConnectionField(SprintProjectSchema)

    all_sprint_projects = graphene.List(SprintProjectJoin)

    def resolve_all_sprint_projects(self, info):
        cursor = SprintProjectModel.objects.aggregate(*[
            {
                "$lookup": {
                    "from": SPRINT_COLLECTION,
                    "localField": "sprint_id",
                    "foreignField": "_id",
                    "as": "sprint_data"
                }
            },
            {"$unwind": "$sprint_data"},
            {
                "$lookup": {
                    "from": PROJECT_COLLECTION,
                    "localField": "project_id",
                    "foreignField": "_id",
                    "as": "project_data"
                }
            },
            {"$unwind": "$project_data"},
            {
                "$project": {
                    "_id": 0,
                    "sprint_project_id": "$_id",
                    "sprint_name": "$sprint_data.sprint_name",
                    "project_name": "$project_data.project_name",
                    "goal": 1,
                }
            },
        ])
        sprint_projects = []
        for item in list(cursor):
            sprint_projects.append(SprintProjectJoin(**item))
        return list(sprint_projects)

    sprint_project = graphene.Field(
        SprintProjectJoin, sprint_project_id=graphene.ID())

    def resolve_sprint_project(self, info, sprint_project_id):
        cursor = SprintProjectModel.objects.aggregate(*[
            {
                "$match": {"_id": ObjectId(sprint_project_id)}
            },
            {
                "$lookup": {
                    "from": SPRINT_COLLECTION,
                    "localField": "sprint_id",
                    "foreignField": "_id",
                    "as": "sprint_data"
                }
            },
            {"$unwind": "$sprint_data"},
            {
                "$lookup": {
                    "from": PROJECT_COLLECTION,
                    "localField": "project_id",
                    "foreignField": "_id",
                    "as": "project_data"
                }
            },
            {"$unwind": "$project_data"},
            {
                "$lookup": {
                    "from": TICKET_COLLECTION,
                    "localField": "_id",
                    "foreignField": "sprint_project_id",
                    "as": "tickets"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "sprint_name": "$sprint_data.sprint_name",
                    "project_name": "$project_data.project_name",
                    "goal": 1,
                    "tickets": {
                        "$map": {
                            "input": "$tickets",
                            "as": "tickets",
                            "in": {
                                "ticket_id": "$$tickets._id",
                                "ticket_number": "$$tickets.ticket_number",
                                "project_name": "$$tickets.project_name",
                                "sprint_name": "$$tickets.sprint_name",
                                "ticket_type": "$$tickets.ticket_type",
                                "priority": "$$tickets.priority",
                                "story_points": "$$tickets.story_points",
                                "description": "$$tickets.description",
                                "active_user_id": "$$tickets.active_user_id",
                                "status_id": "$$tickets.status_id",
                                "sprint_project_id": "$$tickets.sprint_project_id",
                            }
                        }
                    }
                }
            },
        ])
        return SprintProjectJoin(**list(cursor)[0])

    # Team Queries
    teams = MongoengineConnectionField(TeamSchema)

    all_teams = graphene.List(UserTeamJoin)

    def resolve_all_teams(self, info):
        cursor = TeamModel.objects.aggregate(*[
            {
                "$lookup": {
                    "from": USER_TEAM_COLLECTION,
                    "localField": "_id",
                    "foreignField": "team_id",
                    "as": "user_team_data"
                }
            },
            {
                "$lookup": {
                    "from": USER_COLLECTION,
                    "localField": "user_team_data.user_id",
                    "foreignField": "_id",
                    "as": "team_members"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "team_id": "$_id",
                    "team_name": 1,
                    "status": 1,
                    "data_created": 1,
                    "team_members": {
                        "$map": {
                            "input": "$team_members",
                            "as": "team_members",
                            "in": {
                                "user_id": "$$team_members._id",
                                "email": "$$team_members.email",
                                "first_name": "$$team_members.first_name",
                                "last_name": "$$team_members.last_name",
                            }
                        }
                    }
                }
            },
        ])
        teams = []
        for item in list(cursor):
            teams.append(UserTeamJoin(**item))
        return list(teams)

    team = graphene.Field(UserTeamJoin, team_name=graphene.String())

    def resolve_team(self, info, team_name):
        cursor = TeamModel.objects.aggregate(*[
            {
                "$match": {"team_name": team_name}
            },
            {
                "$lookup": {
                    "from": USER_TEAM_COLLECTION,
                    "localField": "_id",
                    "foreignField": "team_id",
                    "as": "user_team_data"
                }
            },
            {
                "$lookup": {
                    "from": USER_COLLECTION,
                    "localField": "user_team_data.user_id",
                    "foreignField": "_id",
                    "as": "team_members"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "team_id": "$_id",
                    "team_name": 1,
                    "status": 1,
                    "data_created": 1,
                    "team_members": {
                        "$map": {
                            "input": "$team_members",
                            "as": "team_members",
                            "in": {
                                "user_id": "$$team_members._id",
                                "email": "$$team_members.email",
                                "first_name": "$$team_members.first_name",
                                "last_name": "$$team_members.last_name",
                            }
                        }
                    }
                }
            },
        ])
        return UserTeamJoin(**list(cursor)[0])

    # Ticket Queries
    tickets = MongoengineConnectionField(TicketSchema)

    all_tickets = graphene.List(TicketSchema)

    def resolve_all_tickets(self, info):
        return list(TicketModel.objects().all())

    ticket = graphene.Field(
        TicketSchema, project_name=graphene.String(), ticket_number=graphene.Int())

    def resolve_ticket(self, info, project_name, ticket_number):
        return TicketModel.objects.get(project_name__iexact=project_name, ticket_number=ticket_number)

    # TicketStatus Queries
    ticket_statuses = MongoengineConnectionField(TicketStatusSchema)

    all_ticket_statuses = graphene.List(TicketStatusSchema)

    def resolve_all_ticket_statuses(self, info):
        return list(TicketStatusModel.objects().all())

    ticket_status = graphene.Field(
        TicketStatusSchema, status_id=graphene.ID())

    def resolve_ticket_status(self, info, status_id):
        return TicketStatusModel.objects.get(status_id=status_id)

    # User Queries
    # TODO - make a seperate user table without password
    users = MongoengineConnectionField(UserSchema)

    all_users = graphene.List(UserSchema)

    def resolve_all_users(self, info):
        return list(UserModel.objects().all())

    user = graphene.Field(UserSchema, user_id=graphene.ID())

    def resolve_user(self, info, user_id):
        return UserModel.objects.get(user_id=ObjectId(user_id))

    # UserTeam Queries
    user_teams = MongoengineConnectionField(UserTeamSchema)

    all_user_teams = graphene.List(UserTeamSchema)

    def resolve_all_user_teams(self, info):
        return list(UserTeamModel.objects().all())


class Mutation(graphene.ObjectType):
    # Project Mutations
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    update_project = UpdateProject.Field()

    # Sprint Mutations
    create_sprint = CreateSprint.Field()
    delete_sprint = DeleteSprint.Field()
    update_sprint = UpdateSprint.Field()

    # SprintProject Mutations
    create_sprint_project = CreateSprintProject.Field()
    delete_sprint_project = DeleteSprintProject.Field()
    update_sprint_project = UpdateSprintProject.Field()

    # Team Mutations
    create_team = CreateTeam.Field()
    delete_team = DeleteTeam.Field()
    update_team = UpdateTeam.Field()

    # Ticket Mutations
    create_ticket = CreateTicket.Field()
    delete_ticket = DeleteTicket.Field()
    update_ticket = UpdateTicket.Field()

    # Ticket Status Mutations
    create_ticket_status = CreateTicketStatus.Field()
    delete_ticket_status = DeleteTicketStatus.Field()
    update_ticket_status = UpdateTicketStatus.Field()

    # User Mutations
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()
    update_user = UpdateUser.Field()

    # UserTeam Mutations
    create_user_team = CreateUserTeam.Field()
    delete_user_team = DeleteUserTeam.Field()
    update_user_team = UpdateUserTeam.Field()


schema = graphene.Schema(
    query=Query, types=[ProjectSchema, SprintSchema, TeamSchema, TicketSchema, UserSchema, UserTeamSchema], mutation=Mutation)
