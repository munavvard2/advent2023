import re
file = open("day3_input.txt")
str = file.read()
file.close()

str =(str.split())
# regexForSpecialChar = r"[^0-9.:space:\n]"
regexForSpecialChar = r"\*"
regexForNumber = r"[0-9]{1,10}"
qualifyingNumbers = []

def getNumber(thisRange,positionOfChar,digitsMatch) :
    thisRange = set(thisRange)
    print(digitsMatch.group())
    thatRange = set(range(positionOfChar - 1, positionOfChar + 2))
    if(len(list(set(thisRange).intersection(thatRange)))) :
        return int(digitsMatch.group())
    return 0
    
for i in range(0,len(str)) :
# for s in str:
    s = str[i]
    for match in re.finditer(regexForSpecialChar, s) : 
        thisMatch = []
        positionOfChar = match.start()
        print('symbol',positionOfChar,match.group())

        # print(match.start()) #found special char on this pos now looking for adjucsent 
        #all this below # position will have number to qualify
        ### => prev[positionOfChar-1],prev[positionOfChar],prev[positionOfChar+1]
        #*# => s   [positionOfChar-1],                    ,s   [positionOfChar+1]
        ### => next[positionOfChar-1],next[positionOfChar],next[positionOfChar+1]
        prev = str[i-1]
        next = str[i+1]

        for digitsMatch in re.finditer(regexForNumber,prev) :
            thisMatch.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))
        for digitsMatch in re.finditer(regexForNumber,s) :
            thisMatch.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))
        for digitsMatch in re.finditer(regexForNumber,next) :
            thisMatch.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))
        thisMatch = list(filter(lambda x : True if (x > 0) else False,thisMatch))
        if(len(thisMatch) == 2) : 
            qualifyingNumbers.append(thisMatch[0] * thisMatch[1])      
print(qualifyingNumbers)            
print(sum(qualifyingNumbers))
