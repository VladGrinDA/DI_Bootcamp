# Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

class Siamese (Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

def test_ex1():
    all_cats = [Bengal('Sara', 5), Chartreux('Felix', 2), Siamese('Misty', 3)]
    sara_pets = Pets(all_cats)
    sara_pets.walk()


# Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __repr__(self) -> str:
        return self.name

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other):
        if self.run_speed() * self.weight > other.run_speed() * other.weight:
            winner = self
        else:
            winner = other
        print(f'The winner is {winner.name}')


def test_ex2():
    max = Dog('Max', 10, 60)
    nala = Dog('Nala', 8, 50)
    fido = Dog('Fido', 12, 70)


    print("Run speed of dogs:")
    print(f'Max run speed is {max.run_speed()}')
    print(f'Nala run speed is {nala.run_speed()}')
    print(f'Fido run speed is {fido.run_speed()}')

    print("Max")
    max.fight(nala)
    max.fight(fido)

    print("\nNala")
    nala.fight(max)
    nala.fight(fido)

    print("\nFido")
    fido.fight(max)
    fido.fight(nala)


print('\n\nExercise 3 is in a different file (exercise_xp_3.py)')

# Exercise 4

class Family:
    def __init__(self, members, last_name) -> None:
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        child = kwargs
        child.update({'is_child': True, 'age': 0})
        print(f"Congrats with a new born {child['name']}!")
        self.members.append(child)

    def get_member(self, name):
        for member in self.members:
            if member['name'] == name:
                return member

    def is_18(self, name):
        return self.get_member(name)['age'] >= 18


    def family_presentation(self):
        print(f'Family {self.last_name}')
        print('\n'.join([', '.join([f'{key.capitalize()}: {value}' for key, value in member.items()]) for member in self.members]))

def test_ex4():
    family_members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
    family = Family(family_members, 'Smith')

    family.born(name='Peter', gender='Male')
    print('Sarah is over 18: ', family.is_18('Sarah'))
    print('Peter is over 18: ', family.is_18('Peter'))
    family.family_presentation()


# Exercise 5

class TheIncredibles(Family):
    def __init__(self, members, last_name) -> None:
        super().__init__(members, last_name)

    def use_power(self, name):
        if not self.is_18(name):
            raise Exception("SHould be over 18 to use a power")
        print(self.get_member(name)['power'])

    def incredible_presentation(self):
        print(f'*Here is our powerful family {self.last_name}*')
        self.family_presentation()
    
    
def test_ex5():
    family_members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]
    incredibles_family = TheIncredibles(family_members, 'The Incredibles')
    incredibles_family.incredible_presentation()
    
    incredibles_family.born(name='Baby Jack', gender='Male', power='Unknown Power')
    incredibles_family.incredible_presentation()

if __name__ == "__main__":
    print('Exercise 1')
    test_ex1()
    print('\n\nExercise 2')
    test_ex2()
    print('\n\nExercise 4')
    test_ex4()
    print('\n\nExercise 5')
    test_ex5()