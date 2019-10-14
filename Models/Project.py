from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField
from GLOBAL import PROJECT_COLLECTION


class Project(Document):
    meta = {"collection": PROJECT_COLLECTION}
    project_id = ObjectIdField(primary_key=True)
    project_name = StringField(unique=True)
    team_id = ObjectIdField()
    description = StringField()
