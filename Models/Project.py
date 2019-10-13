from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField


class Project(Document):
    meta = {"collection": "Project"}
    project_id = ObjectIdField(primary_key=True)
    project_name = StringField(unique=True)
    team_id = ObjectIdField()
    description = StringField()
