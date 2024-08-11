import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
pair_count = 0
num_count = {}

for num in list_of_numbers:
    residual = target_number - num
    if residual in num_count:
        pair_count += num_count[residual]

    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1


print(pair_count)


# Dictionary to store the frequency of each number
num_dict = {}

# Variable to count the number of pairs
pair_count = 0

# Iterate through each number in the list
for number in list_of_numbers:
    # Calculate the complement number that, when added to the current number, equals the target_number
    complement = target_number - number
    
    # If the complement exists in the dictionary, it means we've found a pair
    if complement in num_dict:
        pair_count += num_dict[complement]
    
    # Add the current number to the dictionary or update its frequency
    if number in num_dict:
        num_dict[number] += 1
    else:
        num_dict[number] = 1

# Print the total number of pairs found
print(f"The number of pairs that sum to {target_number} is: {pair_count}")