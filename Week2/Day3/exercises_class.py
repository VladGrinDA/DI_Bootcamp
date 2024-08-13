class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self._b = 1
        self.y = y

    @staticmethod
    def add(x, y):
        return x + y
    
    @property
    def x(self):
        return self.__x
    

new_class = MyClass(1, 2)
print(new_class.add(10, 20))

print(new_class._b)
print(new_class.__x)


print('Exercise BankAccount')

# 1. *Class Attributes and Methods*:
#    - The class should keep track of the total number of bank accounts created and maintain a list of all accounts.
#    - Implement a class method to find an account by its account number.
#    - Implement a class method to summarize total balances across all accounts.
# 2. *Instance Attributes and Methods*:
#    - Use a @property to manage access to the account balance.
#    - Use a @property and @setter to handle and validate the account type.
#    - Include a transaction history that logs deposits and withdrawals.
#    - Implement a method to calculate and add interest to the account balance (specific to savings accounts).
#    - Implement methods for depositing and withdrawing money, with validation checks.

# Implementation Details
# 1. *Class Attributes*:
#    - __total_accounts: Tracks the total number of bank accounts created.
#    - __all_accounts: A list that stores references to all BankAccount instances.
#    - interest_rate: A class attribute to define the default interest rate for savings accounts.
# 2. *Class Methods*:
#    - get_total_accounts(cls): Returns the total number of accounts.
#    - find_account_by_number(cls, account_number): Finds and returns an account by its account number.
#    - total_balances(cls): Returns the sum of balances across all accounts.
# 3. *Properties*:
#    - balance: Provides access to the account balance.
#    - account_type: Manages the type of account with validation logic.
#    - transaction_history: A list that logs all transactions (deposits and withdrawals).
# 4. *Methods*:
#    - deposit(amount): Adds money to the account and logs the transaction.
#    - withdraw(amount): Withdraws money, ensuring the balance doesn’t go negative, and logs the transaction.
#    - apply_interest(): Applies interest to savings accounts.
# Tasks to Complete
# 1. *Create the BankAccount class* with the provided class and instance attributes.
# 2. *Implement class methods* to manage and interact with the accounts collectively.
# 3. *Implement the @property and @setter* for the account balance and account type.
# 4. *Track transaction history* within each account.
# 5. *Test your class* by creating multiple accounts, performing various transactions, and applying interest.

import datetime

class BankAccount:
    __account_number_idx = 0
    __all_accounts = []
    interest_rate = 0

    def __init__(self, account_type, initial_balance=0.) -> None:
        self.__balance = initial_balance
        self.__account_type = account_type
        self.transaction_history = []

        BankAccount.__all_accounts.append(self)
        BankAccount.__account_number_idx += 1
        self.account_number = BankAccount.__account_number_idx


    @classmethod
    def get_total_accounts(cls):
        return len(cls.__all_accounts)
    
    @classmethod
    def find_account_by_number(cls, account_number):
        for account in cls.__all_accounts:
            if account.number == account_number:
                return account

    @classmethod
    def total_balances(cls):
        return sum([account.balance for account in cls.__all_accounts])

    @staticmethod
    def validate_account_type(account_type):
        valid_types = ['savings', 'checking']
        if account_type not in valid_types:
            raise Exception(f"Not a valid account type ({valid_types})")
    
    @property
    def balance(self):
        return self.__balance

    @property
    def account_type(self):
        return self.__account_type
    
    @account_type.setter
    def account_type(self, account_type):
        self.validate_account_type(account_type)
        self.__account_type = account_type
    
    def __log_transaction(self, operation, amount, **kwargs):
        self.transaction_history.append({'operation': operation, 'amount': amount, 'timestamp': datetime.now(), **kwargs})

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount should be positive")
            return
        self.balance += amount
        self.__log_transaction('deposit', amount)
        print(f"{amount} deposited. New balance is {self.balace}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return 
        self.balance -= amount
        self.__log_transaction('withdrawal', amount)
        print(f"{amount} withdrawn. New balance is {self.balance}")

    
    def apply_interest(self):
        if self.account_type == 'savings':
            interest = self.balance * (BankAccount.interest_rate/100)
            self.balance += interest
            self.__log_transaction('interest', interest, 'interest_rate': BankAccount.interest_rate)
            print(f"{interest} interest applied. New balance: {self.balance}")
        else:
            print(f"Accounts of type {self.account_number} does not support interest")
