import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from TicketSchema import CreateTicket, DeleteTicket, UpdateTicket, TicketSchema
from ProjectSchema import CreateProject, DeleteProject, UpdateProject, ProjectSchema
from bson import ObjectId

class Query(graphene.ObjectType):
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

schema = graphene.Schema(query=Query, types=[TicketSchema], mutation=Mutation)