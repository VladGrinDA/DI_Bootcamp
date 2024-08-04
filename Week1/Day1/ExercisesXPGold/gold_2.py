# Exercise 2 : What is the Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

input_month = int(input('Please input a month (1 to 12): '))

if input_month < 1 or input_month > 12:
    print('Invalid month')
elif input_month <= 2 or input_month == 12:
    print('Winter')
elif input_month <= 5:
    print('Spring')
elif input_month <= 8:
    print('Summer')
else:
    print('Autumn')