print('Challenge 1')

string = 'without,hello,bag,world'

result = ','.join(sorted(string.split(',')))

print(result)

print('\n' + 10 * '-')
print('Challenge 2')

sentence = "Margaret's toy is a pretty doll."

def longest_word(sentence):
    max_len = 0
    longest_word = ''
    for word in sentence.split():
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    return longest_word 

print(longest_word(sentence))