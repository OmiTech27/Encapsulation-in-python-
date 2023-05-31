class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance                # Protected attribute
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
    
    def get_balance(self):
        return self._balance

# Create an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Perform deposit and withdrawal operations
account.deposit(500)
account.withdraw(200)

# Get the current balance
balance = account.get_balance()
print("Current Balance:", balance)
