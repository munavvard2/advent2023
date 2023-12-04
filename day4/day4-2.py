file = open("day4_input.txt")
stralsd = file.read()
file.close()

listOfCards = list(map(lambda s : s.split(": "),stralsd.split("\n")))
winnigPoints = []

cardDetails = []
cardAcc = {}
def getCopiesOfCard(card,cardId) : 
    # print("processing card" + str(cardId + 1))    
    numbers = (card[1].split(' | '))
    winningNumbers = numbers[0].split()
    numbersWeHave = numbers[1].split()
    numbersWeWon = [value for value in winningNumbers if value in numbersWeHave]
    # print(numbersWeWon)
    if ("card "+str(cardId + 1)) not in  cardAcc.keys() :
        cardAcc["card "+str(cardId + 1)] = 0    
    cardAcc["card "+str(cardId + 1)] = cardAcc["card "+str(cardId + 1)] + 1
    if len(numbersWeWon) > 0 :
        for i in range(1,len(numbersWeWon) + 1) :
            copyCardId = cardId + i
            # print('cardId',cardId)
            # print('i',i)
            # print('copyCardId',copyCardId)
            # print(copyCardId)
            if copyCardId > 206 :
                return 
            copyCard = listOfCards[copyCardId]
            getCopiesOfCard(copyCard,copyCardId)
    else : 
        return card

for cardId in range(0,len(listOfCards)) :
    # print("process for card" + str(cardId + 1))    
    card = listOfCards[cardId]
    getCopiesOfCard(card,cardId)

# print(cardDetails)
print(sum(cardAcc.values()))