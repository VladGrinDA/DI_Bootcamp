import random
from typing import List

def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    border = 17 * '*'
    row_format = '*   {} | {} | {}   *'
    row_split = '*  ' + '+'.join(3 * ['---']) + '  *'
    
    print(
        border,
        row_format.format(*board[0]),
        row_split,
        row_format.format(*board[1]),
        row_split,
        row_format.format(*board[2]),
        border,
        sep='\n'
    )

def is_valid_turn(board, row, col):
    return 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' '

def get_user_input(message):
    print(message, end='')
    try:
        return int(input()) - 1
    except ValueError:
        print('Please enter integer')
        return get_user_input(message)

def player_turn(board, player):
    print(f'Player {player}\'s turn...')
    while True:
        row = get_user_input('Enter row: ')
        col = get_user_input('Enter column: ')
        if is_valid_turn(board, row, col):
            break
        print('Invalid place. Please try aagain.')
    board[row][col] = player
    return row, col


def check_win(board, last_row, last_col, player):
    return (
        all(cell == player for cell in board[last_row]) # row win
        or all(board[i][last_col] == player for i in range(3)) # column win
        or all(board[i][i] == player for i in range(3)) # first diag win
        or all(board[i][2 - i] == player for i in range(3)) # second diag win
    )


def play():
    board = init_board()
    display_board(board)
    players = ['X', 'O']
    is_draw = True

    for turn in range(9):
        player = players[turn % 2]
        row, col = player_turn(board, player)
        display_board(board)
        if check_win(board, row, col, player):
            print(f'Player {player} won! Congrats!')
            is_draw = False
            break
    
    if is_draw: 
        print('It\'s a draw!')

    if input('Play again? (y/n) ') == 'y':
        play()
        
if __name__ == "__main__":
    play()