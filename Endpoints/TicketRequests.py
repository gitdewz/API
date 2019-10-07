'''
# No Longer Being Used

# from bson.json_util import dumps
# from flask import abort, Response
# from flask_restful import request, Resource
# from Helpers.CollectionFunctions import CollectionFunctions
# from Models.Ticket import Ticket as TicketModel

# collectionFunctions = CollectionFunctions()

# class TicketRequests(Resource):
#     def get(self, projectName, ticketId):
#         # TODO
#         # 1. Authenticated requests
#         if (True):  # authentication
#             data = {"id": int(ticketId)}
#             ticket = Ticket(data)
#             response = Response(
#                 response=dumps(vars(ticket)),
#                 status=200,
#             )
#             return response
#         else:
#             response = Response(
#                 response=dumps({
#                     "id": 1,
#                     "error": "unauthorized",
#                     "message": "User is not authorized to make this request.",
#                 }),
#                 status=401,
#             )
#             return abort(response)

#     def post(self):
#         if (True):  # authentication
#             data = request.json
#             print(data)
#             ticket = Ticket(data)
#             ticket.save()
#             response = Response(
#                 response=dumps(vars(ticket)),
#                 status=200,
#             )
#             return response
#         else:
#             response = Response(
#                 response=dumps({
#                     "id": 1,
#                     "error": "unauthorized",
#                     "message": "User is not authorized to make this request.",
#                 }),
#                 status=401,
#             )
#             return abort(response)

#     def put(self):
#         if (True):  # authentication
#             data = request.json()
#             ticket = Ticket(data)
#             ticket.save()
#             response = Response(
#                 response=dumps(vars(ticket)),
#                 status=200,
#             )
#             return response
#         else:
#             response = Response(
#                 response=dumps({
#                     "id": 1,
#                     "error": "unauthorized",
#                     "message": "User is not authorized to make this request.",
#                 }),
#                 status=401,
#             )
#             return abort(response)
'''
