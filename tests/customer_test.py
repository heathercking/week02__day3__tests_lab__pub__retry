import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

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
        drink = Drink("wine", 4.50, 5, 10)
        self.customer.buy_drink(drink)
        self.assertEqual(5.50, self.customer.wallet)
        self.assertEqual(10, self.customer.drunkenness)
    
    def test_customer_has_age(self):
        self.assertEqual(24, self.customer.age)

    def test_customer_can_buy_food(self):
        food = Food("burger", 7.00, 5)
        self.customer.buy_food(food)
        self.assertEqual(0, self.customer.drunkenness)
        self.assertEqual(3.00, self.customer.wallet)