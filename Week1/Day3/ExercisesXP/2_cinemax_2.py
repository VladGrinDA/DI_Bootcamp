# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the 
# provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {}
total_cost = 0

print('Please input name and age of every cinema visitor. Type \'quit\' when you are done!')
while True: 
    name = input('Please enter a name: ')
    if name == 'quit':
        break
    age = int(input('Please input an age: '))

    family[name] = age
    
    if age > 12:
        total_cost += 15
    elif age >= 3:
        total_cost += 10


print('family: ', family)
print('total cost', total_cost)

