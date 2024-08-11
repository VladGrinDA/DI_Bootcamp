print('\n\nExercise 1')

def concatenate_lists(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenate_lists(list1, list2)


print('\n\nExercise 2')

for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)



print('\n\nExercise 3')

def check_index(name, names):
    for i, n in enumerate(names):
        if n == name:
            return i
    return -1

def user_name_index(names):
    name = input('Please enter your name: ')
    name_idx = check_index(name, names)
    if name_idx != -1:
        print('Name index is:', name_idx)
    else:
        print('No such name in the list')


names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name_index(names)


print('\n\nExercise 4')

def greatest_number():
    num1 = int(input('Input the 1st number: '))
    num2 = int(input('Input the 2nd number: '))
    num3 = int(input('Input the 3rd number: '))
    greatest = max(num1, num2, num3)
    print(f'The greatest number is: {greatest}')

greatest_number()


print('\n\nExercise 5')

def letters_in_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter in 'aeiou':
            print(f'{letter} is a vowel')
        else:
            print(f'{letter} is a consonant')

letters_in_alphabet()

print('\n\nExercise 6')

def words_and_letters():
    words = []
    for _ in range(7):
        word = input('Input a word: ')
        words.append(word)
    letter = input('Input a letter: ')
    for word in words:
        for i, w_letter in enumerate(word):
            if letter == w_letter:
                print(f'{letter} is at index {i} in the word {word}')
            else:
                print(f'{letter} is not in the word {word}')

words_and_letters()

print('\n\nExercise 7')

def min_max_sum():
    numbers = [num for num in range(1, 1000001)]
    print(min(numbers), max(numbers))
    print(sum(numbers))

min_max_sum()


print('\n\nExercise 8')

def list_and_tuple():
    numbers = input('Input a sequence of comma-separated numbers: ')
    numbers_list = numbers.split(',')
    numbers_tuple = tuple(numbers_list)
    print(numbers_list)
    print(numbers_tuple)

list_and_tuple()


print('\n\nExercise 9')

import random

def random_number():
    games_won = 0
    games_lost = 0
    while True:
        num = int(input('Input a number from 1 to 9 or 0 to quit: '))
        random_num = random.randint(1, 9)
        if num == 0:
            break
        if num == random_num:
            print('Winner')
            games_won += 1
        else:
            print('Better luck next time')
            games_lost += 1

    print(f'Games won: {games_won}')
    print(f'Games lost: {games_lost}')

num = 2
random_number()
