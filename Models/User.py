from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField, EmailField
from GLOBAL import USER_COLLECTION


class User(Document):
    meta = {"collection": USER_COLLECTION}
    user_id = ObjectIdField(primary_key=True)
    email = EmailField(unique=True)
    password = StringField()
    first_name = StringField()
    last_name = StringField()
