class Ticket:
    def __init__(self, bug, product, date_subm, user, ticket_status, id=None):
        self.bug = bug
        self.product = product
        self.date_subm = date_subm
        self.user = user
        self.ticket_status = ticket_status
        self.id = id
