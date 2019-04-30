from Models.ApiBaseModel import ApiBaseModel

class Ticket(ApiBaseModel):
    def __init__(self, project: str, data):
        # Project is required
        self.project = project
        self.id = data.get("id", None)        
        if self.id is None:
            # New item, give it the next available ID
            ApiBaseModel.__init__(self)
        else:
            # Passed in the ID, item must already exist
            self.isNew = False
            self.loadAttributes()
        self.category = data.get("category", getattr(self, "category", None))

    def __str__(self):
        return f"{self.project.upper()}-{self.id}"