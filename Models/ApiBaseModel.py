from Controllers.CollectionController import CollectionController

class ApiBaseModel:
    def __init__(self):
        self.isNew = True
        collectionController = CollectionController()
        if not collectionController.doesCollectionExist(self):
            self.id = 1
        else:
            self.id = collectionController.findMax(self, "id") + 1

    def toJson(self):
        return vars(self)

    def loadAttributes(self):
        collectionController = CollectionController()
        document = collectionController.findItem(self)
        for key in document:
            setattr(self, key, document[key])

    def save(self):
        collectionController = CollectionController()
        if self.isNew:
            collectionController.insert(self)
        else:
            collectionController.update(self)
