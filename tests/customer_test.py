import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):

        self.drink_1 = Drink("Fanta", 3)
        self.drink_2 = Drink("beer", 3)
        self.drink_3 = Drink("wine", 3)

        self.customer = Customer("BobTheSnob", 100000)
        

    def test_clear_my_tab(self):

        self.customer.clear_my_tab(2000)
        self.assertEqual(98000, self.customer.wallet)


    def test_buying(self):

        self.customer.buying(self.drink_1.price)
        self.assertEqual(99997, self.customer.wallet)



