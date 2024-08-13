import random


class Cell:
    def __init__(self, is_alive=0):
        self.is_alive = is_alive

    def __str__(self):
        return "█" if self.is_alive else " "


class Board:
    def __init__(self, size_x, size_y):
        self.board = [[Cell() for _ in range(size_x)] for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y


class GOL:
    def __init__(self) -> None:
        self.board = None
    
    def init_board(self, board):
        if not isinstance(board, Board):
            raise TypeError("board must be an instance of Board")
        self.board = board

    def init_random(self, size):
        self.init_board([[Cell(random.randint(0, 1)) for _ in range(size)] for _ in range(size)])

    def print_board(self):
        for row in self.board:
            print("".join([str(cell) for cell in row]))

    def next_state(self):
        new_state = []

        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                adjacent_cells = []
