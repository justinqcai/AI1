import time
import heapq
from collections import deque
class wordladder:
    
    def __init__(self,word,upper):
        
        self.word = word
        self.upper = upper
        
    def final(self):
        
        t = self
        arr = []
        
        arr.append(self)
        
        while t.upper != None:
            
            t = t.upper
            arr.insert(0,t)
            
        for x in range(0,len(arr)):
            
            print(arr[x].word)

class wlsolution:
    
    def __init__(self, targ, end):

        self.starting = targ

        self.result = end
        
        self.worddict = []
        
        file = open("dictionary.txt", "r")
        
        self.worddict = file.read().split('\n')
        self.worddict.append(end.word)
        
    def poss(self, current):
        possibilities = []
        cw = list(current.word)
        for target in self.worddict:
            x = 0
            lw = list(target)
            for index in range(0,6):
                
                if not lw[index] == cw[index]:
                    
                    x = x + 1
            if x == 1:
                add = wordladder(target, current)
                
                possibilities.append(add)
                
                self.worddict.pop(self.worddict.index(target))
                
        return possibilities
    
    def solved(self, x):
        
        return x == self.result.word

    def search(self):
        
        fringe = deque()
        fringe.append(self.starting)
        while True:
            if not fringe:
                return False
            current = fringe.pop()
            if current == self.result:
                return current
            var = self.poss()
            if var is not None:
                for x in var:
                    choice = [x.copy() for x in current.choices]
                    child = nQueens(current.state.copy(), current.allowed.copy(), choice, current.row.copy(), current.size, current.parent)
                    nodes = nodes + 1
                    child.assign(var, x)
                    fringe.append(child)    
  
##### CHANGE WORDS HERE FOR DIFFERENT PROBLEMS ######
start = time.time()
solver1 = wlsolution(wordladder("rudest",None),wordladder("emboil",None))
solver1.search()        
end = time.time()
print(end-start)
