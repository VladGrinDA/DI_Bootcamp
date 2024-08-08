#1
print(10 * '-' + '\n', 'Exercise 1')

def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

#2
print(10 * '-' + '\n', 'Exercise 2')

to_morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

from_morse = {morse: eng for eng, morse in to_morse.items()}

def eng_to_morse(string):
    global to_morse
    return '/'.join(map(lambda x: ' '.join([to_morse.get(char, '') for char in x.lower()]), string.split()))


def morse_to_eng(string):
    return ' '.join(map(lambda x: ''.join([from_morse.get(mchar, '') for mchar in x.split()]), string.split('/')))



eng_string = 'ab 1 23'
morse_string = eng_to_morse(eng_string)

print('The original string is:', eng_string)
print('The morse encoded version:', morse_string)
print('From morse back to english:', morse_to_eng(morse_string))


#3
print(10 * '-' + '\n', 'Exercise 3')

def box_printer(*args):
    length_longest = max(len(x) for x in args)

    print('*' * (length_longest + 4))
    for word in args:
        print('* ' + word + ' ' * (length_longest - len(word)) + ' *')
    print('*' * (length_longest + 4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

#4
print(10 * '-' + '\n', 'Exercise 4')

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)