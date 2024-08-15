import random


class Game:
    _valid_items = {
        'r': {'r': 'draw', 'p': 'loss', 's': 'win'},
        'p': {'r': 'win', 'p': 'draw', 's': 'loss'},
        's': {'r': 'loss', 'p': 'win', 's': 'draw'}
    }
    _items_alias = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }
    def get_user_item(self):
        selected_item = ''
        while True:
            selected_item = input('Please select (r)ock, (p)aper, or (s)cissors: ').lower()
            if selected_item in self._valid_items:
                break
            print('Invalid choice. Please try again.')

        return selected_item

    def get_computer_item(self):
        return random.choice(list(self._valid_items.keys()))

    def get_game_result(self, user_item, computer_item):
        return self._valid_items[user_item][computer_item]

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f'You selected {self._items_alias[user_item]}. The computer selected {self._items_alias[computer_item]}. Result: {result}.')
        return result