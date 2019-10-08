from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField, EmailField


class User(Document):
    meta = {"collection": "User"}
    user_id = ObjectIdField(primary_key=True)
    email = EmailField(unique=True)
    password = StringField()
    first_name = StringField()
    last_name = StringField()
