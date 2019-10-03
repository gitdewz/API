import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Ticket import Ticket as TicketModel
from bson import ObjectId

class TicketSchema(MongoengineObjectType):
    class Meta:
        model = TicketModel
        interfaces = (Node,)

class CreateTicket(graphene.Mutation):
    ticket = graphene.Field(TicketSchema)

    class Arguments:
        ticket_number = graphene.Int(required=True)
        project_name = graphene.String(required=True)

    def mutate(self, info, ticket_number, project_name):
        ticket = TicketModel(id=ObjectId(), ticket_number=ticket_number, project_name=project_name)
        #ticket.id = f"{ticket.project_name}{ticket.ticket_id}"
        print(ticket.ticket_id)
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

class Query(graphene.ObjectType):
    tickets = MongoengineConnectionField(TicketSchema)

class Mutation(graphene.ObjectType):
    create_ticket = CreateTicket.Field()
    update_ticket = UpdateTicket.Field()
    delete_ticket = DeleteTicket.Field()

schema = graphene.Schema(query=Query, types=[TicketSchema], mutation=Mutation)
# getTickets = graphene.Schema(query=Query, types=[TicketSchema])