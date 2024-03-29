from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField
from GLOBAL import TICKET_COLLECTION


class Ticket(Document):
    meta = {
        "collection": TICKET_COLLECTION,
        "indexes": [
            {
                "fields": ["+project_name", "+sprint_name"]
            }
        ]
    }
    ticket_id = ObjectIdField(primary_key=True)
    ticket_number = IntField(unique_with="project_name")
    project_name = StringField(
        unique_with="ticket_number", default="NOPROJECT")
    sprint_name = StringField()
    ticket_type = StringField()
    priority = StringField()
    story_points = IntField()
    title = StringField(unique=True)
    description = StringField()
    active_user_id = ObjectIdField()
    status_id = ObjectIdField()
    sprint_project_id = ObjectIdField()
    kanban_index = IntField(default=-1)
