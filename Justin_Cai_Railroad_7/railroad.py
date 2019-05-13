import pickle
import sys
import math

myFile = open("stationhash.txt", "rb")
d = pickle.load(myFile)
myFile.close()

myFile = open("stationlist.txt", "rb")
sL = pickle.load(myFile)
myFile.close()

myFile = open("stationcoordinates.txt", "rb")
cords = pickle.load(myFile)
myFile.close()

file = open("solution.txt", "w")

def calc(y1, x1, y2, x2):
  x1 = float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)
  R = 3958.76 #miles
  x1 *= (math.pi)/180.0
  y1 *= (math.pi)/180.0
  x2 *= (math.pi)/180.0
  y2 *= (math.pi)/180.0
  return math.acos(min(1, math.sin(y1)*math.sin(y2)+math.cos(y1)*math.cos(y2)*math.cos(x2-x1)))*R

def method(s1, s2):
   queue = [(0, s1, [], 0)]
   closed = {}
   count = 0


   while(queue): #f = item[0], node = item[1], path = item[2], g = item[3]
     item = queue.pop(0)
     count += 1
     if(item[1] == s2):
       item[2].append(s2)
       file.write("Distance: " + str(item[3]) + '\n')
       break
     else:
       closed[item[1]] = item[3]
       children = d[item[1]]
       for c in children:
         g = calc(cords[item[1]][0], cords[item[1]][1], cords[c][0], cords[c][1])
         h = calc(cords[c][0], cords[c][1], cords[s2][0], cords[s2][1])
         if(c in closed):
           if(closed[c] > item[3] + g):
             del closed[c]
             path = list(item[2])
             path.append(item[1])
             queue.append((item[3]+g+h, c, path, item[3]+g))
         else:
           b = True
           for q in queue:
             if(c in q):
               if(q[3] > item[3] + g):
                 queue.remove(q)
                 path = list(item[2])
                 path.append(item[1])
                 queue.append((item[3]+g+h, c, path, item[3]+g))
               b = False
           if(b):
             path = list(item[2])
             path.append(item[1])
             queue.append((item[3]+g+h, c, path, item[3]+g))
     queue.sort()
with open("test.txt") as f:
   for line in f:
      s1 = line[:line.index(",")]
      s1 = sL[s1]
      s2 = line[line.index(",")+2:len(line)-1]
      s2 = sL[s2]
      method(s1, s2)
file.close()
