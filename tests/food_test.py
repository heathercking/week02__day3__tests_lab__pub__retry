import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def SetUp(self):
        self.food = Food("burger", 7.00, 5)
