import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from Models.Sprint import Sprint as SprintModel
from bson import ObjectId


class SprintSchema(MongoengineObjectType):
    class Meta:
        model = SprintModel
        interfaces = (Node,)


class CreateSprint(graphene.Mutation):
    sprint = graphene.Field(SprintSchema)

    class Arguments:
        sprint_name = graphene.String(required=True)
        goal = graphene.String(required=False)
        team_id = graphene.ID(required=False)
        project_id = graphene.ID(required=False)
        date_start = graphene.DateTime(required=False)
        date_end = graphene.DateTime(required=False)

    def mutate(self, info, sprint_name, goal=None, team_id=None, project_id=None, date_start=None, date_end=None):
        sprint = SprintModel(
            id=ObjectId(), sprint_name=sprint_name, goal=goal, team_id=team_id, project_id=project_id, date_start=date_start, date_end=date_end)
        sprint.save()
        return CreateSprint(sprint)


class SprintInput(graphene.InputObjectType):
    sprint_id = graphene.ID(required=False)
    sprint_name = graphene.String(required=False)
    goal = graphene.String(required=False)
    team_id = graphene.String(required=False)
    project_id = graphene.ID(required=False)
    date_start = graphene.DateTime(required=False)
    date_end = graphene.DateTime(required=False)


class UpdateSprint(graphene.Mutation):
    sprint = graphene.Field(SprintSchema)

    class Arguments:
        changes = SprintInput(required=True)
        sprint = SprintInput(required=True)

    def mutate(self, info, sprint, changes):
        sprint = SprintModel(**dict(sprint.items()))
        for k, v in changes.items():
            sprint[k] = v
        sprint.update(**dict(changes.items()))
        return UpdateSprint(sprint)


class DeleteSprint(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        sprint_id = graphene.ID(required=True)

    def mutate(self, info, sprint_id):
        sprint = SprintModel(sprint_id=sprint_id)
        sprint.delete()
        return DeleteSprint(success=True)
