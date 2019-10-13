from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, ObjectIdField, StringField


class Sprint(Document):
    meta = {"collection": "Sprint"}
    sprint_id = ObjectIdField(primary_key=True)
    sprint_name = StringField(unique=True)
    goal = StringField()
    date_start = DateTimeField()
    date_end = DateTimeField()
