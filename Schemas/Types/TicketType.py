import graphene

class TicketType(graphene.InputObjectType):
    team_id = graphene.ID(required=True)