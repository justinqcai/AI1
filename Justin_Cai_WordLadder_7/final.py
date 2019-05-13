import pickle

start = input("Starting word: ")
targ = input("Target word: ")

file = open("wordhash.txt", "rb")
dictionary = pickle.load(file)

file.close()

if(not(start in dictionary)):
   sys.exit(start + " does not exist in the dictionary.")
if(not(targ in dictionary)):
   sys.exit(targ + " does not exist in the dictionary.")

for x in dictionary:
   dictionary[x] = [dictionary[x], -1, -1]

prev = [start]
dictionary[start][1] = 0
dictionary[start][2] = "None"
queue = [start]
count = 0

while(queue):
   current = queue.pop(0)
   count += 1
   if(current == targ):
      break
   neighbors = dictionary[current][0]
   level = dictionary[current][1]
   for n in neighbors:
      if(not(n in prev)):
         queue.append(n)
         dictionary[n] = [dictionary[n][0], level+1, current]
         prev.append(n)

temp = targ

path = []

while(True):
   if(dictionary[temp][2] == "None"):
      path.append(temp)
      break
   path.append(temp)
   temp = dictionary[temp][2]
  
path.reverse()
print(path)
