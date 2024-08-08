print(10 * '-' + '\n', 'Challenge 1')

matrix_str = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

matrix = [[char for char in line] for line in matrix_str.split('\n')]
print(matrix)
# symbols = [
#     ['7', 'i', 'i'],
#     ['T', 's', 'x'],
#     ['h', '%', '?'],
#     ['i', ' ', '#'],
#     ['s', 'M', ' '],
#     ['$', 'a', ' '],
#     ['#', 't', '%'],
#     ['^', 'r', '!']
# ]

# as i understood the assigment the maxtrix should look as defined above
# and we should iterate over it column by columns from top to bottom.
# Here is the code to do that
result = []
alpha_group = ''
for i_col in range(len(matrix[0])):
    for i_row in range(len(matrix)):
        if matrix[i_row][i_col].isalpha():
            alpha_group += matrix[i_row][i_col]
        elif len(alpha_group) > 0:
            result.append(alpha_group)
            alpha_group = ''
                   
result = ' '.join(result)
print('The decoded sequence is:', result)