import json
from bson import ObjectId
from flask import Response
from flask_restful import Resource
from Helpers.CollectionFunctions import CollectionFunctions

class LoginRequests(Resource):
    
    def get(self, token):
        collectionFunctions = CollectionFunctions()
        session = collectionFunctions.get_session(token)
        for key in session:
            if isinstance(session[key], ObjectId):
                session[key] = str(session[key])
        return Response(json.dumps(session), mimetype="application/json")
