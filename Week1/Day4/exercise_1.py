def calculation(a, b):
    return a + b, a - b

res = calculation(40, 10)
print(res)


wizards = ['Harry', 'Ron', 'Hermione']

def choose_hat():
    global wizards
    for name in wizards:
        name += 'sdfsd'


choose_hat()
print(wizards)

name = 'Vlad'

def change_name():
    # global name
    name = 'Vlad1'
    return name

print(change_name())
print(name)