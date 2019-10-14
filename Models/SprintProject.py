from mongoengine import Document
from mongoengine.fields import ObjectIdField
from GLOBAL import SPRINT_PROJECT_COLLECTION


class SprintProject(Document):
    meta = {"collection": SPRINT_PROJECT_COLLECTION}
    sprint_project_id = ObjectIdField(primary_key=True)
    sprint_id = ObjectIdField(required=True)
    project_id = ObjectIdField(required=True)
