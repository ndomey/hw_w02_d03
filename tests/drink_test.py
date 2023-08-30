import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):

        self.drink_1 = Drink("liquor", 3, 3)
        self.drink_2 = Drink("beer", 3, 1)
        self.drink_3 = Drink("wine", 3, 2)

    def test_drink_has_name(self):
        self.assertEqual("liquor", self.drink_1.name)