import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):

        self.pub = Pub("Captain's bar", 500)

    def pub_has_name(self):

        self.assertEqual("Captains bar", self.pub.name)


    def pub_till(self):

        self.assertEqual(500, self.pub.till)

