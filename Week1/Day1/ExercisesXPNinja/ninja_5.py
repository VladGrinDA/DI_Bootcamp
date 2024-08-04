input_string = ''
longest_sentence = 0
while input_string != '!exit':
    input_string = input(f'Please enter sentence longer than {longest_sentence}'
                         f'that does not contain character \'a\' (!exit to stop): ')
    if 'a' not in input_string.lower():
        if len(input_string) > longest_sentence:
            longest_sentence = len(input_string)
            print(f'Congrats! You\'ve just set the new record - {longest_sentence}')
    else:
        print('The sentence contains character \'a\'')