from random import shuffle
from itertools import permutations

class nQueens:
    def __init__(self):
        return
    def printBoard(self, board):
        print('#'*(1+2*(len(board)+1)))
        for i in range(len(board)):
            print('#', end = '')
            for j in range(len(board)):
                if j != board[i]:
                    print(' -', end = '')
                else:
                    print (' Q', end = '')
            print(' #')
        print('#'*(1+2*(len(board)+1)))

    def cost(self, board):
        count = 0
        for i in range(len(board)):
            s = i + board[i]
            d = i - board[i]
            for j in range(i):
                if s == j + board[j]: count += 1
                if d == j - board[j]: count += 1
        return count

    def swaps(self, parent):
        L = []
        for i in range(len(parent)):
            for j in range(i+1,len(parent)):
                s = parent[:]
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                L.append(s)
        return L

    def randomPerm(self, n):
        L = []
        for i in range(n):
            L.append(i)
        shuffle(L)
        return L

    def hillClimb(self, n):
        dec = False
        while not dec:
            parent = self.randomPerm(n)
            dec = True
            while dec:
                c = self.cost(parent)
                if c == 0:
                    self.printBoard(parent)
                    return
                co = float('inf')
                for a in self.swaps(parent):
                    if co > self.cost(a):
                        co = self.cost(a)
                        par = a
                if co < c: parent = par
                else: dec = False
    

if __name__ == '__main__':
    n = 10
    queen = nQueens()
    queen.hillClimb(n)
