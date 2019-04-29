from Controllers.CollectionController import CollectionController

class ApiBaseModel:
    def __init__(self):
        collectionController = CollectionController()
        if not collectionController.doesCollectionExist(self):
            self.id = 1
        else:
            self.id = collectionController.findMax(self, "id") + 1

    def toJson(self):
        return vars(self)

    def insert(self):
        collectionController = CollectionController()
        collectionController.insert(self)
