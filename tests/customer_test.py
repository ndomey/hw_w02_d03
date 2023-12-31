import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):

        self.drink_1 = Drink("liquor", 3, 3)
        self.drink_2 = Drink("beer", 3, 1)
        self.drink_3 = Drink("wine", 3, 2)

        self.food_1 = Food("Burger", 10, 1)

        self.customer = Customer("BobTheSnob", 100000, 17)


    def test_clear_my_tab(self):

        self.customer.clear_my_tab(2000)
        self.assertEqual(98000, self.customer.wallet)


    def test_buying(self):

        self.customer.buying(self.drink_1.price)
        self.assertEqual(99997, self.customer.wallet)


    def test_getting_drunk(self):

        self.customer.getting_drunk(self.drink_1.alcohol_level)
        self.assertEqual(3, self.customer.drunkenness)


    def test_eating(self):

        self.customer.eating(self.food_1.rejuvenation_level)
        self.assertEqual(-1, self.customer.drunkenness)