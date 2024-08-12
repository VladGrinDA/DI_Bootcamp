import random
from exercise_xp import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained) -> None:
        super().__init__(name, age, weight)
        self.trained = trained 
    
    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print(', '.join(map(str, [self, *args])) + 'all play together')
    

    def do_a_trick(self):
        if self.trained:
            tricks = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
            print(f'{self.name} {random.choice(tricks)}')



max = PetDog('Max', 3, 40, False)
nala = PetDog('Nala', 2, 30, False)
coco = PetDog('Coco', 1, 25, True)

max.train()
max.play(nala, coco)
max.do_a_trick()
max.do_a_trick()

nala.do_a_trick()

