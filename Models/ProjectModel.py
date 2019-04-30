from Models.ApiBaseModel import ApiBaseModel

class Project(ApiBaseModel):
    def __init__(self, name):
        ApiBaseModel.__init__(self)
        self.name = name
        self.tickets = []

    def __str__(self):
        return self.name