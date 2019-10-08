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
from mongoengine import connect
# import jwt  # JSON Web Tokens

if __name__ == "__main__":
    collectionFunctions = CollectionFunctions()

    app = Flask(__name__)

    # TODO - figure out how to handle cors correctly ... might've changed with graphql
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Make the WSGI interface available at the top level so wfastcgi can get it.
    wsgi_app = app.wsgi_app

    def auth_required(fn):
        def wrapper(*args, **kwargs):
            # TODO - remove hardcoded default session header 12345
            session = request.headers.get("AUTH_HEADER", "12345")
            if collectionFunctions.authenticate(session):
                return fn(*args, **kwargs)
            return "not authenticated"
        return wrapper

    def graphql_view():
        view = GraphQLView.as_view("graphql", schema=schema, graphiql=True)
        return auth_required(view)

    app.add_url_rule("/graphql", view_func=graphql_view(), methods=["GET", "POST"])

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
