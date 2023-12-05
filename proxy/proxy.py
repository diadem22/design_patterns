class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. Current balance: ${self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self._balance}")
        else:
            print("Insufficient funds")

class BankAccountProxy:
    def __init__(self, account):
        self._account = account

    def deposit(self, amount):
        if amount > 0:
            self._account.deposit(amount)
        else:
            print("Deposit amount should be greater than zero")

    def withdraw(self, amount):
        if amount > 0:
            self._account.withdraw(amount)
        else:
            print("Withdrawal amount should be greater than zero")

real_account = BankAccount(100)
proxy_account = BankAccountProxy(real_account)

proxy_account.deposit(50) 
proxy_account.withdraw(30)  
proxy_account.withdraw(200) 
proxy_account.deposit(-20)  
