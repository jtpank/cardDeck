import hand
class Player:
    def __init__(self, id, chips):
        self.id = id
        self.chips = chips
        self.chipMax = chips
        self.hands = [hand.Hand()]
        self.didDouble = False
        self.firstDecision = True
        self.decision = [[]]
        self.numTimesSplit = 0
        self.allHandsAreComplete = False
        self.betSize = 0
        self.currentHandIndex = 0
    def resetChipStack(self):
        self.chips = self.chipMax
    def newHand(self):
        self.hands = [hand.Hand()]
        self.didDouble = False
        self.firstDecision = True
        self.decision = [[]]
        self.numTimesSplit = 0
        self.allHandsAreComplete = False
        self.currentHandIndex = 0
    def setBetSize(self, value):
        self.betSize = value
    def addChips(self, value):
        self.chips += value
    def reduceChips(self, value):
        self.chips -= value
    def showInfo(self, idx):
        print("Player " + str(self.id) + " Decision: " + str(self.decision[idx]) + " Chips: " + str(self.chips))
    def printChipSize(self):
        print("Player " + str(self.id) + " Chip size: " + str(self.chips))
    def setDidDouble(self):
        self.didDouble = True
    def setAllHandsAreComplete(self):
        self.allHandsAreComplete = True
    def splitCurrentHand(self, idx):
        card = self.hands[idx].getCard()
        self.hands[idx].assignSplitHand(card)
        newHand = hand.Hand()
        newHand.assignCard(card)
        self.hands.insert(idx+1,newHand)
        self.decision.insert(idx+1, ["P"])
        #hands[i] is a hand obj that has hand = [4,4]
        #and hands needs to become hands[i] = [4,newCard], hands[i+1] = [4, newCard]
        #TODO: must assign the next split hand to the next position NOT append
        # if you split, then split, you have to keep track of where that split occured
        # can only have 1 split hadn at a time
        return

    #Game Logic
    #make a decision for a single hand (2 cards)
    #returns a decision of:
    # "S" for stand, "D" for double down
    # "SP" for split, "H" for hit      
    def makeDecision(self, playerHandIdx, dealerVisibleCard, playerSoftDeal, playerHardDeal, playerPairDeal):
        #can hit or stand based off visible card
        #implement basic strategy
        if not self.hands[playerHandIdx].didHandBust():
            initialIndex = dealerVisibleCard
            if dealerVisibleCard == 1:
                initialIndex = 11
            #must be 0-9 for the lookup array
            idx = initialIndex - 2
            if self.firstDecision:
                self.firstDecision = False
                #if paired hand
                if self.hands[playerHandIdx].hand[0] == self.hands[playerHandIdx].hand[1]:
                    card = self.hands[playerHandIdx].hand[0]
                    return playerPairDeal[card][idx]
                else:
                    tot = self.hands[playerHandIdx].handTotal
                    if self.hands[playerHandIdx].numAces > 0:
                        #use player softDeal
                        otherCard = (self.hands[playerHandIdx].handTotal - 11)
                        return playerSoftDeal[otherCard][idx]
                    else:
                        return playerHardDeal[tot][idx]
            else:
                tot = self.hands[playerHandIdx].handTotal
                return playerHardDeal[tot][idx]
        else:
            return "B"


    def updateDecisionTree(self, decision, idx):
        self.decision[idx].append(decision)
    #reset player decision for the current hand
    def resetPlayerDecisions(self):
        self.didDouble = False
        self.firstDecision = True
        self.decision = [[]]