import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Frodo", 10.00, 24, 5)
        
        
    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_customer_has_drunkenness(self):
        self.assertEqual(5, self.customer.drunkenness)

    def test_customer_can_buy_drink(self):
        drink = Drink("wine", 4.50, 4)
        self.customer.buy_drink(drink)
        self.assertEqual(5.50, self.customer.wallet)
    
    def test_customer_has_age(self):
        self.assertEqual(24, self.customer.age)