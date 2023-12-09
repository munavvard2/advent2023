import math
import itertools as it
file = open("day8_input.txt")
inputData = file.read().split("\n")
file.close()

lookUpTable = inputData[0]
lookUpNodes = {}
nodeList = inputData[2::]
for node in nodeList:
    node = node.split("=")
    nodeLR = node[1].replace("(","").replace(")","").split(",")
    lookUpNodes[node[0].strip()] = {
        "L" : nodeLR[0].strip(),
        "R" : nodeLR[1].strip()
    }
crrNodes = list(filter(lambda x: x.endswith("A"),lookUpNodes.keys()))
targetNodes = list(filter(lambda x: x.endswith("Z"),lookUpNodes.keys()))
# print(crrNodes)
# print(targetNodes)
zreached = []
for anode in crrNodes :
    steps = 0
    znode = anode
    for dir in it.cycle(lookUpTable.strip()):
        znode = lookUpNodes[znode][dir]
        # crrNodes = list(map(lambda x : lookUpNodes[x][dir],crrNodes))
        # lookUpNodes[crrNodes[0]][dir],lookUpNodes[crrNodes[1]][dir]]
        steps+=1
        if znode.endswith('Z') : 
            zreached.append(steps)
            break
        # print(list(set(crrNodes) & set(targetNodes)))
        # if targetNodes == crrNodes :
            # break
        # print(lookUpNodes)
print(math.lcm(*zreached))
# print(steps)