from bson.json_util import dumps
from flask import Flask
from Controllers.CollectionController import CollectionController
from Models.TicketModel import Ticket
import os

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

collectionController = CollectionController()

@app.route("/api/ticket/<project>/<ticketId>", methods=['get'])
def getTicket(project=None, ticketId=None):
    if project is not None and ticketId is not None:
        id = int(ticketId)
        project = project
        data = {"id": id, "project": project}
        ticket = Ticket(data)
        mongoData = collectionController.findItem(ticket)
        bsonData = dumps(mongoData)
        return bsonData
    else:
        return "Error: Invalid request path"


if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5556'))
    except ValueError:
        PORT = 5556
    app.secret_key = os.urandom(12)
    app.run(HOST, PORT)