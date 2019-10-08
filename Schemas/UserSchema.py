import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.User import User as UserModel
from bson import ObjectId
from Helpers.CollectionFunctions import CollectionFunctions

# TODO - recreate collection functions a better way,
# probably don't need them all with graphql
collectionFunctions = CollectionFunctions()

# Taylor is the best


class UserSchema(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node,)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserSchema)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, info, email, password, first_name, last_name):
        user = UserModel(id=ObjectId(), email=email, password=password,
                         first_name=first_name, last_name=last_name)
        user.save()
        return CreateUser(user)


class UserInput(graphene.InputObjectType):
    user_id = graphene.String(required=False)
    email = graphene.String(required=False)
    password = graphene.Int(required=False)
    first_name = graphene.Int(required=False)
    last_name = graphene.String(required=False)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserSchema)

    class Arguments:
        changes = UserInput(required=True)
        user = UserInput(required=True)

    def mutate(self, info, user, changes):
        user = UserModel(**dict(user.items()))
        for k, v in changes.items():
            user[k] = v
        user.update(**dict(changes.items()))
        return UpdateUser(user)


class DeleteUser(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        user_id = graphene.ID(required=True)

    def mutate(self, info, user_id):
        user = UserModel(user_id=user_id)
        user.delete()
        return DeleteUser(success=True)
