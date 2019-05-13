### Hi Mr. White, please run this file first before running railroad.py
import pickle

def putFileIntoArray():
   myFile = open("rrNodes.txt")
   stationList, stationCoor, stationCities = {}, {}, {}
   for line in myFile:
      parts = line.split()
      stationList[parts[0]] = ""
      stationCoor[parts[0]] = [float(parts[1]), float(parts[2])]
   myFile = open("rrCities.txt")
   for line in myFile:
      parts = line.strip("/n").split()
      for n in range(0, len(parts)):
         if(n>1):
            parts[1] = parts[1] + " " + parts[n]
      print(parts)
      stationCities[parts[1]] = parts[0]
   return stationList, stationCoor, stationCities

def createDictionary(stationList):
   dictionary = {}
   for str in stationList:
      dictionary[str] = []
   myFile = open("rrEdges.txt")
   for line in myFile:
      parts = line.split()
      dictionary[parts[0]].append(parts[1])
      dictionary[parts[1]].append(parts[0])
   return dictionary
      
def putIntoFile(element, fileName):
   myFile = open(fileName, "wb")
   pickle.dump(element, myFile)
   myFile.close()

def main():
   stationList, stationCoor, stationCities = putFileIntoArray()
   dictionary = createDictionary(stationList)
   putIntoFile(stationCities, "stationlist.txt")
   putIntoFile(dictionary, "stationhash.txt")
   putIntoFile(stationCoor, "stationcoordinates.txt")
   print("Done!")
   
main()
