from Models.ApiBaseModel import ApiBaseModel

class Ticket(ApiBaseModel):
    def __init__(self, category, project):
        ApiBaseModel.__init__(self)
        self.category = category
        self.project = project
        self.insert()

    def __str__(self):
        return f"{self.project.upper()}-{self.id}"