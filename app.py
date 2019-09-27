from bson.json_util import dumps
from flask import abort, Flask, Response, session
from flask_cors import CORS
from flask_restful import Api, request
from Helpers.CollectionFunctions import CollectionFunctions
from Models.TicketModel import Ticket
from Models.UserModel import User
import Endpoints.LoginRequests as LoginRequests
import Endpoints.ProjectRequests as ProjectRequests
import Endpoints.TicketRequests as TicketRequests
import os
import secrets
# import jwt  # JSON Web Tokens

app = Flask(__name__)

# TODO - figure out how to handle cors correctly
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

collectionFunctions = CollectionFunctions()

# User Requests
api.add_resource(LoginRequests.RegistrationRequests, "/register")
api.add_resource(LoginRequests.LoginRequests, "/login")

# Ticket Requests
api.add_resource(TicketRequests.TicketRequests, "/ticket/<string:projectName>/<int:ticketId>")

# Project Requests
api.add_resource(ProjectRequests.ProjectRequests, "/project/<string:projectName>")


if __name__ == "__main__":
    HOST=os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT=int(os.environ.get("SERVER_PORT", "5556"))
    except ValueError:
        PORT=5556
    app.secret_key=os.urandom(12)
    app.run(HOST, PORT)
