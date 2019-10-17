import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from Models.Team import Team as TeamModel
from bson import ObjectId


class TeamSchema(MongoengineObjectType):
    class Meta:
        model = TeamModel
        interfaces = (Node,)


class CreateTeam(graphene.Mutation):
    team = graphene.Field(TeamSchema)

    class Arguments:
        team_name = graphene.String(required=True)
        status = graphene.String(required=False)
        date_created = graphene.DateTime(required=False)

    def mutate(self, info, team_name, status=None, date_created=None):
        team = TeamModel(
            id=ObjectId(), team_name=team_name, status=status, date_created=date_created)
        team.save()
        return CreateTeam(team)


class TeamInput(graphene.InputObjectType):
    team_id = graphene.ID(required=False)
    team_name = graphene.String(required=False)
    status = graphene.String(required=False)
    date_created = graphene.DateTime(required=False)


class UpdateTeam(graphene.Mutation):
    team = graphene.Field(TeamSchema)

    class Arguments:
        changes = TeamInput(required=True)
        team_id = graphene.ID(required=True)

    def mutate(self, info, team_id, changes):
        team = TeamModel.objects.get(team_id=ObjectId(team_id))
        for k, v in changes.items():
            team[k] = v
        team.update(**dict(changes.items()))
        return UpdateTeam(team)


class DeleteTeam(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        team_id = graphene.ID(required=True)

    def mutate(self, info, team_id):
        team = TeamModel.objects.get(team_id=ObjectId(team_id))
        team.delete()
        return DeleteTeam(success=True)
