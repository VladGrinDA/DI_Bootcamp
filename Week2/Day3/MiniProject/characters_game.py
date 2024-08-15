

import faker
import random



class Character:
    _available_moves = ['basic_attack']
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


class Interface:
    @staticmethod
    def display_menu(options):
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
    
    @staticmethod
    def get_user_choice(max_choice):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_choice}")
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def display_battle_status(player, opponent):
        print(f"\n{player.name}: Life - {player.life}, Attack - {player.attack}")
        print(f"{opponent.name}: Life - {opponent.life}, Attack - {opponent.attack}\n")


class HumanPlayer:
    def __init__(self, character):
        self.character = character

    def choose_action(self):
        print(f"\n{self.character.name}'s turn:")
        Interface.display_menu(self.character._available_moves)
        choice = Interface.get_user_choice(len(self.character._available_moves))
        return self.character._available_moves[choice - 1]


class PCPlayer:
    def __init__(self, character):
        self.character = character

    def choose_action(self):
        return random.choice(self.character._available_moves)


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_battle(self):
        print(f"Battle starts between {self.player1.character.name} and {self.player2.character.name}!")
        
        while self.player1.character.life > 0 and self.player2.character.life > 0:
            Interface.display_battle_status(self.player1.character, self.player2.character)
            
            # Player 1's turn
            action = self.player1.choose_action(self.player2.character)
            self.perform_action(self.player1.character, self.player2.character, action)
            
            if self.player2.character.life <= 0:
                break
            
            # Player 2's turn
            action = self.player2.choose_action(self.player1.character)
            self.perform_action(self.player2.character, self.player1.character, action)
        
        self.announce_winner()

    def perform_action(self, attacker, defender, action):
        if action == 'basic_attack':
            attacker.basic_attack(defender)
        elif hasattr(attacker, action):
            if action in ['meditate', 'animal_help', 'train', 'summon']:
                getattr(attacker, action)()
            else:
                getattr(attacker, action)(defender)
        else:
            print(f"Invalid action: {action}")

    def announce_winner(self):
        if self.player1.character.life <= 0:
            winner = self.player2.character.name
            loser = self.player1.character.name
        else:
            winner = self.player1.character.name
            loser = self.player2.character.name
        
        print(f"\nBattle over! {winner} defeats {loser}!")


def choose_player_type(player_number):
    print(f"\nChoose player {player_number} type:")
    Interface.display_menu(["Human", "PC"])
    choice = Interface.get_user_choice(2)
    return "Human" if choice == 1 else "PC"

def create_player(player_type, player_number):
    if player_type == "Human":
        print(f"\nPlayer {player_number}, choose your character:")
        Interface.display_menu(Character._available_chars)
        char_choice = Interface.get_user_choice(len(Character._available_chars))
        char_class = globals()[Character._available_chars[char_choice - 1]]
        
        player_name = input(f"Enter Player {player_number}'s character name: ")
        character = char_class(player_name)
        return HumanPlayer(character)
    else:
        fake = faker.Faker()
        pc_char_class = globals()[random.choice(Character._available_chars)]
        pc_character = pc_char_class(fake.name())
        return PCPlayer(pc_character)

def main():
    print("Welcome to the Battle!")
    
    # Player 1 selection
    player1_type = choose_player_type(1)
    player1 = create_player(player1_type, 1)
    
    # Player 2 selection
    player2_type = choose_player_type(2)
    player2 = create_player(player2_type, 2)
    
    # Start the battle
    battle = Battle(player1, player2)
    battle.start_battle()

    # Ask if the players want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()