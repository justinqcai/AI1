import time
from collections import deque
import copy

class TTT:
    def __init__(self, board, boo):
        if board is not None:
            self.board = board
        else:
            self.board = [' '] * 10
        self.boo = boo

    def move(self, letter, x):
        if letter is True:
            self.board[x] = 'X'
            self.boo = False
        elif letter is False:
            self.board[x] = 'O'
            self.boo = True
    
    def isWinner(self, l):
        if l is False:
            le = 'X'
        if l is True:
            le = 'O'
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or
        (self.board[9] == le and self.board[5] == le and self.board[1] == le))
    
    def isSpaceFree(self, move):
        return self.board[move] == ' '


    def full(self):
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True
    def get_next_unassigned_var(self):
        final = []
        for x in range(1, 10):
            if self.board[x] is ' ':
                final.append(x)
        return final
def dfs_search(board):
    nodes = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
            return nodes
        current = fringe.pop()
        if current.isWinner(current.boo):
            nodes = nodes + 1
        elif current.full():
            nodes = nodes + 1
        else:
            var = current.get_next_unassigned_var()
            if len(var) is not 0:
                for x in var:
                    child = TTT(copy.deepcopy(current.board), copy.deepcopy(current.boo))
                    child.move(child.boo, x)
                    fringe.append(child)
if __name__ == '__main__':
    start = time.time()
    board = dfs_search(TTT(None, True))
    end = time.time()
    print(end- start)
    print(str(board))