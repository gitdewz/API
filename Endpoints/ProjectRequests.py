from bson.json_util import dumps
from flask import abort, Response
from flask_restful import request, Resource
from Helpers.CollectionFunctions import CollectionFunctions
from Models.ProjectModel import Project

collectionFunctions = CollectionFunctions()

class ProjectRequests(Resource):
    def get(self, projectName):
        # TODO
        # 1. Authenticated requests
        if (True):  # authentication
            project = Project(projectName)
            response = Response(
                response=dumps(vars(project)),
                status=200,
            )
            return response
        else:
            response = Response(
                response=dumps({
                    "id": 1,
                    "error": "unauthorized",
                    "message": "User is not authorized to make this request.",
                }),
                status=401,
            )
            return abort(response)
