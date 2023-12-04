import re
import functools
file = open("day1_input.txt")
str = file.read()
file.close()

# def get2Digits(singleStr):
#     return int(singleStr[0]+""+singleStr[len(singleStr) -1 ])
print(functools.reduce(lambda a,b : a+b,list(map(lambda singleStr : int(singleStr[0]+""+singleStr[len(singleStr) -1 ]),re.sub(r"[a-z]+",'',str).splitlines()))))