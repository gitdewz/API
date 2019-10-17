import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.SprintProject import SprintProject as SprintProjectModel
from bson import ObjectId
from Helpers.CollectionFunctions import CollectionFunctions


class SprintProjectSchema(MongoengineObjectType):
    class Meta:
        model = SprintProjectModel
        interfaces = (Node,)


class CreateSprintProject(graphene.Mutation):
    sprint_project = graphene.Field(SprintProjectSchema)

    class Arguments:
        sprint_id = graphene.ID(required=True)
        project_id = graphene.ID(required=True)

    def mutate(self, info, sprint_id, project_id):
        sprint_project = SprintProjectModel(
            id=ObjectId(), sprint_id=sprint_id, project_id=project_id)
        sprint_project.save()
        return CreateSprintProject(sprint_project)


class SprintProjectInput(graphene.InputObjectType):
    sprint_id = graphene.ID(required=True)
    project_id = graphene.ID(required=True)


class UpdateSprintProject(graphene.Mutation):
    sprint_project = graphene.Field(SprintProjectSchema)

    class Arguments:
        changes = SprintProjectInput(required=True)
        sprint_project_id = graphene.ID(required=True)

    def mutate(self, info, sprint_project_id, changes):
        sprint_project = SprintProjectModel.objects.get(
            sprint_project_id=ObjectId(sprint_project_id))
        for k, v in changes.items():
            sprint_project[k] = v
        sprint_project.update(**dict(changes.items()))
        return UpdateSprintProject(sprint_project)


class DeleteSprintProject(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        sprint_project_id = graphene.ID(required=True)

    def mutate(self, info, sprint_project_id):
        sprint_project = SprintProjectModel.objects.get(
            sprint_project_id=ObjectId(sprint_project_id))
        sprint_project.delete()
        return DeleteSprintProject(success=True)
