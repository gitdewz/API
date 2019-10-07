import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Ticket import Ticket as TicketModel
from bson import ObjectId
from Helpers.CollectionFunctions import CollectionFunctions

# TODO - recreate collection functions a better way,
# probably don't need them all with graphql
collectionFunctions = CollectionFunctions()

# Taylor is the best

class TicketSchema(MongoengineObjectType):
    class Meta:
        model = TicketModel
        interfaces = (Node,)

class CreateTicket(graphene.Mutation):
    ticket = graphene.Field(TicketSchema)

    class Arguments:
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        priority = graphene.String(required=False)
        sprint_id = graphene.Int(required=False)
        story_points = graphene.Int(required=False)
        ticket_type = graphene.String(required=False)


    def mutate(self, info, project_name, description, priority, sprint_id, story_points, ticket_type):
        ticket_number = 1
        if collectionFunctions.doesCollectionExist(self):
            collectionFunctions.findMax("Ticket", "ticket_number") + 1
        ticket = TicketModel(id=ObjectId(), ticket_number=ticket_number, project_name=project_name)
        ticket.description = description
        ticket.priority = priority
        ticket.sprint_id = sprint_id
        ticket.story_points = story_points
        ticket.ticket_type = ticket_type
        ticket.save()
        return CreateTicket(ticket)

class TicketInput(graphene.InputObjectType):
    project_name = graphene.String(required=False)
    sprint_id = graphene.Int(required=False)
    ticket_type = graphene.String(required=False)
    priority = graphene.String(required=False)
    story_points = graphene.Int(required=False)
    description = graphene.String(required=False)

class UpdateTicket(graphene.Mutation):
    ticket = graphene.Field(TicketSchema)

    class Arguments:
        ticket_id = graphene.ID(required=True)
        changes = TicketInput(required=True)

    def mutate(self, info, ticket_id, changes):
        ticket = TicketModel(id=ticket_id)
        for k, v in changes.items():
            ticket[k] = v
        ticket.update(**dict(changes.items()))
        return UpdateTicket(ticket)


class DeleteTicket(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        ticket_id = graphene.ID(required=True)

    def mutate(self, info, ticket_id):
        ticket = TicketModel(ticket_id=ticket_id)
        print(ticket.ticket_id)
        ticket.delete()
        return DeleteTicket(success=True)
