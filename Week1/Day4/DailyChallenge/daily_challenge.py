print(10 * '-' + '\n', 'Challenge 1')


symbols = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# as i understood the assigment the maxtrix should look as defined above
# and we should iterate over it column by columns from top to bottom.
# Here is the code to do that
result = []
alpha_group = ''
for i_col in range(len(symbols[0])):
    for i_row in range(len(symbols)):
        if symbols[i_row][i_col].isalpha():
            alpha_group += symbols[i_row][i_col]
        elif len(alpha_group) > 0:
            result.append(alpha_group)
            alpha_group = ''
                   
result = ' '.join(result)
print('The decoded sequence is:', result)