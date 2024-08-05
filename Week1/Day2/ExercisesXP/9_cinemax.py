# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

family = ["David", "Sarah", "Daniel", "Miriam", "Eli"]
total_tikets_cost = 0

for person in family:
    age = int(input(f'{person}, please enter your age: '))
    
    if age >= 12:
        total_tikets_cost += 15
    elif age >= 3:
        total_tikets_cost += 10

print('The total ticket\'s cost for the family is: ', total_tikets_cost)


teenagers = ["David", "Sarah", "Daniel", "Miriam"]
allowed_to_watch = []

for person in teenagers:
    age = int(input(f'{person}, please enter your age: '))

    if age >= 16 and age <= 21:
        allowed_to_watch.append(person)

print('People from the group that are allowed to watch:', ', '.join(allowed_to_watch))

    