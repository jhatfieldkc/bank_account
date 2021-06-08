class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self,):
        print(f"User: {self.name},", f"Balance: ${self.account_balance}")

    # def transfer_money(self, other_user, amount):
    #     # self.account_balance-= amount
    #     other_user.name = self.name
    #     self.display_user_balance
    #     # print(other_user, amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jeremy=User("Jeremy Hatfield", "ceo@world.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawl(100)
guido.display_user_balance()


monty.make_deposit(50)
monty.make_deposit(50)
monty.make_withdrawl(100)
monty.make_withdrawl(100)
monty.display_user_balance()

jeremy.make_deposit(150000000000)
jeremy.make_withdrawl(100)
jeremy.make_withdrawl(1000)
jeremy.make_withdrawl(10000)
jeremy.display_user_balance()

# jeremy.transfer_money(guido, 100)