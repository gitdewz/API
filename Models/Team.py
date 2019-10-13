from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, ObjectIdField, StringField


class Team(Document):
    meta = {"collection": "Team"}
    team_id = ObjectIdField(primary_key=True)
    team_name = StringField(unique=True)
    members = ListField(field=ObjectIdField(), default=[])
    status = StringField()
    date_created = DateTimeField()
