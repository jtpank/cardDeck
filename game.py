import player
import dealer
import hand
from random import randrange
import random

class Game:
    def __init__(self, numPlayers, numDecks, playerChips):
        self.gameDealer = dealer.Dealer()
        self.gamePlayers = [player.Player(i, playerChips) for i in range(numPlayers)]
        self.numPlayers = numPlayers
        self.numDecks = numDecks
        self.deck = []
        self.deckSize = 0
    def dealHandPair(self, pairCard):
        #deal 2 cards to each player and to the dealer from the deck
        for i in range(2):
            #assign first/second card to each player
            for p in self.gamePlayers:
                playerHand = hand.Hand()
                playerHand = p.hands[0]
                playerHand.assignCard(pairCard)
            #assign first/second card to dealer
            self.gameDealer.hand.assignCard(self.dealCard())
        for p in self.gamePlayers:
            for h in p.hands:
                h.calculateHandTotal()
    def dealHand(self):
        #deal 2 cards to each player and to the dealer from the deck
        for i in range(2):
            #assign first/second card to each player
            for p in self.gamePlayers:
                playerHand = hand.Hand()
                playerHand = p.hands[0]
                playerHand.assignCard(self.dealCard())
            #assign first/second card to dealer
            self.gameDealer.hand.assignCard(self.dealCard())
        for p in self.gamePlayers:
            for h in p.hands:
                h.calculateHandTotal()
    def resetBlackJackDeck(self):
        self.deck = []
        self.deckSize = 0
        for sz in range(self.numDecks):
            #ace through 9
            for i in range(9):
                for j in range(4):
                    #append each value 4 times
                    #aces are value 11
                    if i == 0:
                        self.deck.append(1)
                    else:
                        self.deck.append(i+1)
            for i in range(16):
                #append 4 x 10, J, Q, K which are all 10
                self.deck.append(10)
        self.deckSize = len(self.deck)
        self.shuffleDeck()
    def resetAllHands(self):
        for p in self.gamePlayers:
            p.newHand()
        self.gameDealer.newHand()   
    def resetPlayerChips(self):
        for p in self.gamePlayers:
            p.resetChipStack()
    def shuffleDeck(self):
        random.shuffle(self.deck)
    def dealCard(self):
        #deals the card on the top of the deck
        if self.deckSize == 0:
            return -1
        cardDealt = self.deck[0]
        self.deck.pop(0)
        self.deckSize -= 1; 
        return cardDealt
    def placePlayerBets(self, percentLow, playerBetSizeLow, playerBetSizeHigh):
        for p in self.gamePlayers:
            randDraw = random.randint(1,10)
            betSize = 1
            if randDraw <= percentLow:
                betSize = playerBetSizeLow[randrange(len(playerBetSizeLow))]
            else:
                betSize = playerBetSizeHigh[randrange(len(playerBetSizeHigh))]
            p.setBetSize(betSize)
            p.reduceChips(p.betSize)
    def takeTurns(self, playerSoftDeal, playerHardDeal, playerPairDeal):
        #make player decisions
        visibleCard = self.gameDealer.showVisibleCard()
        for p in self.gamePlayers:
            #each player takes their turn
            #make first player decision
            decision = p.makeDecision(0,visibleCard, playerSoftDeal, playerHardDeal, playerPairDeal)
            p.updateDecisionTree(decision, 0)
            #while all hands are NOT completed
            idx = p.currentHandIndex
            while not p.allHandsAreComplete:
                if idx+1 > len(p.hands):
                    p.setAllHandsAreComplete()
                else:
                    while(not p.hands[idx].didHandBust() and not p.hands[idx].didDouble and p.decision[idx][(len(p.decision[idx])-1)] != "S"):
                        if len(p.hands[idx].hand) == 1:
                            p.hands[idx].assignCard(self.dealCard())
                            p.hands[idx].calculateHandTotal()
                            decision = p.makeDecision(idx, visibleCard, playerSoftDeal, playerHardDeal, playerPairDeal)
                            p.updateDecisionTree(decision, idx)
                        else:
                            if(decision == "H"):
                                #Player decides to HIT
                                p.hands[idx].assignCard(self.dealCard())
                                p.hands[idx].calculateHandTotal()
                                decision = p.makeDecision(idx, visibleCard, playerSoftDeal, playerHardDeal, playerPairDeal)
                                p.updateDecisionTree(decision, idx)
                            elif decision == "D":
                                #player decides to double down
                                p.hands[idx].assignCard(self.dealCard())
                                p.hands[idx].calculateHandTotal()
                                p.hands[idx].setDidDouble()
                                p.reduceChips(p.betSize)
                            elif decision == "P":
                                p.splitCurrentHand(idx)
                                p.hands[idx].assignCard(self.dealCard())
                                p.hands[idx].calculateHandTotal()
                                decision = p.makeDecision(idx, visibleCard, playerSoftDeal, playerHardDeal, playerPairDeal)
                                p.updateDecisionTree(decision, idx)
                idx += 1
        # #next make dealer decision
        self.gameDealer.hand.calculateHandTotal()
        dealerDecision = self.gameDealer.makeDecision()
        while(not self.gameDealer.bust and dealerDecision != "S"):
            if dealerDecision == "H":
                self.gameDealer.hand.assignCard(self.dealCard())
                self.gameDealer.hand.calculateHandTotal()
            dealerDecision = self.gameDealer.makeDecision()
        return
    def calculateWinLoss(self):
        for p in self.gamePlayers:
            for hand in p.hands:
                if not hand.bust:
                    #dealer bust
                    if(self.gameDealer.hand.bust):
                        p.addChips(2*p.betSize)
                    #player beat dealer
                    elif ((hand.handTotal > self.gameDealer.hand.handTotal) and self.gameDealer.hand.handTotal != 21):
                        if hand.didDouble:
                            p.addChips(4*p.betSize)
                        else:
                            p.addChips(2*p.betSize)
                    #player push
                    elif (hand.handTotal == self.gameDealer.hand.handTotal):
                        if hand.didDouble:
                            p.addChips(2*p.betSize)
                        else:
                            p.addChips(p.betSize)
        return
    def printPlayerChipSizes(self):
        for p in self.gamePlayers:
            p.printChipSize()
    def printDeck(self):
        print(' '.join(str(card) for card in self.deck))
    def printDeckSize(self):
        print("deck size: " + str(self.deckSize))
    def printNumPlayers(self):
        print("numPlayers: " + str(self.numPlayers))
    def printPlayerHands(self):
        for p in self.gamePlayers:
            p.showHandInfo()
    def printDealerHand(self):
        self.gameDealer.showHandInfo()