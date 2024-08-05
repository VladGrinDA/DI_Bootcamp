# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input('Please input a number: '))
lenght = int(input('Please enter a lenght: '))

print([number * i for i in range(1, lenght + 1)])