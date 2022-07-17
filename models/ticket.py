class Ticket:
    def __init__(self, bug_name, product_name, date_subm, user_name, ticket_status, id=None):
        self.bug_name = bug_name
        self.product_name = product_name
        self.date_subm = date_subm
        self.user_name = user_name
        self.ticket_status = ticket_status
        self.id = id
