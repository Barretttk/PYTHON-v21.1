
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.06, balance=0)
    

    def make_deposite(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self


    def display_user_balance(self):
        self.account.balance
        return self

# work in progress
    def transfer_money(self,amount,other_user):
        self.account.deposit(amount) + other_user
        return self
