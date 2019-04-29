from Models.TicketModel import Ticket
from Models.ProjectModel import Project

def main():
    ticket = Ticket("Enhancement", "TEST")
    print(str(ticket))
    print(ticket.toJson())
    print()
    
    project = Project("Newgirra")
    print(str(project))
    print(project.toJson())

if __name__ == '__main__':
    main()