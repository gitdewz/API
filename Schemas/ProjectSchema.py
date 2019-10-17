import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from Models.Project import Project as ProjectModel
from bson import ObjectId


class ProjectSchema(MongoengineObjectType):
    class Meta:
        model = ProjectModel
        interfaces = (Node,)


class CreateProject(graphene.Mutation):
    project = graphene.Field(ProjectSchema)

    class Arguments:
        project_name = graphene.String(required=True)
        team_id = graphene.ID(required=False)
        description = graphene.String(required=False)

    def mutate(self, info, project_name, team_id=None, description=None):
        project = ProjectModel(
            id=ObjectId(), project_name=project_name, team_id=ObjectId(team_id), description=description)
        project.save()
        return CreateProject(project)


class ProjectInput(graphene.InputObjectType):
    project_name = graphene.String(required=False)
    team_id = graphene.ID(required=False)
    description = graphene.String(required=False)


class UpdateProject(graphene.Mutation):
    project = graphene.Field(ProjectSchema)

    class Arguments:
        changes = ProjectInput(required=True)
        project_id = graphene.ID(required=True)

    def mutate(self, info, project_id, changes):
        project = ProjectModel.objects.get(project_id=ObjectId(project_id))
        for k, v in changes.items():
            if (k == "team_id"):
                project[k] = ObjectId(v)
            else:
                project[k] = v
        project.update(**dict(changes.items()))
        return UpdateProject(project)


class DeleteProject(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        project_id = graphene.ID(required=True)

    def mutate(self, info, project_id):
        project = ProjectModel.objects.get(project_id=ObjectId(project_id))
        project.delete()
        return DeleteProject(success=True)
