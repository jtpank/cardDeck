class Player:
    def __init__(self, id, chips):
        self.id = id
        self.chips = chips
        self.chipMax = chips
        self.hands = []
        self.didDouble = False
        self.firstDecision = True
        self.decision = "N"
        self.numTimesSplit = [0]
        self.allHandsAreComplete = False
    def resetChipStack(self):
        self.chips = self.chipMax
    def newHand(self):
        self.hands = []
        self.didDouble = [False]
        self.firstDecision = [True]
        self.numTimesSplit = [0]
        self.allHandsAreComplete = False
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
    def splitHand(self, currentHand):
        #hands[i] is a hand obj that has hand = [4,4]
        #and hands needs to become hands[i] = [4,newCard], hands[i+1] = [4, newCard]
        # 
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
            if self.numAces > 0:
                #use player softDeal
                otherCard = (self.handTotal - 11)
                if otherCard >= 8:
                    return playerSoftDeal[8][idx]
                elif otherCard == 7:
                    return playerSoftDeal[7][idx]
                elif otherCard == 6:
                    return playerSoftDeal[6][idx]
                elif otherCard == 4 or otherCard == 5:
                    return playerSoftDeal[5][idx]
                else:
                    return playerSoftDeal[3][idx]
            else:
                if self.handTotal >= 17:
                    return playerHardDeal[17][idx]
                elif self.handTotal >= 13 and self.handTotal < 17:
                    return playerHardDeal[16][idx]
                elif self.handTotal == 12:
                    return playerHardDeal[12][idx]
                elif self.handTotal == 11:
                    return playerHardDeal[11][idx]
                elif self.handTotal == 10:
                    return playerHardDeal[10][idx]
                elif self.handTotal == 9:
                    return playerHardDeal[9][idx]
                else:
                    return playerHardDeal[8][idx]
        else:
            if self.handTotal >= 17:
                return playerHardDeal[17][idx]
            elif self.handTotal >= 13 and self.handTotal < 17:
                return playerHardDeal[16][idx]
            elif self.handTotal == 12:
                return playerHardDeal[12][idx]
            elif self.handTotal == 11:
                return playerHardDeal[11][idx]
            elif self.handTotal == 10:
                return playerHardDeal[10][idx]
            elif self.handTotal == 9:
                return playerHardDeal[9][idx]
            else:
                return playerHardDeal[8][idx]

        return -1
    def setPlayerDecision(self, decision):
        self.decision = decision
    #reset player decision for the current hand
    def resetPlayerDecisions(self):
        self.didDouble = False
        self.firstDecision = True
        self.decision = "N"