from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, ObjectIdField, StringField
from GLOBAL import TEAM_COLLECTION


class Team(Document):
    meta = {"collection": TEAM_COLLECTION}
    team_id = ObjectIdField(primary_key=True)
    team_name = StringField(unique=True)
    status = StringField()
    date_created = DateTimeField()
