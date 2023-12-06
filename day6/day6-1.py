file = open("day6_input.txt")
inputData = file.read()
file.close()
import functools 


inputData = inputData.split("\n")
raceTimes = list(map( lambda x : int(x),inputData[0].replace('Time:      ',"").split()))
raceDists = list(map( lambda x : int(x),inputData[1].replace('Distance:  ',"").split()))

races = (list(zip(raceTimes,raceDists)))

winnigWays = {}

for time,dist in races :
    matchWon = []
    for i in range(0,time + 1) : 
        distCoverd = (i*abs((i - time)))
        if distCoverd > dist :
            matchWon.append(distCoverd)
    winnigWays.setdefault("match " + str(time),matchWon)
acc = 1
for match,ways in winnigWays.items():
    acc = acc * len(ways)
print(acc)
