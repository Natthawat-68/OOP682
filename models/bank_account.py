class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def __eq__(self, other):
        return self.balance == other.balance
        
    def __div__(self, other): 
        if isinstance(other, (int, float)):
            new_balance = self.balance / other
            return BankAccount(new_balance)
        return None
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_balance = self.balance * other
            return BankAccount(new_balance)
        return None
        
    def __sub__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance - other.balance
            new_account = BankAccount(new_balance)
            return new_account
        return None
    
    def __add__(self, other):
        new_balance = self.balance + other.balance
        new_account = BankAccount(new_balance)
        return new_account
        
    def __str__(self):
        return f"BankAccount Balance: {(self.balance):,.2f}"

