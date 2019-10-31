import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from Models.TicketStatus import TicketStatus as TicketStatusModel
from bson import ObjectId


class TicketStatusSchema(MongoengineObjectType):
    class Meta:
        model = TicketStatusModel
        interfaces = (Node,)


class CreateTicketStatus(graphene.Mutation):
    ticket_status = graphene.Field(TicketStatusSchema)

    class Arguments:
        status_order = graphene.Int(required=True)
        status_label = graphene.String(required=True)
        project_id = graphene.ID(required=True)

    def mutate(self, info, status_order, status_label, project_id):
        ticket_status = TicketStatusModel(
            id=ObjectId(), status_order=status_order, status_label=status_label, project_id=project_id)
        ticket_status.save()
        return CreateTicketStatus(ticket_status)


class TicketStatusInput(graphene.InputObjectType):
    status_id = graphene.ID(required=False)
    status_order = graphene.Int(required=False)
    status_label = graphene.String(required=False)
    project_id = graphene.ID(required=False)


class UpdateTicketStatus(graphene.Mutation):
    ticket_status = graphene.Field(TicketStatusSchema)

    class Arguments:
        changes = TicketStatusInput(required=True)
        status_id = graphene.ID(required=True)

    def mutate(self, info, status_id, changes):
        ticket_status = TicketStatusModel.objects.get(
            ticket_status_id=ObjectId(status_id))
        for k, v in changes.items():
            ticket_status[k] = v
        ticket_status.update(**dict(changes.items()))
        return UpdateTicketStatus(ticket_status)


class DeleteTicketStatus(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        status_id = graphene.ID(required=True)

    def mutate(self, info, status_id):
        ticket_status = TicketStatusModel.objects.get(
            status_id=ObjectId(status_id))
        ticket_status.delete()
        return DeleteTicketStatus(success=True)
