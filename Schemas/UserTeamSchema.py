import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.UserTeam import UserTeam as UserTeamModel
from bson import ObjectId
from Helpers.CollectionFunctions import CollectionFunctions

class UserTeamSchema(MongoengineObjectType):
    class Meta:
        model = UserTeamModel
        interfaces = (Node,)


class CreateUserTeam(graphene.Mutation):
    user_team = graphene.Field(UserTeamSchema)

    class Arguments:
        user_id = graphene.ID(required=True)
        team_id = graphene.ID(required=True)

    def mutate(self, info, user_id, team_id):
        user_team = UserTeamModel(
            id=ObjectId(), user_id=user_id, team_id=team_id)
        user_team.save()
        return CreateUserTeam(user_team)


class UserTeamInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    team_id = graphene.ID(required=True)


class UpdateUserTeam(graphene.Mutation):
    user_team = graphene.Field(UserTeamSchema)

    class Arguments:
        changes = UserTeamInput(required=True)
        user_team_id = graphene.ID(required=True)

    def mutate(self, info, user_team_id, changes):
        user_team = UserTeamModel.objects.get(user_team_id=ObjectId(user_team_id))
        for k, v in changes.items():
            user_team[k] = v
        user_team.update(**dict(changes.items()))
        return UpdateUserTeam(user_team)


class DeleteUserTeam(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        user_team_id = graphene.ID(required=True)

    def mutate(self, info, user_team_id):
        user_team = UserTeamModel.objects.get(user_team_id=ObjectId(user_team_id))
        user_team.delete()
        return DeleteUserTeam(success=True)
