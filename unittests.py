import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee("Vesa", "Kuoppala", 10.0)

    def tearDown(self):
        None

    def test_too_many_hours_raises_an_error(self):
        with self.assertRaises(ValueError):
            self.emp1.payment(200)

    def test_double_time_hours_give_proper_payment(self):
        self.assertEqual(1500.00, self.emp1.payment(100))

    def test_time_and_half_hours_give_proper_payment(self):
        self.assertEqual(550.00, self.emp1.payment(50))

    def test_regular_time_hours_give_proper_payment(self):
        self.assertEqual(200.00, self.emp1.payment(20))

    def test_negative_hours_raises_an_error(self):
        with self.assertRaises(ValueError):
            self.emp1.payment(-10)

