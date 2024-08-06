# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = input('Please input any word: ')
result = {}

for i, char in enumerate(word):
    if char in result:
        result[char].append(i)
    else:
        result[char] = [i]

print('Result: ', result)