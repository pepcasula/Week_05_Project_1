class Bug:
    def __init__(self, short_name, description, product, first_reported, id=None):
        self.short_name = short_name
        self.description = description
        self.product = product
        self.first_reported = first_reported
        self.id = id