import game
import sys
import player
import math
import random
import strategy

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
    simulationSets = 100
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
            #calculate win/loss
            simGame.calculateWinLoss()
        #print final output
        for x in range(numPlayers):
            totalPlayerArr[x].append(simGame.gamePlayers[x].chips)
        # print("Set number: " + str(s))
        # simGame.printPlayerChipSizes()
        # simGame.printPlayerHands()
        # simGame.printDealerHand()
        # simGame.printDeckSize()
    print(random.randint(1,10))
    print()
    print("Number of sims: " + str(simulationSets) + " Number of hands per turn: " + str(numberTurns))
    for i in range(numPlayers):
        for x in range(len(totalPlayerArr[i])):
            totalPlayerArr[i][x] -= playerChipSize
            if totalPlayerArr[i][x] > 0:
                numWins[i] += 1
        # + " gain: " + str(totalPlayerArr[i]) + 
        print("Player " + str(i) + " win %: " + str(math.floor((numWins[i]/simulationSets)*100)))
    # p1 = player.Player(0, 100)
    # for i in range(3):
    #     p1.assignCard(1)
    # p1.assignCard(9)
    # p1.assignCard(10)
    # p1.calculateHandTotal()
    # p1.showHandInfo()
    # for k in playerHardDeal.keys():
    #     print(str(k) + "\t" + str(playerHardDeal[k]))
    # for k in playerSoftDeal.keys():
    #     print(str(k) + "\t" + str(playerSoftDeal[k]))

if __name__ == "__main__":
    main()
