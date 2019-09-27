from Helpers.CollectionFunctions import CollectionFunctions
from Models.ApiBaseModel import ApiBaseModel

# TODO
# 1. Find a better way to make collection functions global
collectionFunctions = CollectionFunctions()
class Project(ApiBaseModel):
    def __init__(self, name):
        self.name = name
        item = collectionFunctions.findItem(self.__class__.__name__, {"name": self.name}, {"id": True})
        if (item):
            self.id = item["id"]
        if not (self.id):
            ApiBaseModel.__init__(self)
            self.tickets = []

    def __str__(self):
        return self.name