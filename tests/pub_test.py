import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):

        self.pub = Pub("Captain's bar", 500)


    def test_pub_has_name(self):
        self.assertEqual("Captain's bar", self.pub.name)


    def test_pub_till(self):
        self.assertEqual(500, self.pub.till)
