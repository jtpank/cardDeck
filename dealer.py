class Dealer:
    def __init__(self):
        self.hand = []
        self.bust = False
        self.handTotal = 0
        self.numAces = 0
    def gotBlackjack(self):
        return False 
    def assignCard(self, card):
        self.hand.append(card)
    def newHand(self):
        self.bust = False
        self.hand = []
        self.handTotal = 0
        self.numAces = 0
    def makeDecision(self):
        if self.handTotal >= 17:
            return "S"
        else:
            return "H"
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
    def showVisibleCard(self):
        #only show players visible card
        return self.hand[0]
    def showHandInfo(self):
        print("Dealer hand: " + ' '.join(str(card) for card in self.hand) + " aces: " + str(self.numAces) + " Total: " + str(self.handTotal))