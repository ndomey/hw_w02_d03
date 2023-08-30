
class Pub:
    def __init__(self, name, till, drinks):

        self.name = name
        self.till = till
        self.drinks = drinks


    def pay_in_till(self, drink):
        self.till += drink


    def check_age(self, age):

        if age < 18:
            print("Sorry, I cannot sell you alcohol!")