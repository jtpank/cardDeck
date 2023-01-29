class Player:
    def __init__(self, id, chips):
        self.id = id
        self.chips = chips
        self.hand = []
        self.numAces = 0
        self.handTotal = 0
        self.bust = False
        self.didDouble = False
        self.firstDecision = True
        self.decision = "N"
    def assignCard(self, card):
        self.hand.append(card)
        if card == 1:
            self.numAces += 1
    def newHand(self):
        self.bust = False
        self.didDouble = False
        self.firstDecision = True
        self.sum = 0
        self.hand = []
        self.numAces = 0
        self.handTotal = 0
        self.initalDecision = "N"
    def calculateHandTotal(self):
        self.handTotal = 0
        for card in self.hand:
            if card != 1:
                #ace case
                self.handTotal += card
        if self.numAces > 0:
            if self.handTotal <= 10:
                newTotal = self.handTotal + 11 + (self.numAces-1)*1
                if newTotal <= 21:
                    self.handTotal = newTotal
                else:
                    self.handTotal = self.handTotal + self.numAces*1
            else:
                self.handTotal = self.handTotal + self.numAces*1
        if self.handTotal > 21:
            self.bust = True
    def showHandInfo(self):
        print("Player " + str(self.id) + " hand: " + ' '.join(str(card) for card in self.hand) + " aces: " + str(self.numAces) + " Total: " + str(self.handTotal) + " Decision: " + self.decision)
    def showChips(self):
        print("Chip size: " + str(self.chips))
    def printNumAces(self):
        print("num aces: " + str(self.numAces))
    def setDidDouble(self):
        self.didDouble = True
    #Game Logic
    def makeDecision(self, dealerVisibleCard, playerSoftDeal, playerHardDeal):
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
                #use player hardDeal
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
            #use player hardDeal
        return -1
    def setPlayerDecision(self, decision):
        self.decision = decision