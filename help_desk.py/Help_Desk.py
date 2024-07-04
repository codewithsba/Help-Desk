import datetime

class Ticket:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = "open"
        self.timestamp = datetime.datetime.now()

    def close(self):
        self.status = "closed"

    def reopen(self):
        self.status = "open"

tickets = []

def create_ticket(title, description):
    """Create a new ticket."""
    id = len(tickets) + 1
    new_ticket = Ticket(id, title, description)
    tickets.append(new_ticket)
    print(f"Ticket {id} created.")

def view_tickets():
    """View all tickets."""
    if not tickets:
        print("No tickets.")
    else:
        for ticket in tickets:
            print(f"ID: {ticket.id}, Title: {ticket.title}, Status: {ticket.status}")

def update_ticket_status(ticket_id, new_status):
    """Update the status of a specific ticket."""
    for ticket in tickets:
        if ticket.id == ticket_id:
            if hasattr(ticket, 'close') and hasattr(ticket, 'reopen'):
                if new_status.lower() == 'close':
                    ticket.close()
                elif new_status.lower() == 'reopen':
                    ticket.reopen()
                else:
                    print("Invalid status. Use 'close' or 'reopen'.")
            else:
                print("This operation is not supported for this ticket.")
            break
    else:
        print("Ticket not found.")

def delete_ticket(ticket_id):
    """Delete a ticket."""
    global tickets
    tickets = [ticket for ticket in tickets if ticket.id != ticket_id]
    print(f"Ticket {ticket_id} deleted.")

# Example usage
create_ticket("Network Issue", "Can't connect to the internet.")
view_tickets()
update_ticket_status(1, "close")  # Assuming the first ticket is ID 1
view_tickets()
delete_ticket(1)
view_tickets()
