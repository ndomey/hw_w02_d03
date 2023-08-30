class Customer:
    def __init__(self, name, wallet):

        self.name = name
        self.wallet = wallet


    def buying(self, cost):
        self.wallet -= cost