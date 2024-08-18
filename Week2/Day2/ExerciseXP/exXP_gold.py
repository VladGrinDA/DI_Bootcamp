# Exercise 1: Bank Account

import datetime

class BankAccount:

    def __init__(self, username, password, authenticated=False) -> None:
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = authenticated
    
    @staticmethod
    def _check_auth(method):
        def wrapper(self, *args, **kwargs):
            if not self.authenticated:
                raise Exception("Error: You should be authenticated to use this method!")
            return method(self, *args, **kwargs)
        return wrapper

    def __repr__(self):
        return f"BankAccount(username={self.username}, authenticated={self.authenticated})"

    def _validate_credentials(self, username, password):
        return username == self.username and password == self.password

    def authenticate(self, username, password):
        if not self._validate_credentials(username, password):
            raise Exception("Error: Wrong username or password!")
        self.authenticated = True

    @_check_auth
    def check_balance(self):
        print(f"The current balance is: {self.balance}")

    @_check_auth
    def deposit(self, amount):
        if amount < 0:
            raise Exception("Deposit amount should be positive")
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}")
    
    @_check_auth
    def withdraw(self, amount):
        if amount < 0:
            raise Exception("Deposit amount should be positive")
        self.balance -= amount
        print(f"{amount} withdrawn. New balance is {self.balance}")



def test_BA():
    print("\n Testing BankAccount")
    account = BankAccount("Alice", "password")
    try:
        account.authenticate("Alice", "wrong_password") 
    except Exception as e:
        print(e)
    try:
        account.withdraw(10)
    except Exception as e:
        print(e)
    account.authenticate("Alice", "password")    
    try:
        account.withdraw(10)
    except Exception as e:
        print(e)
    account.check_balance()
    account.deposit(100)
    account.withdraw(30)
    try:
        account.withdraw(-10)
    except Exception as e:
        print(e)
    account.check_balance()


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, authenticated=False, minimum_balance=0.) -> None:
        super().__init__(username, password, authenticated)
        self.__minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self.__minimum_balance
    
    # not the best approach because it will be called twice
    # but it shold be better to call withdraw from parent class after checking balance 
    @BankAccount._check_auth 
    def withdraw(self, amount):
        if self.balance - amount < self.__minimum_balance:
            raise Exception("Widthdraw will put the balace lower than the minimum value")
        super().withdraw(amount)
    
def test_MBA():
    print("\n Testing MinimumBalanceAccount")
    account = MinimumBalanceAccount("Alice", "password")
    try:
        account.withdraw(10)
    except Exception as e:
        print(e)
    account.authenticate("Alice", "password")    
    try:
        account.withdraw(10)
    except Exception as e:
        print(e)
    account.check_balance()
    account.deposit(100)
    account.withdraw(30)
    try:
        account.withdraw(-10)
    except Exception as e:
        print(e)
    account.check_balance()


class ATM:
    def __init__(self, account_list, try_limit=None):
        if not self._is_valid_al(account_list):
            raise Exception(f"account_list should be a list of (BankAccount, MinimumBalanceAccount) instances")
        self.__acount_list = account_list

        if not isinstance(try_limit, int) or try_limit <= 0:
            try_limit = 2
            print(f"try_limit should be a positive number (greater than 0), using default value of {try_limit}")

        self.__try_limit = try_limit
        self.current_tries = 0
    
    @staticmethod
    def _is_valid_al(account_list):
        if not isinstance(account_list, list):
            return False
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                return False
        return True
    
    @staticmethod
    def _display_options(menu_options):
        for i, option in enumerate(menu_options):
            print(f'{i + 1}. {option}')
    
    def tries_left(self):
        return self.__try_limit - self.current_tries

    def log_in(self, username, password):
        for account in self.__acount_list:
            try:
                account.authenticate(username, password)
                return account
            except:
                pass
        self.current_tries += 1
    
    def show_account_menu(self, account):
        menu_options = ['deposit', 'withdraw', 'balance', 'exit']
        while True:
            self._display_options(menu_options)
            user_inp = input()
            try:
                if user_inp == '1':
                    amount = int(input('Enter amount to deposit: '))
                    account.deposit(amount)
                elif user_inp == '2':
                    amount = int(input('Enter amount to withdraw: '))
                    account.withdraw(amount)
                elif user_inp == '3':
                    account.check_balance()
                elif user_inp == '4':
                    break
            except Exception as e:
                print(e)

    def show_main_menu(self):
        menu_options = ['Log in', 'Exit']
        while True:
            self._display_options(menu_options)
            user_inp = input()
            if user_inp == '1':
                while True:
                    if self.tries_left() <= 0:
                        print("You've reached the maximum number of tries")
                        exit()

                    username = input('Enter username: ')
                    password = input('Enter password: ')
                    account = self.log_in(username, password)
                    if account is not None:
                        self.show_account_menu(account)
                        break

                    print("Wrong username or password.")
                    print(f"Tries left: {self.tries_left()}")
                break
            elif user_inp == '2':
                exit()

                    
def test_ATM():
    print('\n Testing ATM')
    account_list = [
        BankAccount('alex', '123456'),
        MinimumBalanceAccount('maria', '121212', 1000),
        BankAccount('john', 'qwerty', 10000)
    ]
    atm = ATM(account_list)
    atm.show_main_menu()

if __name__ == '__main__':
    test_BA()
    test_MBA()
    test_ATM()