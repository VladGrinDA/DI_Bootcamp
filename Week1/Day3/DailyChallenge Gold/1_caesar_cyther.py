# text = input('Input text: ').lower()
# shift = int(input('Input shift: '))

text = 'abc zfssd'
shift = 3
enc_text = ''
a_ord = ord('a')
alph_len = 26

for char in text:
    if char in ' !.?':
        enc_text += char
    else:
        enc_text += chr(a_ord + (ord(char) + shift - a_ord) % alph_len)

print('Encoded text: ', enc_text)
