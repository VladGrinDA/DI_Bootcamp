print('Exercise 1')

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __operations_handler(method):
        def wrapper(self, other):
            if isinstance(other, Currency):
                if self.currency != other.currency:
                    raise TypeError(f"Cannot use {method.__name__} with currency {self.currency} and {other.currency}")
                return method(self, other.amount)
            else:
                return method(self, other)
        return wrapper

    def __str__(self) -> str:
        return f"{str(self.amount)} {self.currency}"
    
    def __repr__(self) -> str:
        return str(self)

    @__operations_handler
    def __add__(self, other):
        return self.amount + other
    
    @__operations_handler
    def __sub__(self, other):
        return self.amount - other
    
    def __int__(self):
        return int(self.amount)
    
    def __iadd__(self, other):
        self.amount = self.__add__(other)
        return self
    
    def __isub__(self, other):
        self.amount = self.__sub__(other)
        return self
    
    # def __neg__(self):
    #     return - self.amount


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += c2
print(c1)

try:
    c1 + c3
except TypeError as e:
    print(e)

try:
    c1 += c3
except TypeError as e:
    print(e)

print('\n\nExercise 2')

from func import add_print

add_print(5, 6)

print('\n\nExercise 3')

import string
import random

def random_string(n):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))


print(random_string(5))


print('\n\nExercise 4')

import datetime 

def current_date():
    print(datetime.date.today())


current_date()


print('\n\nExercise 5')

def time_until_jan_1():
    now = datetime.datetime.now()
    print(now)
    td = datetime.datetime(now.year + 1, 1, 1) - now
    print(f"The 1st of January is in {td.days} days and {td.seconds // 3600}:{(td.seconds // 60) % 60}:{td.seconds % 60} hours")


time_until_jan_1()

print('\n\nExercise 6')

def minutes_lived():
    bday, bmonth, byear = map(int, input('Enter your birth date in a format dd mm yyyy ').split())
    minutes_lived = (datetime.datetime.now() - datetime.datetime(byear, bmonth, bday)).seconds // 60
    print(f"You have lived {minutes_lived} minutes")

minutes_lived()


print('\n\nExercise 7')

from faker import Faker

faker = Faker('it_IT')

def add_users(users, n):
    global faker
    for _ in range(n):
        users.append({
            'name': faker.name(),
            'address': faker.address(),
            'language_code': faker.language_code()
        })


users = []
add_users(users, 5) # add 5 users

print(users)


