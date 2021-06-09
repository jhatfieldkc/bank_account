class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance *= (1 + self.int_rate)
        return self

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def add_interest(self):
        self.account.yield_interest()
        return self

    # def transfer_money(self, other_user, amount):
    #     # self.account_balance-= amount
    #     other_user.name = self.name
    #     self.display_user_balance
    #     # print(other_user, amount)

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# User.change_bank_name("Bank of Money")
# print(User.bank_name)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jeremy = User("Jeremy Hatfield", "ceo@world.com")

# guido.account.deposit(100).deposit(200).deposit(50).withdrawal(100).display_account_info()

# guido.make_deposit(100)
# print(guido.account.balance)

monty.make_deposit(500).make_deposit(50).make_withdrawal(100).make_withdrawal(100).display_user_balance()

jeremy.make_deposit(150000000000).make_withdrawal(100).make_withdrawal(1000).make_withdrawal(10000).add_interest().display_user_balance()

