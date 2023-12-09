from collections import Counter
class Hand : 
    def getCardValues(self,cardChar) : 
        if cardChar.isnumeric():
            return int(cardChar)
        mapper = {
            'T' : 10,
            'J' : 1,
            'Q' : 12,
            'K' : 13,
            'A' : 14
        }
        return mapper[cardChar]

    def __init__(self,hand) : 
        cardsRow,points = hand.split()
        self.points = int(points)
        self.cards = tuple(self.getCardValues(cardChar) for cardChar in cardsRow)
        self.handPower = self.getHandPower()

    def getHandPower(self) : 
        counter = Counter(self.cards)
        highestTimes = max(counter.values())

        Js = counter[1]
        del counter[1]
        highestTimes = Js
        if counter : 
            highestTimes += max(counter.values())
            
        if highestTimes == 5 or highestTimes == 4 : # 5 or 4 same
            return (highestTimes + 1)
        elif len(counter) == 2 : #full
            return 4
        elif highestTimes == 3 : # 3 same
            return 3 
        elif len(counter) == 3 : # 2pair
            return 2
        elif highestTimes == 2 : 
            return highestTimes - 1
        else:
            return 0
    def __lt__(self,other):
        return self.handPower < other.handPower or (self.handPower == other.handPower and self.cards < other.cards)
    def __repr__(self) :  # toString()
        return "cards : "  + str(self.cards) + ", Points : "+str(self.points)+ "\n"

def getResult(inputData) :
    hands = [Hand(hand) for hand in inputData]
    # hands.sort(key = lambda x : x.handPower) 
    hands.sort()
    ans = 0 
    for i,hand in enumerate(hands):
        ans += hand.points * (i+1)
    return ans

file = open("day7_input.txt")
inputData = file.read().split("\n")
file.close()
print(getResult(inputData))
