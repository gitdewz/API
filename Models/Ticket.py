from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField

class Ticket(Document):
    meta = {"collection": "Ticket"}
    ticket_id = ObjectIdField(primary_key=True)
    ticket_number = IntField()
    project_name = StringField()
    sprint_id = IntField()
    ticket_type = StringField()
    priority = StringField()
    story_points = IntField()
    description = StringField()