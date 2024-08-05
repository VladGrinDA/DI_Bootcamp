# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

print('All numbers from 1 to 20')
for i in range(1, 21):
    print(i)

print('All numbers from 1 to 20 with even indexes')
for i in range(1, 21):
    if (i - 1) % 2 == 0:
        print(i)