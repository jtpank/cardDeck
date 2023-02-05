import game
import sys
import player
import math
import random
import strategy
import hand
playerHardDeal = strategy.playerHardDeal_book
playerSoftDeal = strategy.playerSoftDeal_book
playerPairDeal = strategy.playerPairDeal_book
def main():
    numPlayers = 3
    totalPlayerArr = []
    numWins = []
    for i in range(numPlayers):
        totalPlayerArr.append([])
        numWins.append(0)
    playerChipSize = 100
    percentLow = 9
    playerBetSizeLow = [1,2]
    playerBetSizeHigh = [5,8]
    numDecks = 3
    numberTurns = 100
    simulationSets = 1
    simGame = game.Game(numPlayers, numDecks, playerChipSize)
    for s in range(simulationSets):
        simGame.resetPlayerChips()
        for i in range(numberTurns):
            #reset deck every turn
            if(simGame.deckSize < (52*numDecks)):
                simGame.resetBlackJackDeck()
            simGame.resetAllHands()
            #place bets
            simGame.placePlayerBets(percentLow, playerBetSizeLow, playerBetSizeHigh)
            #deal hand
            simGame.dealHand()
            #take turns
            simGame.takeTurns(playerSoftDeal,playerHardDeal, playerPairDeal)
            for p in simGame.gamePlayers:
                #after dealHand(), guaranteed to have p.hands[0] 
                playerHand = p.hands[0]
                print("Player: " + str(p.id) + ' ' + playerHand.returnHandString() + ' dec: ' + p.decision)
            simGame.gameDealer.hand.calculateHandTotal()
            print("Dealer: " + simGame.gameDealer.hand.returnHandString())
            print()
            #calculate win/loss
            # simGame.calculateWinLoss()
        #print final output
        for x in range(numPlayers):
            totalPlayerArr[x].append(simGame.gamePlayers[x].chips)
    print()
    print("Number of sims: " + str(simulationSets) + " Number of hands per turn: " + str(numberTurns))
    for i in range(numPlayers):
        for x in range(len(totalPlayerArr[i])):
            totalPlayerArr[i][x] -= playerChipSize
            if totalPlayerArr[i][x] > 0:
                numWins[i] += 1
        # + " gain: " + str(totalPlayerArr[i]) + 
        print("Player " + str(i) + " win %: " + str(math.floor((numWins[i]/simulationSets)*100)))

if __name__ == "__main__":
    main()




