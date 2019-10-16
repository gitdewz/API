import pymongo
from bson.json_util import dumps
from flask import abort, Flask, request, Response, session
from flask_cors import CORS
from Helpers.CollectionFunctions import CollectionFunctions
from Models.Ticket import Ticket as TicketModel
import os
import secrets
from flask_graphql import GraphQLView
from Schemas.Schema import schema
from Schemas.LoginSchema import login_schema
from mongoengine import connect
from GLOBAL import CLIENT_ENV_KEY, DB_NAME
# import jwt  # JSON Web Tokens

collectionFunctions = CollectionFunctions()

connect(DB_NAME, host=os.environ[CLIENT_ENV_KEY],
                alias="default")

application = Flask(__name__)

# TODO - config test/prod environments
application.config["DEV"] = False

# TODO - figure out how to handle cors correctly ... might've changed with graphql
CORS(application, resources={r"/*": {"origins": "*"}})

def graphql_login():
    # TODO - graphiql should probably be false
    return GraphQLView.as_view("login", schema=login_schema, graphiql=True)

application.add_url_rule("/login", view_func=graphql_login())

def auth_required(fn):
    def wrapper(*args, **kwargs):
        # TODO - remove hardcoded default session header 12345
        token = request.headers.get("AUTHTOKEN", "")
        if collectionFunctions.authenticate(token):
            return fn(*args, **kwargs)
        return "not authenticated"
    return wrapper

def graphql_view():
    view = GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    if (application.config["DEV"]):
        return view
    return auth_required(view)

application.add_url_rule("/graphql", view_func=graphql_view(),
                    methods=["GET", "POST"])

application.secret_key = os.urandom(12)
