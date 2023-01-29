import player
import dealer
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