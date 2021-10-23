import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("burger", 7.00, 5)


    def test_food_has_name(self):
        self.assertEqual("burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(7.00, self.food.price)
    
    def test_food_has_rejuvination_level(self):
        self.assertEqual(5, self.food.rejuvination_level)
