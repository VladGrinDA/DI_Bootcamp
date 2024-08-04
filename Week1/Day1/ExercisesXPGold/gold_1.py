# Exercise 1 : Hello World-I love Python
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

# print('Hello world \n' * 4 + 'I love python\n' * 4)
print('\n'.join(['Hello world'] * 4) + '\n' + '\n'.join(['I love python'] * 4))
