import graphene
from Schemas.UserSchema import CreateUser, LoginUser, UserSchema


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()


login_schema = graphene.Schema(types=[UserSchema], mutation=Mutation)
