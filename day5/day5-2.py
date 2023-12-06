file = open("day5_input.txt")
inputData = file.read()
file.close()
inputData = inputData.split("\n")
seedsPAIR = list(map(lambda x: int(x),inputData[0].replace("seeds: ","").split(" ")))
# seeds = seedsPAIR
# # for i in range(0,len(seedsPAIR),2) : 
# #     seeds = list(set(seeds))
# #     seeds.extend(list(range(seedsPAIR[i],seedsPAIR[i] + seedsPAIR[i+1])))
# # print(seeds)
# # exit()
# seeds = list(range(924423181,924423185))#924423181 + 691197498))
# seeds = list(zip(seedsPAIR[::2], seedsPAIR[1::2]))
inputData.pop(0)
inputData.pop(0)
crrtable = ""
allData = {}
for value in inputData:    
    if value == "":
        continue
    # end if
    if "map" in value:
        crrtable = value.replace(' map:',"")
    else:
        values = list(map(lambda x: int(x),value.split(" ")))
        srcDest = crrtable.split("-to-")
        if crrtable not in allData.keys() :
            allData.setdefault(crrtable,{})
        if srcDest[0] not in allData[crrtable] : 
            allData[crrtable].setdefault(srcDest[0],[])
        if srcDest[1] not in allData[crrtable] : 
            allData[crrtable].setdefault(srcDest[1],[])

        allData[crrtable][srcDest[0]].append({"from": values[1], "to": (values[1] + values[2])})
        allData[crrtable][srcDest[1]].append({"from": values[0], "to": (values[0] + values[2])})
    # end if
# end for
seedslocation = {}
minLocation = 9999999999999999999999999999999999999999999
allDataKeys = allData.keys()
for i in range(0,len(seedsPAIR),2) : 
    for seed in range(seedsPAIR[i],seedsPAIR[i] + seedsPAIR[i+1]):
    # for seed in seeds:
        searchvalue = int(seed)
        for key in allDataKeys:
            keys = key.split("-to-")
            value = allData[key]
            diff = -1
            whichIndex = 0
            for checking in value[keys[0]]:
                if checking["from"] <= searchvalue <= checking["to"]:
                    diff = checking["from"] - searchvalue
                    break
                whichIndex = whichIndex + 1
                # end if
            # end for
            if diff == -1:
                pass
            else:
                searchvalue = value[keys[1]][whichIndex]["from"] + abs(diff)
            # end if
        # end for
        if searchvalue < minLocation :
            minLocation = searchvalue
    # end for
# end for
print(minLocation)
