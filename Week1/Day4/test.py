matrix_str = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

def f1():
    print('f1')
    return True

def f2():
    print('f2')
    return True

if f1() or f2():
    print('test or')


x = 5

y = x

x = 10

print(y)