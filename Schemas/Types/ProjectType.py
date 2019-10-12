import graphene

class ProjectType(graphene.InputObjectType):
    project_id = graphene.ID(required=True)