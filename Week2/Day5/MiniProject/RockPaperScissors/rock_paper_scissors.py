from collections import defaultdict
from game import Game

def display_options(menu_options):
    print("\nMenu:")
    for option, description in menu_options.items():
        print(f"({option}) {description}")

def get_user_menu_choice(menu_options):
    display_options(menu_options)
    return input()

def print_result(results):
    print(
        "\nGame Results: ",
        f"You won {results['win']} times",
        f"You lost {results['loss']} times",
        f"You drew {results['draw']} times",
        sep='\n'
    )

def main():
    results = defaultdict(int)
    menu_options = {
        'p': 'Play new game',
        's': 'Show scores',
        'e': 'Exit'
    }
    while True:
        user_choice = get_user_menu_choice(menu_options)
        if user_choice == 'e':
            break
        elif user_choice == 'p':
            game = Game()
            game_result = game.play()
            results[game_result] += 1
        elif user_choice == 's':
            print_result(results)
        else:
            print("Invalid choice. Please choose again.")
    print_result(results)
    print('Thank you for playing!')

if __name__ == '__main__':
    main()
