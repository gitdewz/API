from mongoengine import Document
from mongoengine.fields import DateField, ListField, ObjectIdField, StringField


class Sprint(Document):
    meta = {"collection": "Sprint"}
    sprint_id = ObjectIdField(primary_key=True)
    sprint_name = StringField(unique=True)
    goal = StringField()
    tickets = ListField(default=[])
    date_start = DateField()
    date_end = DateField()
