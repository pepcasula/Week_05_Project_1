from unicodedata import name


class Bug:
    def __init__(self, short_name, description, product_name, first_reported, id=None):
        self.short_name = short_name
        self.description = description
        self.product_name = product_name
        self.first_reported = first_reported
        self.id = id