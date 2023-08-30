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


    def eating(self, food):

        self.drunkenness -= food