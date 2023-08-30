class Customer:
    def __init__(self, name, wallet, age):

        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0


    def clear_my_tab(self, amount_owned):

        self.wallet -= amount_owned

    
    def buying(self, drink):

        self.wallet -= drink

    
    def getting_drunk(self, drink):

        self.drunkenness += drink


    def drunk(self, drunkenness):
        
        if drunkenness > 10:
            print("I think you've had enough, have some water!")
            