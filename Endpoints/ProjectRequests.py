from bson.json_util import dumps
from flask import abort, Response
from flask_restful import request, Resource
from Helpers.CollectionFunctions import CollectionFunctions
from Models.ProjectModel import Project

collectionFunctions = CollectionFunctions()

# Project is required
        self.project = project
        self.id = data.get("id", None)        
        if self.id is None:
            # New item, give it the next available ID
            ApiBaseModel.__init__(self)
        else:
            # Passed in the ID, item must already exist
            self.isNew = False
            self.loadAttributes()
        self.category = data.get("category", getattr(self, "category", None))

class ProjectRequests(Resource):
    def get(self, project):
        # TODO
        # 1. Authenticated requests
        if (True):  # authentication
            data = {"name": int(ticketId)}
            project = Project(project, data)
            response = Response(
                response=dumps(vars(ticket)),
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
