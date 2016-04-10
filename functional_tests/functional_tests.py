import unittest
import numpy as np
import matplotlib.pyplot as plt


from Customer import Customer
from Item import Item


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Vesa", "Kuoppala")
        self.item = Item("Ball")

    def tearDown(self):
        pass

# Case 1:
# Customer buys 4 items of the same kind from store, the total cost is 12$
    def test_customer_buys_four_items_and_cost_is_12_dollars(self):
        cost = self.customer.buy(self.item, 4)
        self.assertEqual(cost, 12)

# Case 2:
# Customer buys 3 items of the same kind from store, the total cost is 12$
    def test_customer_buys_three_items_and_cost_is_12_dollars(self):
        cost = self.customer.buy(self.item, 3)
        self.assertEqual(cost, 12)


# Plot a table. Quantity varies from 0 to 8
class PlotTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Vesa", "Kuoppala")
        self.item = Item("Ball")
        self.quantities = np.arange(0, 8, 1)

    def tearDown(self):
        None

    def test_customer_creates_table_for_quantities(self):

        # Add data to list
        data = []

        for i in self.quantities:
            data_row = []
            data_row.append(i)
            self.item.set_price(i)
            data_row.append(self.item.price)
            data_row.append(self.customer.buy(self.item, i))
            data.append(data_row)

        # Define column and row labels for table
        columns = ('Q', 'P', 'T')

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        the_table = ax.table(
            cellText=data,
            colLabels=columns,
            loc='center'
        )

        plt.show()





