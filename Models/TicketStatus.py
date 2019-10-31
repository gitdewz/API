from mongoengine import Document
from mongoengine.fields import IntField, ObjectIdField, StringField
from GLOBAL import TICKET_STATUS_COLLECTION


class TicketStatus(Document):
    meta = {"collection": TICKET_STATUS_COLLECTION}
    status_id = ObjectIdField(primary_key=True)
    status_order = IntField(unique_with="project_id")
    status_label = StringField(unique_with="project_id")
    project_id = ObjectIdField()
