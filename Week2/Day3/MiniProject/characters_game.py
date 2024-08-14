
# Description
# Create a class called Character with the following attributes and methods:
# attribute name
# attribute life – starts with a default value of 20
# attribute attack – the base attack of a character (integer) will be a default of 10
# method basic_attack() - accepts another Character instance as a parameter. Your character will <attack> the other
#  character so his <life> points should drop.


# Instructions
# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)



# Druid:
# meditate() - increases life by 10, decrease attack by 2
# animal_help()- increases attack by 5
# fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other character’s life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

import faker
import random

class Character:
    _available_moves = ['basick_attack']
    _available_chars = []
                       
    def __init__(self, name, life=20, attack=10) -> None:
        self.name = name
        self.__life = life
        self.__attack = attack

    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self, new_life):
        life_diff = new_life - self.__life
        if life_diff > 0:
            print(f"{self.name} gained {life_diff} life.")
        else:
            print(f"{self.name} lost {abs(life_diff)} life.")

        self.__life = max(0, new_life)
        print(f'Current life: {self.__life}')

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, new_attack):
        attack_diff = new_attack - self.__attack
        if attack_diff > 0:
            print(f"{self.name} gained {attack_diff} attack.")
        else:
            print(f"{self.name} lost {abs(attack_diff)} attack.")
        self.__attack = max(0, new_attack)
        print(f'Current attack: {self.__attack}')


    def basic_attack(self, other_char):
        print(f"{self.name} does basic attack ({self.attack}) on {other_char.name}.")
        other_char.life -= self.attack


class Druid(Character):
    __default_catch_phrase = "Rooted in Fury, Branching into Legend!"
    __med_life_inc = 10
    __med_att_dec = -2
    __anim_att_inc = 5
    _available_moves = Character._available_moves + ['meditate', 'animal_help', 'fight']
    Character._available_chars.append('Druid')

    def __init__(self, name, life=20, attack=10, catch_phrase=None) -> None:
        super().__init__(name, life, attack)
        self.catch_phrase = Druid.__default_catch_phrase if catch_phrase else catch_phrase
    
    def use_catch_phrase(self):
        print(f"{self.name} says: {self.catch_phrase}")

    def meditate(self):
        print(f"{self.name} meditated.")
        self.life += Druid.__med_life_inc
        self.attack += Druid.__med_att_dec

    def animal_help(self):
        print(f"{self.name} used animal help.")
        self.attack += Druid.__anim_att_inc

    def fight(self, other_char):
        damage = 0.75 * self.life + 0.75 * self.attack
        print(f"{self.name} fights {other_char.name} with {damage} damage.")
        other_char.life -= damage


# Warrior:
# brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
# train() - increases both your attack and life points by 2.
# roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.

class Warrior(Character):
    __default_catch_phrase = "Battle Forged, Honor Tempered"
    __train_att_inc = 2
    __train_life_inc = 2
    __roar_att_dec = -3
    _available_moves = Character._available_moves + ['brawl', 'train', 'roar']
    Character._available_chars.append('Warrior')

    def __init__(self, name, life=20, attack=10) -> None:
        super().__init__(name, life, attack)

    def brawl(self, other_char):
        print(f"{self.name} brawls {other_char.name}.")
        other_char.life -= 2 * self.attack
        self.attack += 0.5 * self.attack
    
    def train(self):
        print(f"{self.name} trains.")
        self.attack += Warrior.__train_att_inc
        self.life += Warrior.__train_life_inc

    def roar(self, other_char):
        print(f"{self.name} roars on {other_char.name}.")
        other_char.attack += Warrior.__roar_att_dec



# Mage:
# curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
# summon() - increases attack attribute by 3 points.
# cast_spell() - accepts another Character instance as a parameter and subtracts attack/
# life to the other character’s life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).


class Mage(Character):
    __default_catch_phrase = "A Spark of Genius, a Blast of Magic"
    __curse_att_dec = -2
    __summon_att_inc = 3
    _available_moves = Character._available_moves + ['curse', 'summon', 'cast_spell']
    Character._available_chars.append('Mage')

    def __init__(self, name, life=20, attack=10) -> None:
        super().__init__(name, life, attack)

    def curse(self, other_char):
        print(f"{self.name} curses {other_char.name}.")
        other_char.attack += Mage.__curse_att_dec

    def summon(self):
        print(f"{self.name} summoned.")
        self.attack += Mage.__summon_att_inc

    def cast_spell(self, other_char):
        print(f"{self.name} cast spell on {other_char.name}.")
        damage = self.attack / self.life
        other_char.life -= self.attack


class Player:
    def __init__(self, name, type, char=None) -> None:
        self.name = name
        self.type = type
        self.char = char

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.type}, {self.char})"
    
    def choose_char(self):
        raise NotImplementedError
    
    def choose_move(self):
        raise NotImplementedError

class HumanPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name, "human")
    
    def choose_char(self, available_chars):
        while True:
            try:
                chosen_char = int(input())
                if chosen_char in available_chars:
                    self.char = available_chars[chosen_char]()
                    return
            except ValueError:
                pass

            print("Invalid input. Try again.")

    def choose_move(self):
        available_moves = {i: move for i, move in enumerate(self.char._available_moves)}
        print("Choose a move: {}".format([f"{i}: {move}" for i, move in available_moves.items()]))
        while True:
            try:
                chosen_move = int(input())
                if chosen_move in available_moves:
                    return available_moves[chosen_move]
            except ValueError:
                pass

            print("Invalid input. Try again.")
    

class ComputerPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name, "computer")

    def choose_char(self, available_chars):
        self.char = random.choice(available_chars)()


def duel():
    pass