# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {3, 7, 11, 19, 27}

my_fav_numbers.add(1)
my_fav_numbers.add(2)

my_fav_numbers.remove(27)

friend_fav_numbers = {5, 9, 11, 16, 19}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print('my_fav_numbers', my_fav_numbers)
print('friend_fav_numbers', friend_fav_numbers)
print('our_fav_numbers', our_fav_numbers)
