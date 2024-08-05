# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

string_dups = input('Please input any string (preferably with duplicated characters:)): ')
last_char = ''
string_no_dups = ''

for char in string_dups:
    if char != last_char:
        string_no_dups += char
        last_char = char

print(string_no_dups)