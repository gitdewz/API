########################
# No Longer Being Used #
########################

# from Models.ApiBaseModel import ApiBaseModel


# class User(ApiBaseModel):
#     def __init__(self, data):
#         # Project is required
#         self.id = data.get("id", None)
#         self.username = data.get("username", None)
#         self.password = data.get("password", None)
#         if self.id is None:
#             # New item, give it the next available ID
#             ApiBaseModel.__init__(self)
#         else:
#             # Passed in the ID, item must already exist
#             self.isNew = False
#             self.loadAttributes()

#     def __str__(self):
#         return f"User#{self.id}"
