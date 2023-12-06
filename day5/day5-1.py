file = open("day5_input.txt")
inputData = file.read()
file.close()
inputData = inputData.split("\n")
seeds = inputData[0].replace("seeds: ","").split(" ")

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
for seed in seeds:
    searchvalue = int(seed)
    for key in allData.keys():
        print(key,searchvalue);
        keys = key.split("-to-")
        value = allData[key]
        diff = -1
        whichIndex = 0
        for checking in value[keys[0]]:
            print(searchvalue,checking)
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
    seedslocation[seed] = searchvalue
# end for
print(min(seedslocation.values()))
