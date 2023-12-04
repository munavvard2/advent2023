file = open("day4_input.txt")
str = file.read()
file.close()

listOfCards = list(map(lambda s : s.split(": "),str.split("\n")))
winnigPoints = []
for card in listOfCards :
    numbers = (card[1].split(' | '))
    winningNumbers = numbers[0].split()
    numbersWeHave = numbers[1].split()
    numbersWeWon = [value for value in winningNumbers if value in numbersWeHave]
    print(winningNumbers)
    print(numbersWeHave)
    print(numbersWeWon)
    if len(numbersWeWon) > 0 :
        thisSum = 1
        for number in range(0,len(numbersWeWon) - 1) :
            thisSum = thisSum * 2
        winnigPoints.append(int(thisSum))
print(winnigPoints)
print(sum(winnigPoints))
