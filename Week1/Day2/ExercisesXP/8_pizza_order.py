# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
topping_inp = ''

print('Please enter desirable toppings (2.5 nis each). Enter \'quit\' when you are done')
while True:
    topping_inp = input('Please enter topping name: ')
    if topping_inp == 'quit':
        break
    print(f'We will add {topping_inp} to your delicious pizza!')
    toppings.append(topping_inp)

print(f'Pizza with toppings: {", ".join(toppings)}\n costs {10 + len(toppings) * 2.5}')


