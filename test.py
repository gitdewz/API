from Models.TicketModel import Ticket
from Models.ProjectModel import Project

def main():
    ticket_data = {"category":"Enhancement", "project":"TEST"}
    ticket = Ticket(ticket_data)
    print(str(ticket))
    print(ticket.toJson())
    print()

    project = Project("Newgirra")
    print(str(project))
    print(project.toJson())

if __name__ == '__main__':
    main()
