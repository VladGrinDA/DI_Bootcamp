input_number = int(input('Please input a number between 1 and 100: '))
output_string = ''

if input_number % 3 == 0:
    output_string += 'Fizz'

if input_number % 5 == 0:
    output_string += 'Buzz'

print(output_string)


