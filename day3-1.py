import re
file = open("day3_input.txt")
str = file.read()
file.close()

str =(str.split())
regexForSpecialChar = r"[^0-9.:space:\n]"
regexForNumber = r"[0-9]{1,10}"
qualifyingNumbers = []

def getNumber(thisRange,positionOfChar,digitsMatch) :
    thisRange = set(thisRange)
    thatRange = set(range(positionOfChar - 1, positionOfChar + 2))
    if(len(list(set(thisRange).intersection(thatRange)))) :
        return int(digitsMatch.group())
    return 0
        
    
for i in range(0,len(str)) :
# for s in str:
    s = str[i]
    for match in re.finditer(regexForSpecialChar, s) : 
        positionOfChar = match.start()
        # print('symbol',positionOfChar,match.group())

        # print(match.start()) #found special char on this pos now looking for adjucsent 
        #all this below # position will have number to qualify
        ### => prev[positionOfChar-1],prev[positionOfChar],prev[positionOfChar+1]
        #*# => s   [positionOfChar-1],                    ,s   [positionOfChar+1]
        ### => next[positionOfChar-1],next[positionOfChar],next[positionOfChar+1]
        prev = str[i-1]
        next = str[i+1]
        # matchDigitsinPrevAndNext
        for digitsMatch in re.finditer(regexForNumber,prev) :
            qualifyingNumbers.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))
        for digitsMatch in re.finditer(regexForNumber,s) :
            qualifyingNumbers.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))
        for digitsMatch in re.finditer(regexForNumber,next) :
            qualifyingNumbers.append(getNumber(range(digitsMatch.start(),digitsMatch.end()),positionOfChar,digitsMatch))

print(qualifyingNumbers)            
print(sum(qualifyingNumbers))
