from Models.TicketModel import Ticket

def main():
    ticket = Ticket("Enhancement", "TEST")
    print(str(ticket))
    print(ticket.toJson())

if __name__ == '__main__':
    main()