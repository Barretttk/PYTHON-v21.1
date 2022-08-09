

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

    def transfer_money(self, amount):
        self.balance += self.User(amount)
        return self


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



user1 = User("tim","tb@gmail.com")
print(user1.name)
user1.make_deposite(1000)
print(user1.account.balance)
user1.make_withdrawal(200)
print(user1.account.balance)
print("*"*80)
#========================================

user2 = User("James","JB@gmail.com")
print(user2.name)
user2.make_deposite(500)
print(user1.account.balance)
print("*"*80)
#========================================
user3 = User("Mike","ML@gmail.com")
print(user3.name)
user3.make_deposite(800)
print(user1.account.balance)
print("*"*80)