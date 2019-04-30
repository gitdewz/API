from Models.ApiBaseModel import ApiBaseModel

class Ticket(ApiBaseModel):
    def __init__(self, data):
        self.id = data.get("id", None) 
        if self.id is None:
            # New item, give it the next available ID
            ApiBaseModel.__init__(self)
        else:
            # Passed in the ID, item must already exist
            self.isNew = False
        self.project = data.get("project", None)
        self.category = data.get("category", None)

    def __str__(self):
        return f"{self.project.upper()}-{self.id}"