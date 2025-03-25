#meal prices in cents
CHEAP = 250
TASTY = 400



class Card:
    def __init__(self, balance):
        # balance in cents
        self.balance = balance
    
    def eat_cheap(self):
        if self.balance >= CHEAP:
            self.balance -= CHEAP
        
    def eat_tasty(self):
        if self.balance >= TASTY:
            self.balance -= TASTY
    
    def load_money(self, amount):
        if amount < 0:
            return
    
        self.balance += amount

        if self.balance > 15000:
            self.balance = 15000
    
    def balance_in_euros(self):
        return self.balance / 100

    def __str__(self):
        balance_in_euros = round(self.balance / 100, 2)

        return "The card has {:0.2f} euros".format(balance_in_euros)