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
crrNode = "AAA"
steps = 0
while crrNode != "ZZZ":
    for dir in lookUpTable:
        crrNode = lookUpNodes[crrNode][dir]
        steps+=1
        print(crrNode)
        print(dir)
        # print(lookUpNodes)    
print(steps)