# Justin Cai
# 7th Period
# 2018jcai@tjhsst.edu
import time
import math
import heapq
from collections import deque
import random
import copy
from random import shuffle

class Sudoku:
    def __init__(self, state, choices, row, n):
        """ creates an Sudoku board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the self.state predecessor in a search
        """
        if state is None:
            self.state= [[-1 for x in range(n)] for y in range(n)]
        else:
            self.state = state
##        self.choices=[set() for f in range(n)]
        self.size = n
        if choices is None:
            self.choices = [[list(range(n)) for x in range(n)] for y in range(n)]
        else:
            self.choices = choices
        if row is None:
            self.row = [81 for x in range(n)]
        else:
            self.row = row

    def assign(self, row, col, value):
        """ updates the self.state by setting self.state[var] to value
            also propogates constraints and updates choices
        """
        if self.state[row][col] is not -1:
            return
        else:
            self.state[row][col]=value
            self.row[row] = self.row[row] - 1
            for x in self.choices[row][col]:
                if x is not value:
                    self.choices[row][col].remove(x)
                    self.row[row] = self.row[row] - 1
            for x in range(self.size):
                if x is not row and value in self.choices[x][col]:
                    self.choices[x][col].remove(value)
                    self.row[x] = self.row[x] -1
                if x is not col and value in self.choices[row][x]:
                    self.choices[row][x].remove(value)
                    self.row[row] = self.row[row] - 1
            if row < 3:
                if col < 3:
                    for x in range(3):
                        for y in range(3):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 6:
                    for x in range(3):
                        for y in range(3, 6):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 9:
                    for x in range(3):
                        for y in range(6, 9):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
            elif row < 6:
                if col < 3:
                    for x in range(3, 6):
                        for y in range(3):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 6:
                    for x in range(3,6):
                        for y in range(3, 6):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 9:
                    for x in range(3,6):
                        for y in range(6, 9):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
            elif row < 9:
                if col < 3:
                    for x in range(6,9):
                        for y in range(3):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 6:
                    for x in range(6,9):
                        for y in range(3, 6):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
                elif col < 9:
                    for x in range(6,9):
                        for y in range(6, 9):
                            if x is not row and y is not col and value in self.choices[x][y]:
                                self.choices[x][y].remove(value)
                                self.row[x] = self.row[x]-1
    def goal_test(self):
        """ returns True iff self.state is the goal self.state """
        for x in range(self.size):
            for y in range(self.size):
                if self.state[x][y] not in self.choices[x][y]:
                    return False
        return True
    def get_next_unassigned_var(self):
        flen = 9
        final = None
        for row in range(9):
            for col in range(9):
                if self.state[row][col] == -1 and len(self.choices[row][col]) < flen:
                    flen = len(self.choices[row][col])
                    final = [row, col]
        return final

    def get_choices_for_var(self, var):
        x = int(var[0])
        y = int(var[1])
        return self.choices[x][y]
        """ returns choices[var], the list of available values
                 for variable var, possibly sorted """
    def __str__(self):
        strn = ""
        for n in range(self.size):
            strn+="#"
            for f in range(self.size):
                if self.state[n][f] == -1:
                    strn+= " -"
                else:
                    strn += " "
                    strn += str(self.state[n][f] + 1)
            strn+=" #\n"
        return strn
        """ returns a string representation of the object """


###---------------------------------------------------------------

def dfs_search(board):
    fringe = deque()
    fringe.append(board)
    node = 0
    while True:
        if not fringe:
            return False
        current = fringe.pop()
        if current.goal_test():
            print(node)
            return current
        var = current.get_next_unassigned_var()
        if var is not None:
            for x in current.get_choices_for_var(var):
                child = Sudoku(copy.deepcopy(current.state), copy.deepcopy(current.choices), copy.deepcopy(current.row), current.size)
                child.assign(int(var[0]), int(var[1]), x)
                fringe.append(child)
                node = node + 1
if __name__ == '__main__':
    n = 9
    b = Sudoku(None, None, None, n)
    b.assign(0, 0, 5)
    b.assign(0, 2, 1)
    b.assign(0, 4, 4)
    b.assign(1, 5, 3)
    b.assign(1, 7, 2)
    b.assign(3, 0, 3)
    b.assign(3, 1, 2)
    b.assign(3, 5, 7)
    b.assign(4, 1, 0)
    b.assign(4, 6, 1)
    b.assign(5, 6, 6)
    b.assign(6, 0, 4)
    b.assign(6, 3, 1)
    b.assign(6, 4, 6)
    b.assign(7, 7, 7)
    b.assign(7, 8, 0)
    b.assign(8, 3, 5)
#    b.assign(8, 2, 3)
    start = time.time()
    board = dfs_search(b)
    print(time.time()-start)
    print(board)

    """ sets board as the initial self.state and returns a
        board containing a Sudoku solution
        or None if none exists
    """