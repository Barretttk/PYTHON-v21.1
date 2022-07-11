
class BankAccount: 


    def __init__(self,int_rate = .06,balance = 0):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        elif amount < self.balance:
            self.balance -= amount
        return self


    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        
        print(self.balance)

tim = BankAccount(.02,200)
tim.display_account_info()

corn = BankAccount(.08,0)
corn.deposit(3000).display_account_info()

joseph = BankAccount(.05, 1522)
joseph.deposit(1000).withdraw(500).display_account_info()

miguel = BankAccount()
miguel.display_account_info()

isaac = BankAccount(balance = 20,int_rate=0.09)
isaac.display_account_info().deposit(6000).display_account_info()