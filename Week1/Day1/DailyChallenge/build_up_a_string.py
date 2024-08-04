# Daily challenge: Build up a string
# Sample 10 character string: qwertyuiop

import random

input_string = input('Please input 10 character long string: ')

if len(input_string) > 10:
    print('string not long enought')
elif len(input_string) < 10:
    print('string too long')
else:
    print('perfect string')

    print(f'The first character is {input_string[0]}. The last character is {input_string[-1]}')

    for char in input_string:
        print(char, end='')


    # Bonus
    print()
    input_string_shuffeled = list(input_string)
    random.shuffle(input_string_shuffeled)

    for char in ''.join(input_string_shuffeled):
        print(char, end='')

