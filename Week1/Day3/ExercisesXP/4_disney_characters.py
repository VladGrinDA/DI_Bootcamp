# Exercise 4 : Disney characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i

print('disney_users_A:', disney_users_A)


disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user

print('disney_users_B:', disney_users_B)


disney_users_C = {}
for i, user in enumerate(sorted(users)):
    disney_users_C[user] = i

print('disney_users_C:', disney_users_C)


disney_users_A_i = {}
i = 0
for user in users:
    if 'i' in user.lower():
        disney_users_A_i[user] = i
        i += 1

print('disney_users_A with i:', disney_users_A_i)


disney_users_A_mp = {}
i = 0
for user in users:
    if user[0].lower() in 'mp':
        disney_users_A_mp[user] = i
        i += 1

print('disney_users_A starts with m or p:', disney_users_A_mp)