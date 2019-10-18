import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Ticket import Ticket as TicketModel
from bson import ObjectId
from Helpers.CollectionFunctions import CollectionFunctions

# Taylor is the best


class TicketSchema(MongoengineObjectType):
    class Meta:
        model = TicketModel
        interfaces = (Node,)


class CreateTicket(graphene.Mutation):
    ticket = graphene.Field(TicketSchema)

    class Arguments:
        project_name = graphene.String(required=False)
        description = graphene.String(required=False)
        priority = graphene.String(required=False)
        sprint_name = graphene.String(required=False)
        project_name = graphene.String(required=False)
        story_points = graphene.Int(required=False)
        ticket_type = graphene.String(required=False)
        active_user_id = graphene.ID(required=False)

    def mutate(self, info, description=None, priority=None, sprint_name=None, project_name="NOPROJECT", story_points=None, ticket_type=None, active_user_id=None):
        collectionFunctions = CollectionFunctions()
        project_name = project_name.upper()
        ticket_number = collectionFunctions.findNextId(
            "Ticket", {"project_name": project_name}, "ticket_number")
        ticket = TicketModel(
            id=ObjectId(), ticket_number=ticket_number, project_name=project_name)
        ticket.description = description
        ticket.priority = priority
        ticket.sprint_name = sprint_name
        ticket.story_points = story_points
        ticket.ticket_type = ticket_type
        ticket.active_user_id = active_user_id
        ticket.save()
        return CreateTicket(ticket)


class TicketInput(graphene.InputObjectType):
    project_name = graphene.String(required=False)
    ticket_number = graphene.Int(required=False)
    sprint_name = graphene.String(required=False)
    ticket_type = graphene.String(required=False)
    priority = graphene.String(required=False)
    story_points = graphene.Int(required=False)
    description = graphene.String(required=False)
    active_user_id = graphene.ID(required=False)


class UpdateTicket(graphene.Mutation):
    ticket = graphene.Field(TicketSchema)

    class Arguments:
        changes = TicketInput(required=True)
        ticket_id = graphene.ID(required=True)

    def mutate(self, info, ticket_id, changes):
        collectionFunctions = CollectionFunctions()
        ticket = TicketModel.objects.get(ticket_id=ObjectId(ticket_id))
        if "project_name" in changes.keys():
            ticket_number = collectionFunctions.findNextId(
                "Ticket", {"project_name": changes['project_name']}, "ticket_number")
            changes["ticket_number"] = ticket_number
        for k, v in changes.items():
            ticket[k] = v
        ticket.update(**dict(changes.items()))
        return UpdateTicket(ticket)


class DeleteTicket(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        ticket_id = graphene.ID(required=True)

    def mutate(self, info, ticket_id):
        ticket = TicketModel.objects.get(ticket_id=ObjectId(ticket_id))
        ticket.delete()
        return DeleteTicket(success=True)
