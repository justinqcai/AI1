import random
import time
from collections import deque
import math
import heapq
_maxtiles = 0
_goal_state = [(i+1) for i in range(_maxtiles)]
_count = 0
class Node:
    def __init__(self, state, parent, depth, action, cost):
        self.state = state
        self.parent = parent
        self.depth= depth
        self.aciton = action
        self.children
        self.cost = cost
        self.children = []
    def display(self):
        print(self.state, self.action)
    def goal_test(self):
        global _count
        _count +=1
        if_count & 10000 = 0:
            print("Node count: ", _count, "Depth:", self.depth)
        return self.state == _goal_state
    def get_Solution(self):
        n = self
        so = [n]
        while n.parent is not None:
            n = n.parent
            sol.append(n)
        sol.reverse()
        actions = ""
        for s in sol:
            actions += s.action
        print("Solution...", actions)
        return sol
    def swap_blank(self, a, b):
        new_state = self.state.copy()
        t = new_state[a]
        new_state[a] = new_state[b]
        new_state[b] = t
        return new_state
    def expand(self):
        blank_index = self.state.index(_maxtiles)
        row= blank_index // _width
        col = blank_index % _width
        if col < 2:
            new_state = self.swap_blank(blank_index, blank_index + 1)
            action = "R"
            self.add_child(Node(new_state, self, self.depth + 1, action, 0))
        if col> 0:
            new_state = self.swap_blank(blank_index, blank_index -1)
            action = "L"
            self.add_child(Node(new_state, self, self.depth + 1, action, 0))
    def add_child(self, node):
        n = self
        while n is not None and n.state != node.state:
            n = n.parent
        if n is None:
            self.children.append(node)
    def __lt__(self, other):
        return self.cost < 
    def treesearch():
    def jumble(steps):
    def compute_anhattan_distance(self):
        dist = 0
        for r in range(_width):
            for c in range(_length):
                tile = self.state [r*_width + c]
                if(tile != _maxtiles):
                    correctRow = )tile - 1)// _width
                    correctCol = (tile - 1) % _width
                    dist += abs(r- correctRow)+abs(c-correctCol)
        return dist
    


    
