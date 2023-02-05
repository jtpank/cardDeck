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
    percentLow = 8
    playerBetSizeLow = [1,2]
    playerBetSizeHigh = [5,8]
    numDecks = 3
    numberTurns = 10
    simulationSets = 5
    simGame = game.Game(numPlayers, numDecks, playerChipSize)
    # NOTE: TODO: Players are allowed to double after split
    # NOTE: TODO: Players are allowed to split Aces AGAIN!
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
            # for p in simGame.gamePlayers:
            #     #after dealHand(), guaranteed to have p.hands[0]
            #     # print("Player: " + str(p.id) + " chips: " + str(p.chips))
            #     for i in range(len(p.hands)):
            #         print("Player: " + str(p.id) + ' ' + p.hands[i].returnHandString() + ' decisions: ' + str(p.decision[i]) + " bet: " + str(p.betSize))
            simGame.gameDealer.hand.calculateHandTotal()
            # print("Dealer: " + simGame.gameDealer.hand.returnHandString())
            #calculate win/loss
            simGame.calculateWinLoss()
            # for p in simGame.gamePlayers:
            #     print("Player: " + str(p.id) + " chips: " + str(p.chips))
            # print()
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
        print()
        print("Player " + str(i) + " gain: " + str(totalPlayerArr[i]))
        print("Player " + str(i) + " win %: " + str(math.floor((numWins[i]/simulationSets)*100)) + " total: " + str(sum(totalPlayerArr[i])))
if __name__ == "__main__":
    main()




