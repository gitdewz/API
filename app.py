from bson.json_util import dumps
from flask import Flask
from Helpers.CollectionFunctions import CollectionFunctions
from Models.TicketModel import Ticket
import os

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

collectionFunctions = CollectionFunctions()

@app.route("/api/ticket/<project>/<ticketId>", methods=['get'])
def getTicket(project=None, ticketId=None):
    if ticketId.isdigit():
        data = {"id": int(ticketId) }
        ticket = Ticket(project, data)
        return dumps(vars(ticket))
    else:
        return dumps({"Error": "Invalid request path. TicketID must be an integer."})


if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5556'))
    except ValueError:
        PORT = 5556
    app.secret_key = os.urandom(12)
    app.run(HOST, PORT)