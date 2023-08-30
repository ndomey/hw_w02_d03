import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):

        self.food_1 = Food("Burger", 10, 1)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food_1.name)

