import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("wine", 4.50, 5, 10)
        self.drink2 = Drink("beer", 3.50, 5, 20)
        self.customer_1 = Customer("Frodo", 10.00, 24, 5)
        self.customer_2 = Customer("Pippin", 20.00, 17, 0)
        self.customer_3 = Customer("Samwise", 15.00, 18, 40)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_add_drink(self):
        self.pub.add_drink(self.drink1)
        self.assertEqual(1, self.pub.drink_count())

    def test_can_serve_drink(self):
        self.pub.serve_drink(self.drink1, self.customer_1)
        self.assertEqual(5.50, self.customer_1.wallet)
        self.assertEqual(104.50, self.pub.till)
    
    def test_cannot_serve_drink__not_old_enough(self):
        self.pub.serve_drink(self.drink1, self.customer_2)
        self.assertEqual(20.00, self.customer_2.wallet)
        self.assertEqual(100.00, self.pub.till)

    def test_cannot_serve_drink__too_drunk(self):
        self.pub.serve_drink(self.drink1, self.customer_3)
        self.assertEqual(15.00, self.customer_3.wallet)
        self.assertEqual(100.00, self.pub.till)

    def test_customer_is_old_enough(self):
        self.assertEqual(True, self.pub.customer_is_old_enough(self.customer_1))
    
    def test_customer_is_not_old_enough(self):
        self.assertEqual(False, self.pub.customer_is_old_enough(self.customer_2))
    
    def test_customer_drunkenness__not_too_drunk(self):
        self.assertEqual(False, self.pub.customer_is_too_drunk(self.customer_1))
    
    def test_customer_drunkenness__too_drunk(self):
        self.assertEqual(True, self.pub.customer_is_too_drunk(self.customer_3))
    
    def test_increase_stock_level_of_drink(self):
        self.pub.add_drink(self.drink1)
        self.pub.increase_stock_level(self.drink1, 1)
        self.assertEqual(11, self.drink1.stock_level)

    


