import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.Project import Project as ProjectModel
from bson import ObjectId

class ProjectSchema(MongoengineObjectType):
    class Meta:
        model = ProjectModel
        interfaces = (Node,)

class CreateProject(graphene.Mutation):
    project = graphene.Field(ProjectSchema)

    class Arguments:
        project_number = graphene.Int(required=True)
        project_name = graphene.String(required=True)

    def mutate(self, info, project_number, project_name):
        project = ProjectModel(id=ObjectId(), project_number=project_number, project_name=project_name)
        #project.id = f"{project.project_name}{project.project_id}"
        print(project.project_id)
        project.save()
        return CreateProject(project)

class ProjectInput(graphene.InputObjectType):
    project_name = graphene.String(required=False)
    sprint_id = graphene.Int(required=False)
    project_type = graphene.String(required=False)
    priority = graphene.String(required=False)
    story_points = graphene.Int(required=False)
    description = graphene.String(required=False)

class UpdateProject(graphene.Mutation):
    project = graphene.Field(ProjectSchema)

    class Arguments:
        project_id = graphene.ID(required=True)
        changes = ProjectInput(required=True)

    def mutate(self, info, project_id, changes):
        project = ProjectModel(id=project_id)
        for k, v in changes.items():
            project[k] = v
        project.update(**dict(changes.items()))
        return UpdateProject(project)


class DeleteProject(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        project_id = graphene.ID(required=True)

    def mutate(self, info, project_id):
        project = ProjectModel(project_id=project_id)
        print(project.project_id)
        project.delete()
        return DeleteProject(success=True)

class Query(graphene.ObjectType):
    projects = MongoengineConnectionField(ProjectSchema)

class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()

schema = graphene.Schema(query=Query, types=[ProjectSchema], mutation=Mutation)
# getProjects = graphene.Schema(query=Query, types=[ProjectSchema])