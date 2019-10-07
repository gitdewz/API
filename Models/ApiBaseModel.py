########################
# No Longer Being Used #
########################

# from Helpers.CollectionFunctions import CollectionFunctions

# class ApiBaseModel:
#     def __init__(self):
#         self.isNew = True
#         collectionFunctions = CollectionFunctions()
#         if not collectionFunctions.doesCollectionExist(self):
#             self.id = 1
#         else:
#             self.id = collectionFunctions.findMax(self, "id") + 1

#     def toJson(self):
#         return vars(self)

#     def loadAttributes(self):
#         collectionFunctions = CollectionFunctions()
#         document = collectionFunctions.findItem(self.__class__.__name__, {"id": self.id}, {"_id": False})
#         for key in document:
#             setattr(self, key, document[key])

#     def save(self):
#         collectionFunctions = CollectionFunctions()
#         if self.isNew:
#             collectionFunctions.insert(self)
#         else:
#             collectionFunctions.update(self)
