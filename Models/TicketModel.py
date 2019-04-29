from Models.ApiBaseModel import ApiBaseModel
import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["test"]

class Ticket(ApiBaseModel):
    def __init__(self, category, project):
        ApiBaseModel.__init__(self)
        self.category = category
        self.project = project
        collection = db[self.__class__.__name__]
        collection.insert(self.toJson())

    def __str__(self):
        return f"{self.project.upper()}-{self.id}"