# Justin Cai
# 7th Period
# 2018jcai@tjhsst.edu
import time
import math
import heapq
from collections import deque
import random
from random import shuffle

class nQueens:
    def __init__(self, state, allowed, choices, row, n, parent):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the self.state predecessor in a search
        """
        if state is None:
            self.state= [-1] * n
        else:
            self.state = state
##        self.choices=[set() for f in range(n)]
        self.size = n
        self.parent = parent
        if allowed is None:
            self.allowed = list(range(n))
        else:
            self.allowed = allowed
        if choices is None:
            self.choices = [list(range(n))]*(n)
        else:
            self.choices = choices
        if row is None:
            self.row = list(range(n))
        else:
            self.row = row

    def assign(self, var, value):
        """ updates the self.state by setting self.state[var] to value
            also propgates constraints and updates choices
        """
        if var is not 0:
            self.parent = self.state[var-1]
        self.state[var]=value
        self.allowed.remove(value)
        self.row.remove(var)
        for x in range(self.size):
            if self.state[x] is not value and value in self.choices[x]:
                self.choices[x].remove(value)
        if var is not self.size-1:
            if value is not self.size-1:
                if value+1 in self.choices[var+1] and self.state[var+1] is not value+1:
                    self.choices[var+1].remove(value+1)
            if value is not 0:
                if value-1 in self.choices[var+1] and self.state[var+1] is not value-1:
                    self.choices[var+1].remove(value-1)
        if var is not 0:
            if value is not self.size-1: 
                if value+1 in self.choices[var-1] and self.state[var-1] is not value+1:
                    self.choices[var-1].remove(value+1)
            if value is not 0:
                if value-1 in self.choices[var-1] and self.state[var-1] is not value-1:
                    self.choices[var-1].remove(value-1)

    def goal_test(self):
        """ returns True iff self.state is the goal self.state """
        for x in range(self.size):
            if self.state[x] not in self.choices[x]:
                return False
        return True
    def get_next_unassigned_var(self):
        if self.row:
            return self.row[0]
    def get_h1_var(self):
        final = self.row[0]
        for f in self.row:
            x = len(self.choices[f])
            y = len(self.choices[final])
            if x < y:
                final = f
        return final
##      ROWS IN ORDER
        """ returns the index of a column that is unassigned and
            has valid choices available """
        

    def get_choices_for_var(self, var):
        return self.choices[var]
        """ returns choices[var], the list of available values
                 for variable var, possibly sorted """
    def get_choices_for_var_h1(self, var):
        random.shuffle(self.choices[var])
        return self.choices[var]
    
    def __str__(self):
        strn = ""
        for n in range(self.size):
            strn+="#"
            for f in range(self.size):
                if self.state[n] is not f:
                    strn+= " -"
                else:
                    strn += " Q"
            strn+=" #\n"
        return strn
        """ returns a string representation of the object """


###---------------------------------------------------------------

def dfs_search(board):
    nodes = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
            return False
        current = fringe.pop()
        if current.goal_test():
            print(nodes)
            return current
        var = current.get_next_unassigned_var()
        if var is not None:
            for x in current.get_choices_for_var(var):
                choice = [x.copy() for x in current.choices]
                child = nQueens(current.state.copy(), current.allowed.copy(), choice, current.row.copy(), current.size, current.parent)
                nodes = nodes + 1
                child.assign(var, x)
                fringe.append(child)
def heuristic(board):
    ## RANDOM COLUMN
    nodes = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
            return False
        current = fringe.pop()
        if current.goal_test():
            print(nodes)
            return current
        var = current.get_next_unassigned_var()
        if var is not None:
            for x in current.get_choices_for_var_h1(var):
                choice = [x.copy() for x in current.choices]
                child = nQueens(current.state.copy(), current.allowed.copy(), choice, current.row.copy(), current.size, current.parent)
                nodes = nodes + 1
                child.assign(var, x)
                fringe.append(child)

def h1(board):
    ## LEAST CONSTRAINT ROW
    nodes = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
            return False
        current = fringe.pop()
        if current.goal_test():
            print(nodes)
            return current
        var = current.get_h1_var()
        if var is not None:
            for x in current.get_choices_for_var(var):
                choice = [x.copy() for x in current.choices]
                child = nQueens(current.state.copy(), current.allowed.copy(), choice, current.row.copy(), current.size, current.parent)
                nodes = nodes + 1
                child.assign(var, x)
                fringe.append(child)
def h2(board):
    ## RANDOM COLUMN AND LEAST CONSTRAINT ROW
    nodes = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
            return False
        current = fringe.pop()
        if current.goal_test():
            print(nodes)
            return current
        var = current.get_h1_var()
        if var is not None:
            for x in current.get_choices_for_var_h1(var):
                choice = [x.copy() for x in current.choices]
                child = nQueens(current.state.copy(), current.allowed.copy(), choice, current.row.copy(), current.size, current.parent)
                nodes = nodes + 1
                child.assign(var, x)
                fringe.append(child)
                 
if __name__ == '__main__':
    n = 83
    start = time.time()
    board = dfs_search(nQueens(None, None, None, None, n, None))
    print(time.time()-start)
    start = time.time()
    board = heuristic(nQueens(None, None, None, None, n, None))
    print(time.time()-start)
    start = time.time()
    board = h1(nQueens(None, None, None, None, n, None))
    print(time.time()-start)
    start = time.time()
    board = h2(nQueens(None, None, None, None, n, None))
    print(time.time()-start)
    """ sets board as the initial self.state and returns a
        board containing an nQueens solution
        or None if none exists
    """
