# Exercise 9 : Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

input_height = int(input('Pleas input your height in centimeters: '))

if input_height > 145:
    print('Congrats! You are tall enought to ride!')
else:
    print('Sorry! You need to grow a bit')