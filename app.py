import pymongo
from bson.json_util import dumps
from flask import abort, Flask, Response, session
from flask_cors import CORS
from flask_restful import Api, request
from Helpers.CollectionFunctions import CollectionFunctions
from Models.Ticket import Ticket as TicketModel
import os
import secrets
from flask_graphql import GraphQLView
from Schemas.Schema import schema
from mongoengine import connect
# import jwt  # JSON Web Tokens

app = Flask(__name__)

# TODO - figure out how to handle cors correctly
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

collectionFunctions = CollectionFunctions()

'''
# No Longer Being Used #

# User Requests
# api.add_resource(LoginRequests.RegistrationRequests, "/register")
# api.add_resource(LoginRequests.LoginRequests, "/login")

# # Ticket Requests
# api.add_resource(TicketRequests.TicketRequests, "/ticket",
#                  "/ticket/<string:projectName>/<int:ticketId>")

# # Project Requests
# api.add_resource(ProjectRequests.ProjectRequests,
#                  "/project/<string:projectName>")
'''

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))


if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(mongo_client.list_database_names())
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5556"))
        connect("mongoengine", host="mongodb://localhost:27017/", alias="default")
    except ValueError:
        PORT = 5556
    app.secret_key = os.urandom(12)
    app.run(HOST, PORT)
