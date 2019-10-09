from mongoengine import Document
from mongoengine.fields import DateField, ListField, ObjectIdField, StringField


class Team(Document):
    meta = {"collection": "Team"}
    team_id = ObjectIdField(primary_key=True)
    team_name = StringField(unique=True)
    members = ListField(default=[])
    projects = ListField(default=[])
    status = StringField()
    date_created = DateField()
