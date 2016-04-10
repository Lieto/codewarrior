import itertools


class Item:

    new_id = itertools.count(start=1, step=1)

    def __init__(self, name):
        self.id = next(Item.new_id)
        self.name = name
        self.price = 0.0

    def set_price(self, quantity):

        self.price = 4.0

        if quantity > 3:
            self.price -= 1

        if quantity > 5:
            self.price -= 1
