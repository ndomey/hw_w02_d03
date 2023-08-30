import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):

        self.drink_1 = Drink("liquor", 3)
        self.drink_2 = Drink("beer", 3)
        self.drink_3 = Drink("wine", 3)

        self.pub = Pub("Captain's bar", 500, [self.drink_1, self.drink_2, self.drink_3])

        self.customer_1 = Customer("BobTheSnob", 100000, 17)


    def test_pub_has_name(self):
        self.assertEqual("Captain's bar", self.pub.name)


    def test_pub_till(self):
        self.assertEqual(500, self.pub.till)


    def test_pay_in_till(self):
        self.pub.pay_in_till(self.drink_2.price)
        self.assertEqual(503, self.pub.till)


    def test_check_age(self):
        self.pub.check_age(self.customer_1.age)
