class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

# Example Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()
