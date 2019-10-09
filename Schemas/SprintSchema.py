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
        date_start = graphene.Date(required=False)
        date_end = graphene.Date(required=False)

    def mutate(self, info, sprint_name, goal, date_start, date_end):
        sprint = SprintModel(
            id=ObjectId(), sprint_name=sprint_name, goal=goal, date_start=date_start, date_end=date_end)
        sprint.save()
        return CreateSprint(sprint)


class SprintInput(graphene.InputObjectType):
    sprint_name = graphene.String(required=False)
    goal = graphene.String(required=False)
    date_start = graphene.Date(required=False)
    date_end = graphene.Date(required=False)


class UpdateSprint(graphene.Mutation):
    sprint = graphene.Field(SprintSchema)

    class Arguments:
        sprint_id = graphene.ID(required=True)
        changes = SprintInput(required=True)

    def mutate(self, info, sprint_id, changes):
        sprint = SprintModel(id=sprint_id)
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
