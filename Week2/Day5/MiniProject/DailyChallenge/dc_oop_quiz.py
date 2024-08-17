# Exersize Quizz

# What is a class? 
# A template for creating objects. It defines the attributes and methods that the objects created from it will have.

# What is an instance?
# Instance is an object created from a class.

# What is encapsulation?
# Encapsulation is a way to restrict the direct access to some components of an object

# What is abstraction?
# The process of hiding the implementation details and showing only the essential features of an object.

# What is inheritance?
# The process of creating a new class from an existing class.

# What is multiple inheritance?
# It is the process of creating a new class from more than one existing class.

# What is polymorphism?
# Polymorphism is the ability of an object to take on many forms.

# What is method resolution order or MRO?
# Determines the order in which a method is searched for in a class hierarchy.

from typing import List, Optional
from collections import deque
import random


print('\n\nExercise 2')

class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value} of {self.suit}'
    
class Deck:
    __suites = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    __values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self) -> None:
        self.cards = self.get_full_deck()

    def __len__(self):
        return len(self.cards)
    
    def __repr__(self):
        return repr(self.cards)

    def get_full_deck(self):
        return deque([Card(suit, value) for value in self.__values for suit in self.__suites])
    
    def reset(self):
        self.cards = self.get_full_deck()

    def shuffle(self, reset=False):
        if reset:
            self.reset()
        if len(self) != 52:
            print(f'Deck should have 52 card but currently it has {len(self)}.')

        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


    
def test_deck():
    deck = Deck()
    print(len(deck))
    print(deck)
    print(deck.cards[-1])
    print(deck.deal())
    print(len(deck))
    deck.shuffle()
    deck.shuffle(reset=True)
    print(deck)


if __name__ == '__main__':
    test_deck()