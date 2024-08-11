print('Exercise 1')

class Circle:
    pi = 3.1415

    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * self.radius ** 2

    def print_circle(self):
        print(f"The geometrical definition of a circle is: "
              f"{self.radius} is the radius of a circle. "
              f"The perimeter of a circle is {self.perimeter():.3f} "
              f"and the area is {self.area():.3f}.")
        


circle1 = Circle(10)
circle1.print_circle()

circle2 = Circle(1)
circle2.print_circle()

print('\n', 10 * '-')
print('Exercise 2')

import random

class MyList:
    def __init__(self, letters) -> None:
        self.letters = letters 
    
    def reversed(self):
        return self.letters[::-1]
    
    def sorted(self):
        return sorted(self.letters)
    
    def random_numbers(self):
        return [random.randint(0, 9) for _ in self.letters]
    


ml = MyList(['b', 'a', 'c'])
print(ml.letters)
print(ml.reversed())
print(ml.sorted())
print(ml.random_numbers())

print('\n', 10 * '-')
print('Exercise 3')


class MenuManager:
    def __init__(self, menu=None):
        self.menu = menu if menu is not None else []

    def __repr__(self):
        return '\n'.join([f'Name: {item["name"]}, Price: {item["price"]}, Spicy: {item["spice"]}, Contains Gluten: {item["gluten"]}' for item in self.menu])

    def get_item(self, name):
        for dish in self.menu:
            if dish['name'] == name:
                return dish

    def add_item(self, name, price, spice, gluten):
        self.menu.append({'name': name, 'price': price, 'spice': spice, 'gluten': gluten})

    def update_item(self, name, price, spice, gluten):
        dish = self.get_item(name)
        if dish is not None:
            dish.update([('price', price), ('spice', spice), ('gluten', gluten)])

    def remove_item(self, name):
        self.menu = [item for item in self.menu if item['name'] != name]


menu_manager = MenuManager()

menu_manager.add_item('Pizza', 12.99, True, False)
menu_manager.add_item('Pasta', 10.99, False, True)
menu_manager.add_item('Soup', 6.99, False, False)

print('\nMenu:')
print(menu_manager)

print('\nUpdating Pizza:')
menu_manager.update_item('Pizza', 15, True, True)
print(menu_manager)

print('\nRemoving Soup:')
menu_manager.remove_item('Soup')
print(menu_manager)
