x = int(input('Enter the Number: ')) 
divisors_sum = 0

for num in range(1, x // 2 + 1):
    if x % num == 0:
        divisors_sum += num

if divisors_sum == x:
    print(True)
else:
    print(False)