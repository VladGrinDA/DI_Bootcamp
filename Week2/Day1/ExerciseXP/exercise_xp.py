print('Exercise 1')

import random

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def __repr__(self):
        return f'{self.name} {self.age}'

def find_oldest_cat(cat_list):
    oldest_cat = cat_list[0]
    for cat in cat_list[1:]:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

cat_names = ['Whiskers', 'Luna', 'Jasper']
cats = [Cat(name, random.randint(1, 12)) for name in cat_names]

oldest_cat = find_oldest_cat(cats)

print('All cats: ', cats)
print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')


print('\n', 10 * '-')
print('Exercise 2')

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')

davids_dog = Dog('Rex', 50)
print(f'Details of {davids_dog.name}: Height: {davids_dog.height}cm')
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f'Details of {sarahs_dog.name}: Height: {sarahs_dog.height}cm')
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is bigger than {sarahs_dog.name}')
else:
    print(f'{sarahs_dog.name} is bigger than {davids_dog.name}')


print('\n', 10 * '-')
print('Exercise 3')


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There's a lady who's sure",
                "all that glitters is gold",
                "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()


print('\n', 10 * '-')
print('Exercise 4')

# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self, name, animals=None):
        self.animals = set() if animals is None else animals
        self.name = ''

    def add_animal(self, animal):
        self.animals.add(animal)

    def get_animals(self):
        print(', '.join(self.animals))

    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)

    def sort_animals(self):
        curr_char = ''
        idx = 0
        animals_sorted = {}
        for animal in sorted(self.animals):
            if animal[0] != curr_char:
                idx += 1
                animals_sorted[idx] = [animal]
                curr_char = animal[0]
            else:
                animals_sorted[idx].append(animal)
        return animals_sorted

    def get_groups(self):
        print(self.sort_animals())


ramat_gan_safari = Zoo('Ramat Gan Safari')

ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Zebra')
ramat_gan_safari.add_animal('Lion')
ramat_gan_safari.add_animal('Elephant')
ramat_gan_safari.add_animal('Zebra')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Elephant')
ramat_gan_safari.add_animal('Kangaroo')
ramat_gan_safari.add_animal('Kangaroo')

print('Added some animals')
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal('Lion')
ramat_gan_safari.sell_animal('Zebra')

print('Sold some animals')
ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()


