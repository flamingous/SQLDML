  
class Account:
    def __init__(self, account_number, account_balance, account_holder):
       
        self.account_number = account_number
        self.account_balance = float(account_balance)
        self.account_holder = account_holder
    def __str__(self):
        return f"Your account number: {self.account_number}\nYour account balance is: {self.account_balance}\nAnd the account holder is: {self.account_holder}"

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount

    def check_balance(self):
        return self.account_balance
    
account1 = Account(8169625308, 10000, "Adaeze Margaret")
print(account1)
