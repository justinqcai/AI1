from core import *
from random import randint

dictionary = {}
def human(board, player):
    move = ' '
    x = -1
    l = actions(board)
    print(board)
    while x not in l:
        print('What is your next move?')
        move = input()
        x = int(move)
    return x
def random(board, player):
    move = -1
    while move not in range(9) or board[move] is not '.':
        move = randint(0,8)
    return move
def max_dfs(board, player, max_d, current_d):
    if terminal_test(board):
        if terminal_test(board) == TIE:
            return 0, None
        elif terminal_test(board) == MAX:
            return 100000000, None
        elif terminal_test(board) == MIN:
            return -100000000, None
    v = -100000000
    move = -1
    for m in actions(board):
        new_value = min_dfs(make_move(board, player, m), toggle(player),
                            max_d, current_d + 1)[0]
        if new_value == v:
            return new_value, m
        if new_value > v:
            v = new_value
            move = m
        # new_board = make_move(board, player, m)
        # if (new_board, player) in dictionary:
        #     new_value = dictionary[(new_board, player)]
        # else:
        #     new_value = min_dfs(new_board, toggle(player), max_d, current_d+1)[0]
        #     dictionary[(new_board, player)] = new_value
        # if new_value > v:
        #     v = new_value
        #     move = m
    return v, move

def min_dfs(board, player, max_d, current_d):
    if terminal_test(board):
        if terminal_test(board) == TIE:
            return 0, None
        elif terminal_test(board) == MAX:
            return 100000000, None
        elif terminal_test(board) == MIN:
            return -100000000, None
    v = 100000000
    move = -1
    for m in actions(board):
        new_value = max_dfs(make_move(board, player, m), toggle(player),
                            max_d, current_d + 1)[0]
        if new_value == v:
            return new_value, m
        if new_value < v:
            v = new_value
            move = m
        # new_board = make_move(board, player, m)
        # if (new_board, player) in dictionary:
        #     new_value = dictionary[(new_board, player)]
        # else:
        #     new_value = max_dfs(new_board, toggle(player), max_d, current_d + 1)[0]
        #     dictionary[(new_board,player)] = new_value
        # if new_value < v:
        #     v = new_value
        #     move = m
    return v, move


def minimax_strategy(max_depth):
    """ Takes a max_depth parameter and returns a new function/closure for strategy """
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy

def minimax(board, player, max_depth):
    """ Takes a current board and player and max_depth and returns a best move
     This is the top level mini-max function. Note depth is ignored. We
     always search to the end of the game."""
    if player == MAX: move= max_dfs(board, player, max_depth, 0)[1]
    if player == MIN: move= min_dfs(board, player, max_depth, 0)[1]
    #print("player %s selects %i" % (player,move))
    return move