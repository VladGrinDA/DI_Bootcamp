#1
print(10 * '-' + '\n', 'Exercise 1')

from datetime import date

def get_age(year, month, day):
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    age = current_year - year
    if current_month < month and current_day < day:
        age -= 1
    
    return age


def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    
    age = get_age(year, month, day)
    
    if gender == 'm':
        return age >= 67
    elif gender == 'f':
        return age >= 62
    else:
        return False


gender = input("Please enter your gender (m/f): ").lower()
date_of_birth = input("Please enter your date of birth (yyyy/mm/dd): ")

if can_retire(gender, date_of_birth):
    print("You can retire.")
else:
    print("You cannot retire yet.")


#2
print(10 * '-' + '\n', 'Exercise 2')

def four_sum(x):
    result = 0
    x = str(x)
    x_add = ''
    for _ in range(4):
        x_add += x
        result += int(x_add)
    
    return result

print(four_sum(3))

#3
print(10 * '-' + '\n', 'Exercise 3')

import random
from functools import reduce

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    cnt = 0
    while True:
        cnt += 1
        if throw_dice() == throw_dice():
            return cnt
     

def main(num_throws=100):
    throws_result = [throw_until_doubles() for i in range(num_throws)]

    total_throws = reduce(lambda x, y: x + y, throws_result)
    avg_throws = total_throws / len(throws_result)

    print('Total throws:', total_throws)
    print('Average throws:', avg_throws)


main()