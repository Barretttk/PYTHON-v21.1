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
        print(self.int_rate)
        self.balance *= 1+ self.int_rate
        print(self.balance)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.06, balance=0)
    

tim = User('tim', 'Tb@gmail.com')
tim.account.deposit(5000).display_account_info()
tim.account.withdraw(550).display_account_info()