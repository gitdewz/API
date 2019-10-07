'''
# No Longer Being Used

# from bson.json_util import dumps
# from flask import abort, Flask, request, Response, session
# from flask_restful import Resource
# from Helpers.CollectionFunctions import CollectionFunctions
# from Models.UserModel import User
# import secrets

# collectionFunctions = CollectionFunctions()


# def authenticate(credentials):
#     # TODO
#     # 1. Correctly authenticate users, probably use jwt
#     return collectionFunctions.findUser(credentials)


# class RegistrationRequests(Resource):
#     # TODO
#     # 1. Do I need to use abort for bad requests?
#     def post(self):
#         print(request.json)
#         user = User(request.json)
#         if not (collectionFunctions.doesItemExist("User", "username", user.username)):
#             user.save()
#             response = Response(
#                 response=dumps({"token": secrets.token_hex()}),
#                 status=200,
#             )
#             return response
#         else:
#             response = Response(
#                 response=dumps({
#                     "id": 1,
#                     "error": "bad request",
#                     "message": "username taken please enter a different one",
#                 }),
#                 status=400,
#             )
#             return abort(response)


# class LoginRequests(Resource):
#     def post(self):
#         user = authenticate(request.json)
#         if user:
#             session["authenticated"] = True
#             response = Response(
#                 response=dumps({
#                     "token": secrets.token_hex(),
#                     "user": user,
#                 }),
#                 status=200,
#             )
#             print(response)
#             return response
#         else:
#             session["authenticated"] = False
#             response = Response(
#                 response=dumps({
#                     "id": 1,
#                     "error": "bad request",
#                     "message": "Invalid request path. TicketID must be an integer.",
#                 }),
#                 status=400,
#             )
#             return abort(response)
'''
