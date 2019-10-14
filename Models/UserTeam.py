from mongoengine import Document
from mongoengine.fields import ObjectIdField
from GLOBAL import USER_TEAM_COLLECTION


class UserTeam(Document):
    meta = {"collection": USER_TEAM_COLLECTION}
    user_team_id = ObjectIdField(primary_key=True)
    user_id = ObjectIdField(required=True)
    team_id = ObjectIdField(required=True)
