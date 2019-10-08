import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Schemas.ProjectSchema import CreateProject, DeleteProject, UpdateProject, ProjectSchema
from Schemas.TicketSchema import CreateTicket, DeleteTicket, UpdateTicket, TicketSchema
from Schemas.UserSchema import CreateUser, DeleteUser, UpdateUser, UserSchema
from bson import ObjectId


class Query(graphene.ObjectType):
    # Project Query
    projects = MongoengineConnectionField(ProjectSchema)

    # Ticket Query
    tickets = MongoengineConnectionField(TicketSchema)


class Mutation(graphene.ObjectType):
    # Project Mutations
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    update_project = UpdateProject.Field()

    # Ticket Mutations
    create_ticket = CreateTicket.Field()
    delete_ticket = DeleteTicket.Field()
    update_ticket = UpdateTicket.Field()

    # User Mutations
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()


schema = graphene.Schema(
    query=Query, types=[ProjectSchema, TicketSchema, UserSchema], mutation=Mutation)
