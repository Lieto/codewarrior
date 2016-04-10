import itertools


class Customer:
    new_id = itertools.count(start=1, step=1)

    def __init__(self, forename, surname):
        self.id = next(Customer.new_id)
        self.forename = forename
        self.surname = surname

    def buy(self, item, quantity):

        item.set_price(quantity=quantity)
        cost = item.price * quantity
        return cost



