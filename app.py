import pymongo
from bson.json_util import dumps
from flask import abort, Flask, request, Response, session
from flask_cors import CORS
from Helpers.CollectionFunctions import CollectionFunctions
from Login.LoginRequests import LoginRequests, RegisterRequests
from Models.Ticket import Ticket as TicketModel
import os
import secrets
from flask_graphql import GraphQLView
from Schemas.Schema import schema
from Schemas.LoginSchema import login_schema
from mongoengine import connect
from flask_restful import Api
import json
from GLOBAL import CLIENT_ENV_KEY, DB_NAME
# import jwt  # JSON Web Tokens

if __name__ == "__main__":
    os.environ[CLIENT_ENV_KEY] = "mongodb://localhost:27017/"
    collectionFunctions = CollectionFunctions()

    application = Flask(__name__)
    # TODO - figure out how to handle cors correctly ... might've changed with graphql
    CORS(application)

    api = Api(application)
    
    application.config["CORS_HEADERS"] = "Content-Type"

    # TODO - config test/prod environments
    application.config["DEV"] = True


    # Make the WSGI interface available at the top level so wfastcgi can get it.	
    # wsgi_app = application.wsgi_app

    api.add_resource(LoginRequests, "/rest/login", "/rest/login/<string:token>")
    api.add_resource(RegisterRequests, "/rest/register")

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
            return Response(json.dumps({"error": "not authenticated"}), status=405)
        return wrapper

    def graphql_view():
        view = GraphQLView.as_view("graphql", schema=schema, graphiql=True)
        # if (application.config["DEV"]):
        #     return view
        return auth_required(view)

    application.add_url_rule("/graphql", view_func=graphql_view(),
                     methods=["GET", "POST"])

    HOST = os.environ.get("SERVER_HOST", "localhost")
    mongo_client = pymongo.MongoClient(os.environ[CLIENT_ENV_KEY])
    print(mongo_client.list_database_names())

    try:
        PORT = int(os.environ.get("SERVER_PORT", "5556"))
        connect(DB_NAME, host=os.environ[CLIENT_ENV_KEY],
                alias="default")
    except ValueError:
        PORT = 5556
    application.secret_key = os.urandom(12)

    # DEBUG MODE ONLY TO STOP CORS ERRORS #
    application.config['PROPAGATE_EXCEPTIONS'] = False
    # DEBUG MODE ONLY TO STOP CORS ERRORS #
    application.run(HOST, PORT, debug=True)
