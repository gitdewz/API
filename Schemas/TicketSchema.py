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
        title = graphene.String(required=False)
        priority = graphene.String(required=False)
        sprint_name = graphene.String(required=False)
        project_name = graphene.String(required=False)
        story_points = graphene.Int(required=False)
        ticket_type = graphene.String(required=False)
        active_user_id = graphene.ID(required=False)
        status_id = graphene.ID(required=False)
        sprint_project_id = graphene.ID(required=False)
        kanban_index = graphene.Int(required=False)

    def mutate(self, info, description=None, title=None, priority=None, sprint_name=None, project_name="NOPROJECT",
               story_points=None, ticket_type=None, active_user_id=None, status_id=None, sprint_project_id=None, kanban_index=-1):
        collectionFunctions = CollectionFunctions()
        if project_name != "NOPROJECT" and not status_id:
            status_id = collectionFunctions.get_default_status_id(project_name)
        project_name = project_name.upper()
        ticket_number = collectionFunctions.findNextId(
            "Ticket", {"project_name": project_name}, "ticket_number")
        ticket = TicketModel(
            id=ObjectId(), ticket_number=ticket_number, project_name=project_name)
        ticket.description = description
        ticket.title = title
        ticket.priority = priority
        ticket.sprint_name = sprint_name
        ticket.story_points = story_points
        ticket.ticket_type = ticket_type
        ticket.active_user_id = active_user_id
        ticket.status_id = status_id
        ticket.sprint_project_id = sprint_project_id
        ticket.kanban_index = kanban_index
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
    title = graphene.String(required=False)
    active_user_id = graphene.ID(required=False)
    status_id = graphene.ID(required=False)
    sprint_project_id = graphene.ID(required=False)
    kanban_index = graphene.Int(required=False)


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


class OrderInput(graphene.InputObjectType):
    class TicketOrder(graphene.InputObjectType):
        ticket_id = graphene.ID()
        kanban_index = graphene.Int()
    ticket_order = graphene.List(TicketOrder)


class UpdateTicketOrder(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        ticket_order = OrderInput(required=True)

    def mutate(self, info, ticket_order):
        # TODO:
        # 1. Can you update all of these at once with update_many or something?
        for change in ticket_order["ticket_order"]:
            ticket = TicketModel.objects.get(ticket_id=ObjectId(change.ticket_id))
            ticket.update(kanban_index=change.kanban_index)
        success = True
        return UpdateTicketOrder(success)


class DeleteTicket(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        ticket_id = graphene.ID(required=True)

    def mutate(self, info, ticket_id):
        ticket = TicketModel.objects.get(ticket_id=ObjectId(ticket_id))
        ticket.delete()
        return DeleteTicket(success=True)
