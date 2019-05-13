from Othello_Core import OthelloCore
from random import shuffle
from random import randint
import os, signal
import time
from multiprocessing import Process, Value
time_limit = 5

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

SQUARE_WEIGHTS = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
bval = 100000000
aval = -(bval)
bestMove = -1

class Strategy(OthelloCore):
    def __init__(self):
        pass

    def is_valid(self, move):
        """Is move a square on the board?"""
        if move in self.squares():
        	return True
        return False

    def opponent(self, player):
        """Get player's opponent piece."""
        if player is BLACK:
            return WHITE
        elif player is WHITE:
            return BLACK

    def find_bracket(self, square, player, board, direction):
        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """
        opp = self.opponent(player)
        bracket = square + direction
        if board[bracket] is not opp:
            return None
        else:
            while board[bracket] is opp:
                bracket += direction
            if board[bracket] is player:
                return bracket
            else:
                return None


    def is_legal(self, move, player, board):
        """Is this a legal move for the player?"""
        for x in DIRECTIONS:
            if self.find_bracket(move, player, board, x) is not None:
                return True
        return False

    def make_move(self, move, player, board):
        board[move] = player
        for x in DIRECTIONS:
            board = self.make_flips(move, player, board, x)
        return board

        """Update the board to reflect the move by the specified player."""

    def make_flips(self, move, player, board, direction):
        if self.find_bracket(move, player, board, direction) is not None:
            opp = self.opponent(player)
            bracket = move + direction
            while board[bracket] is opp:
                board[bracket] = player
                bracket += direction
        return board
        """Flip pieces in the given direction as a result of the move by player."""

    def legal_moves(self, player, board):
        moves = []
        for move in self.squares():
            if board[move] is EMPTY:
                if self.is_legal(move, player, board) and move not in moves:
                    moves.append(move)
        return moves
        """Get a list of all legal moves for player, as a list of integers"""

    def any_legal_move(self, player, board):
        if len(self.legal_moves(player, board)) is 0:
            return False
        return True
        """Can player make any moves? Returns a boolean"""

    def next_player(self, board, prev_player):
        if prev_player is WHITE:
            player = BLACK
        else:
            player = WHITE
        if self.any_legal_move(player, board) is False:
            if self.any_legal_move(prev_player, board) is False:
                return None
            else:
                return prev_player
        return player
    def score(self, player, board):
        count1 = 0
        count2 = 0
        for x in board:
            if x is player:
                count1 = count1 + 1
            elif x is self.opponent(player):
                count2 = count2 + 1
        return count1 - count2
    def weight(self, p, o, b):
    	fnl = 0
        moves = self.legal_moves(o, b)
    	for x in self.squares():
    		if b[x] is p:
    			fnl += SQUARE_WEIGHTS[x]
    		elif b[x] is o:
    			fnl -= SQUARE_WEIGHTS[x]
        for x in moves:
            fnl -= 10
        if len(moves) is 1:
            fnl += 120
    	return fnl
    def max_dfs(self, board, player, alpha, beta, max_d, current_d):
        if self.any_legal_move(player, board) is False:
            if self.score(player, board) == 0:
                return 0, None
            elif self.score(BLACK, board) > 0:
                return 100000000, None
            elif self.score(BLACK, board) < 0:
                return -100000000, None
        if current_d == max_d:
            return self.weight(player, self.opponent(player), board), None
        v = -100000000
        move = -1
        for m in self.legal_moves(player, board):
            new_value = self.min_dfs(self.make_move(m, player, list(board)), self.opponent(player), alpha, beta, max_d, current_d + 1)[0]
            if new_value == v:
                return new_value, m
            elif new_value > v:
                v = new_value
                move = m
            if v >= beta:
                return v, move
            alpha = max(alpha, v)
        return v, move
    def min_dfs(self, board, player, alpha, beta, max_d, current_d):
        if self.any_legal_move(player, board) is False:
            if self.score(player, board) == 0:
                return 0, None
            elif self.score(BLACK, board) > 0:
                return 100000000, None
            elif self.score(BLACK, board) < 0:
                return -100000000, None
        if current_d == max_d:
            return self.weight(player, self.opponent(player), board), None
        v = 100000000
        move = -1
        for m in self.legal_moves(player, board):
            new_value = self.max_dfs(self.make_move(m, player, list(board)), self.opponent(player), alpha, beta,
                                max_d, current_d + 1)[0]
            if new_value == v:
                return new_value, m
            elif new_value < v:
                v = new_value
                move = m
            if v <= alpha:
                return v, move
            beta = min(beta, v)
        return v, move
    def best_strategy(self, board, player, best_move, still_running):
        while(still_running.value > 0 and best_move.value<1000):
            time.sleep(1)
            best_move.value = self.alphabeta_search(3)(player, board)
    def alphabeta(self, board, player, depth):
        if player == BLACK: move = self.max_dfs(board, player, aval, bval, depth, 0)[1]
        if player == WHITE: move = self.min_dfs(board, player, aval, bval, depth, 0)[1]
        return move
    def alphabeta_search(self, depth):
        def strategy(player, board):
            return self.alphabeta(board, player, depth)
        return strategy
    def human_strategy(self, depth):
    	def human(player, board):
    		print('Human: ')
    		pos = input()
    		pos = str(pos)
    		pos = (int(pos[0]))*10 + (int(pos[1]))
    		while pos not in self.legal_moves(player, board):
    			print('Human: ')
    			pos = input()
    			pos = str(pos)
    			pos = (int(pos[0]))*10 + (int(pos[1]))
    		return pos
    	return human
    def random_strategy(self, depth):
        def random(player, board):
            move = -1
            while move not in self.legal_moves(player, board):
                move = randint(11, 89)
            return move
        return random