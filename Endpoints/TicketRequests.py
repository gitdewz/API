from bson.json_util import dumps
from flask import abort, Response
from flask_restful import request, Resource
from Helpers.CollectionFunctions import CollectionFunctions
from Models.TicketModel import Ticket

collectionFunctions = CollectionFunctions()

class TicketRequests(Resource):
    def get(self, project, ticketId):
        # TODO
        # 1. Authenticated requests
        if (True):  # authentication
            data = {"id": int(ticketId)}
            ticket = Ticket(project, data)
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
