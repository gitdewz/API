import graphene

class UserType(graphene.InputObjectType):
    user_id = graphene.ID(required=True)