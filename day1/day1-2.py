import re
import functools

file = open("day1_input.txt")
str = file.read()
file.close()

mapper = {
    # "zero" : "0"
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",    
}
# for key, value in mapper.items():
#     str = str.replace(key, value)

# print(str)
strDigitArr = []
for singleStr in str.splitlines():
    res = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9])){1}", singleStr) #regex for matching 
    replacedLineToDigits = [] #accumulator
    for digit in res:
        replacedLineToDigits.append(mapper.get(digit, digit)) #find and append to acc, default value if its not in dict
    strDigitArr.append(replacedLineToDigits) #to main list
print(functools.reduce(lambda a,b : a+b,list(map(lambda singleStr : int(singleStr[0]+""+singleStr[len(singleStr) -1 ]),strDigitArr)))) #as in day 1-1