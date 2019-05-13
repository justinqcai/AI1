from core import *
from random import randint

def minimax_strategy(max_depth):
    """ Takes a max_depth parameter and returns a new function/closure for strategy """
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy

def minimax(board, player, max_d):
    if player == MAX: return max_dfs(board, player, max_d, 0)[1]
    if player == MIN: return min_dfs(board, player, max_d, 0)[1]

def max_dfs(board, player, max_d, current_d):
    if "X" not in board and "O" not in board:
        board = make_move(board, player, 4)
        return None, 4
    tt = terminal_test(board)
    if tt:
        if tt == MAX:
            return 10000000, None
        elif tt == MIN:
            return -10000000, None
        elif tt == TIE:
            return 0, None
    v = -1000000
    move = -1
    act = actions(board)
    for m in act:
        new_value = min_dfs(make_move(board, player, m), toggle(player), max_d, current_d+1)[0]
        if new_value >= v:
            v = new_value
            move = m
    return v, move

def min_dfs(board, player, max_d, current_d):
    if "X" not in board and "O" not in board:
        board = make_move(board, player, 4)
        return None, 4
    tt = terminal_test(board)
    if tt:
        if tt == MAX:
            return 1000000, None
        elif tt == MIN:
            return -10000000, None
        elif tt == TIE:
            return 0, None
    v = 10000000
    move = -1
    act = actions(board)
    for m in act:
        new_value = max_dfs(make_move(board, player, m), toggle(player), max_d, current_d+1)[0]
        if new_value <= v:
            v = new_value
            move = m
    return v, move

def human(board, player):
    move = -1
    while move not in range(9):
        print('What is your next move? (0-8)')
        move = int(input())
    return move
def random(board, player):
    move = -1
    while move not in range(9) or board[move] is not '.':
            move = randint(0,8)
    return move

