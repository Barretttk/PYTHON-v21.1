from unicodedata import name


class User:
    def __init__(self, name, email):
        self.name = "Andre"
        self.email = "ADR@hotmail.com"
        self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self, amount):
        self.account.deposit(100)
        # return self
        print(self.account.balance)


    # def withdraw(self, amount):
    #     if amount > self.balance:
    #         print("Insufficient funds: Charging a $5 fee")
    #         self.balance -= 5
    #     elif amount < self.balance:
    #         self.balance -= amount
    #     return self


    # def display_account_info(self):
    #     print(self.balance)
    #     return self

    # def yield_interest(self):
    #     print(self.balance)
    #     print(self.int_rate)
    #     self.balance *= 1+ self.int_rate
    #     print(self.balance)
    #     return self
