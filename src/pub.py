
class Pub:
    def __init__(self, name, till, drinks):

        self.name = name
        self.till = till
        self.drinks = drinks


    def pay_in_till(self, drink):
        self.till += drink