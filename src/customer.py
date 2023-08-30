class Customer:
    def __init__(self, name, wallet, age):

        self.name = name
        self.wallet = wallet
        self.age = age


    def clear_my_tab(self, amount_owned):

        self.wallet -= amount_owned

    
    def buying(self, drink):

        self.wallet -= drink