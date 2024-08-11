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
