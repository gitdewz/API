from Models.TicketModel import Ticket
from Models.ProjectModel import Project

def main():
    project = Project("Newgirra")
    print(str(project))
    print(project.toJson())

if __name__ == '__main__':
    main()
