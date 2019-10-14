from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, ObjectIdField, StringField
from GLOBAL import SPRINT_COLLECTION


class Sprint(Document):
    meta = {"collection": SPRINT_COLLECTION}
    sprint_id = ObjectIdField(primary_key=True)
    sprint_name = StringField(unique=True)
    goal = StringField()
    date_start = DateTimeField()
    date_end = DateTimeField()
