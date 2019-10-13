import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Project import Project as ProjectModel
from Models.Sprint import Sprint as SprintModel
from Models.Team import Team as TeamModel
from Models.Ticket import Ticket as TicketModel
from Models.User import User as UserModel
from Schemas.ProjectSchema import CreateProject, DeleteProject, UpdateProject, ProjectSchema
from Schemas.SprintSchema import CreateSprint, DeleteSprint, UpdateSprint, SprintSchema
from Schemas.TeamSchema import CreateTeam, DeleteTeam, UpdateTeam, TeamSchema
from Schemas.TicketSchema import CreateTicket, DeleteTicket, UpdateTicket, TicketSchema
from Schemas.UserSchema import CreateUser, DeleteUser, LoginUser, UpdateUser, UserSchema
from bson import ObjectId


class Query(graphene.ObjectType):
    # Project Queries
    projects = MongoengineConnectionField(ProjectSchema)

    all_projects = graphene.List(ProjectSchema)

    def resolve_all_projects(self, info):
        return list(ProjectModel.objects().all())

    # Sprint Queries
    sprints = MongoengineConnectionField(SprintSchema)

    all_sprints = graphene.List(SprintSchema)

    def resolve_all_sprints(self, info):
        return list(SprintModel.objects().all())

    # Team Queries
    teams = MongoengineConnectionField(TeamSchema)

    all_teams = graphene.List(TeamSchema)

    def resolve_all_teams(self, info):
        return list(TeamModel.objects().all())

    # Ticket Queries
    tickets = MongoengineConnectionField(TicketSchema)

    all_tickets = graphene.List(TicketSchema)

    def resolve_all_tickets(self, info):
        return list(TicketModel.objects().all())

    ticket = graphene.Field(
        TicketSchema, project_name=graphene.String(), ticket_number=graphene.Int())

    def resolve_ticket(self, info, project_name, ticket_number):
        return TicketModel.objects.get(project_name__iexact=project_name, ticket_number=ticket_number)

    # User Queries
    # TODO - make a seperate user table without password
    users = MongoengineConnectionField(UserSchema)

    all_users = graphene.List(UserSchema)

    def resolve_all_users(self, info):
        return list(UserModel.objects().all())


class Mutation(graphene.ObjectType):
    # Project Mutations
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    update_project = UpdateProject.Field()

    # Sprint Mutations
    create_sprint = CreateSprint.Field()
    delete_sprint = DeleteSprint.Field()
    update_sprint = UpdateSprint.Field()

    # Team Mutations
    create_team = CreateTeam.Field()
    delete_team = DeleteTeam.Field()
    update_team = UpdateTeam.Field()

    # Ticket Mutations
    create_ticket = CreateTicket.Field()
    delete_ticket = DeleteTicket.Field()
    update_ticket = UpdateTicket.Field()

    # User Mutations
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()
    update_user = UpdateUser.Field()


schema = graphene.Schema(
    query=Query, types=[ProjectSchema, TicketSchema, UserSchema], mutation=Mutation)
