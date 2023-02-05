import hand
class Dealer:
    def __init__(self):
        self.hand = hand.Hand()
    def gotBlackjack(self):
        return False 
    def newHand(self):
        self.bust = False
        self.hand = hand.Hand()
    def makeDecision(self):
        if self.hand.handTotal >= 17:
            return "S"
        else:
            return "H"
    def calculateHandTotal(self):
        self.hand.handTotal = 0
        for card in self.hand.hand:
            if card != 1:
                #ace case
                self.hand.handTotal += card
        if self.hand.numAces > 0:
            if self.hand.handTotal <= 10:
                newTotal = self.hand.handTotal + 11 + (self.hand.numAces-1)*1
                if newTotal <= 21:
                    self.hand.handTotal = newTotal
                else:
                    self.hand.handTotal = self.hand.handTotal + self.hand.numAces*1
            else:
                self.hand.handTotal = self.hand.handTotal + self.hand.numAces*1
        if self.hand.handTotal > 21:
            self.hand.bust = True    
    def showVisibleCard(self):
        #only show players visible card
        #getCard returns the 0 index card
        return self.hand.getCard()
    