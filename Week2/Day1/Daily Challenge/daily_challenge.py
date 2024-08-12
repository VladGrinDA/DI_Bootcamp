class Farm:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount
    

    def get_info(self):
        animal_count_str = '\n'.join([f'{animal_name}: {count}' for animal_name, count in self.animals.items()])
        info_str = f"{self.owner}'s farm\n\n" \
            f'{animal_count_str}\n\n' \
            f'    E-I-E-I-0!'
        return info_str
    

    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_list = [animal + 's' if self.animals[animal] > 1 else animal for animal in self.get_animal_types()]
        animal_list_str = ', '.join(animal_list[:-1]) + (f' and ' if len(animal_list) > 1 else '') + animal_list[-1]
        return f"{self.owner}'s farm has {animal_list_str}"
    

macdonald = Farm("McDonald")

macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('chicken')

print(macdonald.get_info())

print(macdonald.get_short_info())