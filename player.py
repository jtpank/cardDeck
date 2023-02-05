import hand
class Player:
    def __init__(self, id, chips):
        self.id = id
        self.chips = chips
        self.chipMax = chips
        self.hands = [hand.Hand()]
        self.splitHand = hand.Hand()
        self.didDouble = False
        self.firstDecision = True
        self.decision = "N"
        self.numTimesSplit = 0
        self.allHandsAreComplete = False
        self.betSize = 0
    def resetChipStack(self):
        self.chips = self.chipMax
    def newHand(self):
        self.hands = [hand.Hand()]
        self.splitHand = hand.Hand()
        self.didDouble = [False]
        self.firstDecision = [True]
        self.numTimesSplit = 0
        self.allHandsAreComplete = False
    def setBetSize(self, value):
        self.betSize = value
    def addChips(self, value):
        self.chips += value
    def reduceChips(self, value):
        self.chips -= value
    def showInfo(self):
        print("Player " + str(self.id) + " Decision: " + self.decision + " Chips: " + str(self.chips))
    def printChipSize(self):
        print("Player " + str(self.id) + " Chip size: " + str(self.chips))
    def setDidDouble(self, idx):
        if idx >= len(self.didDouble)-1:
            self.didDouble.append(True)
        else:
            self.didDouble[idx] = True
    def splitAHand(self, idx):
        #hands[i] is a hand obj that has hand = [4,4]
        #and hands needs to become hands[i] = [4,newCard], hands[i+1] = [4, newCard]
        return
        #TODO: must assign the next split hand to the next position NOT append
        # if you split, then split, you have to keep track of where that split occured
        # can only have 1 split hadn at a time
        return
    #Game Logic
    #make a decision for a single hand (2 cards)
    #returns a decision of:
    # "S" for stand, "D" for double down
    # "SP" for split, "H" for hit      
    def makeDecision(self, dealerVisibleCard, playerSoftDeal, playerHardDeal, playerPairDeal):
        #can hit or stand based off visible card
        #implement basic strategy
        initialIndex = dealerVisibleCard
        if dealerVisibleCard == 1:
            initialIndex = 11
        #must be 0-9 for the lookup array
        idx = initialIndex - 2
        if self.firstDecision:
            self.firstDecision = False
            #if paired hand
            if self.hands[0].hand[0] == self.hands[0].hand[1]:
                card = self.hands[0].hand[0]
                return playerPairDeal[card][idx]
            else:
                tot = self.hands[0].handTotal
                if self.hands[0].numAces > 0:
                    #use player softDeal
                    otherCard = (self.hands[0].handTotal - 11)
                    return playerSoftDeal[otherCard][idx]
                else:
                    return playerHardDeal[tot][idx]
        else:
            tot = self.hands[0].handTotal
            return playerHardDeal[tot][idx]
        return -1

    def setPlayerDecision(self, decision):
        self.decision = decision
    #reset player decision for the current hand
    def resetPlayerDecisions(self):
        self.didDouble = False
        self.firstDecision = True
        self.decision = "N"