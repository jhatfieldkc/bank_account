class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self,):
        print(f"User: {self.name},", f"Balance: ${self.account_balance}")
        return self

    # def transfer_money(self, other_user, amount):
    #     # self.account_balance-= amount
    #     other_user.name = self.name
    #     self.display_user_balance
    #     # print(other_user, amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jeremy=User("Jeremy Hatfield", "ceo@world.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(100).display_user_balance()

monty.make_deposit(500).make_deposit(50).make_withdrawl(100).make_withdrawl(100).display_user_balance()

jeremy.make_deposit(150000000000).make_withdrawl(100).make_withdrawl(1000).make_withdrawl(10000).display_user_balance()

# jeremy.transfer_money(guido, 100)