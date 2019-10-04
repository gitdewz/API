from mongoengine import Document
from mongoengine.fields import IntField, ListField, ObjectIdField, StringField

class Project(Document):
    meta = {"collection": "Project"}
    project_id = ObjectIdField(primary_key=True)
    project_name = StringField()
    description = StringField()
    tickets = ListField()