print('\n\nExercise 1')

d_input = input('Please enter a list of D values separated by commas: ')
c = 50 
h = 30
d_list = [int(x) for x in d_input.split(",")]
result_list = [round(((2 * c * x) / h) ** 0.5, 0) for x in d_list]
print(result_list) # 18,22,24

print('\n\nExercise 2')



