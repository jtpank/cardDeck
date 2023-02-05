import player
import dealer
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
    def dealHand(self):
        #deal 2 cards to each player and to the dealer from the deck
        for i in range(2):
            #assign first/second card to each player
            for p in self.gamePlayers:
                p.assignCard(self.dealCard())
            #assign first/second card to dealer
            self.gameDealer.assignCard(self.dealCard())
        for p in self.gamePlayers:
            p.calculateHandTotal()
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
        for p in self.gamePlayers:
            decision = p.makeDecision(self.gameDealer.showVisibleCard(), playerSoftDeal, playerHardDeal, playerPairDeal)
            p.setPlayerDecision(decision)  
            while(not p.bust and not p.didDouble and decision != "S"):
                if(decision == "H"):
                    #Player decides to HIT
                    p.assignCard(self.dealCard())
                    p.calculateHandTotal()
                    decision = p.makeDecision(self.gameDealer.showVisibleCard(), playerSoftDeal, playerHardDeal, playerPairDeal)
                elif decision == "D":
                    #player decides to double down
                    p.assignCard(self.dealCard())
                    p.calculateHandTotal()
                    p.setDidDouble()
                    p.reduceChips(p.betSize)
                # elif decision == "SP":
                #     #split decision tree
        #next make dealer decision
        self.gameDealer.calculateHandTotal()
        dealerDecision = self.gameDealer.makeDecision()
        while(not self.gameDealer.bust and dealerDecision != "S"):
            if dealerDecision == "H":
                self.gameDealer.assignCard(self.dealCard())
                self.gameDealer.calculateHandTotal()
            dealerDecision = self.gameDealer.makeDecision()
        return
    def calculateWinLoss(self):
        for p in self.gamePlayers:
            if not p.bust:
                #dealer bust
                if(self.gameDealer.bust):
                    p.addChips(2*p.betSize)
                #player beat dealer
                elif ((p.handTotal > self.gameDealer.handTotal) and self.gameDealer.handTotal != 21):
                    if p.didDouble:
                        p.addChips(4*p.betSize)
                    else:
                        p.addChips(2*p.betSize)
                #player push
                elif (p.handTotal == self.gameDealer.handTotal):
                    if p.didDouble:
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