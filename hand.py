class Hand:
    #a hand consists of n cards
    # a player can have Many hands in one turn (but starts with one)
    def __init__(self):
        self.hand = []
        self.numAces = 0
        self.handTotal = 0
        self.bust = False
        self.betSize = 0
    #can assign a card to a hand
    def assignCard(self, card):
        self.hand.append(card)
        if card == 1:
            self.numAces += 1
    #can assign a hand
    def assignSplitHand(self, card):
        if card == 1:
            self.numAces += 1
        self.hand = [card]
    #can get card for split
    def getCard(self):
        if len(self.hand) > 0:
            return self.hand[0]
    def getHandSize(self):
        return len(self.hand)
    #can set a betsize to a hand
    def setBetSize(self, value):
        self.betSize = value
    #calculate the value of the hand
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
    def didHandBust(self):
        return self.bust
    def setBust(self):
        self.bust = True
    def returnHandString(self):
        return str("Hand: " + ' '.join(str(card) for card in self.hand) + " aces: " + str(self.numAces) + " Total: " + str(self.handTotal))
    #can display the card hand info
    def displayHandInfo(self):
        print("Hand: " + ' '.join(str(card) for card in self.hand) + " aces: " + str(self.numAces) + " Total: " + str(self.handTotal))