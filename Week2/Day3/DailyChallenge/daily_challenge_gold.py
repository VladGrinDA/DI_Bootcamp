
persons = [
    ('John', '20', '90'),
    ('Jony', '17', '93'), 
    ('Jony', '17', '91'), 
    ('Json', '21', '85'), 
    ('Tom', '19', '80'),
    ('Json', '18', '85')
]

print(persons)
persons_sorted = sorted(persons, key=lambda x: x[0] + x[1] + x[2])
print(persons_sorted)