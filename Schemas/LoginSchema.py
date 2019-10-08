import graphene
from Schemas.UserSchema import LoginUser, UserSchema


class Mutation(graphene.ObjectType):
    login_user = LoginUser.Field()


login_schema = graphene.Schema(types=[UserSchema], mutation=Mutation)
