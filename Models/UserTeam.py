from mongoengine import Document
from mongoengine.fields import ObjectIdField


class UserTeam(Document):
    meta = {"collection": "UserTeam"}
    user_team_id = ObjectIdField(primary_key=True)
    user_id = ObjectIdField(required=True)
    team_id = ObjectIdField(required=True)
