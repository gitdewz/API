import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Project import Project as ProjectModel
from Models.Sprint import Sprint as SprintModel
from Models.Ticket import Ticket as TicketModel
from Schemas.ProjectSchema import CreateProject, DeleteProject, UpdateProject, ProjectSchema
from Schemas.SprintSchema import CreateSprint, DeleteSprint, UpdateSprint, SprintSchema
from Schemas.TicketSchema import CreateTicket, DeleteTicket, UpdateTicket, TicketSchema
from Schemas.UserSchema import CreateUser, DeleteUser, LoginUser, UpdateUser, UserSchema
from bson import ObjectId


class Query(graphene.ObjectType):
    # Project Queries
    projects = MongoengineConnectionField(TicketSchema)

    all_projects = graphene.List(ProjectSchema)

    def resolve_all_projects(self, info):
        return list(ProjectModel.objects().all())

    # Sprint Queries
    sprints = MongoengineConnectionField(SprintSchema)

    all_sprints = graphene.List(SprintSchema)

    def resolve_all_sprints(self, info):
        return list(SprintModel.objects().all())

    # Ticket Queries
    tickets = MongoengineConnectionField(TicketSchema)

    all_tickets = graphene.List(TicketSchema)

    def resolve_all_tickets(self, info):
        return list(TicketModel.objects().all())


class Mutation(graphene.ObjectType):
    # Project Mutations
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    update_project = UpdateProject.Field()

    # Sprint Mutations
    create_sprint = CreateSprint.Field()
    delete_sprint = DeleteSprint.Field()
    update_project = UpdateSprint.Field()

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
