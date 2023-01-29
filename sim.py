import game
import sys
import player
from random import randrange
import random
import math

#S is stand, H is hit, D is double, P is split, 
#with 0 ace off deal
dealerUpCard_with17 = ["S" for i in range(10)]
dealerUpCard_with13to16 = ["S" for i in range(5)] + ["H" for i in range(5)]
dealerUpCard_with12 = ["H" for i in range(2)] + ["S" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with11 = ["D" for i in range(9)] + ["H"]
dealerUpCard_with10 = ["D" for i in range(8)] + ["H" for i in range(2)]
dealerUpCard_with9 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with5to8 = ["H" for i in range(10)]

# playerHardDeal = {
#     17: dealerUpCard_with17,
#     16: dealerUpCard_with13to16,
#     12: dealerUpCard_with12,
#     11: dealerUpCard_with11,
#     10: dealerUpCard_with10,
#     9: dealerUpCard_with9,
#     8: dealerUpCard_with5to8
# }
standAll = ["S" for i in range(10)]
hitAll = ["H" for i in range(10)]
playerHardDeal = {
    17: standAll,
    16: standAll,
    12: hitAll,
    11: hitAll,
    10: hitAll,
    9: hitAll,
    8: hitAll
}

#with 1 ace off deal
dealerUpCard_with8to10 = ["S" for i in range(10)]
dealerUpCard_with7 = ["S"] + ["D" for i in range(4)] + ["S" for i in range(2)] + ["H" for i in range(3)]
dealerUpCard_with6 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with4to5 = ["H" for i in range(2)] + ["D" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with2to3 = ["H" for i in range(3)] + ["D" for i in range(2)] + ["H" for i in range(5)]
# playerSoftDeal = {
#     8: dealerUpCard_with8to10,
#     7: dealerUpCard_with7,
#     6: dealerUpCard_with6,
#     5: dealerUpCard_with4to5,
#     3: dealerUpCard_with2to3,
# }
playerSoftDeal = {
    8: standAll,
    7: standAll,
    6: standAll,
    5: hitAll,
    3: hitAll,
}


#dealer decision


def main():
    numPlayers = 3
    totalPlayerArr = []
    numWins = [0,0,0]
    for i in range(numPlayers):
        totalPlayerArr.append([])
    playerChipSize = 100

    percentLow = 8
    playerBetSizeLow = [1,2,3]
    playerBetSizeHigh = [5,8]
    numDecks = 1
    numberTurns = 100
    simulationSets = 100
    simGame = game.Game(numPlayers, numDecks, playerChipSize)
    for s in range(simulationSets):
        for p in simGame.gamePlayers:
            p.resetChipStack()
        for i in range(numberTurns):
            simGame.resetBlackJackDeck()
            simGame.resetAllHands()
            simGame.dealHand()
            #place bets
            for p in simGame.gamePlayers:
                randDraw = random.randint(1,10)
                betSize = 2
                if randDraw <= percentLow:
                    betSize = playerBetSizeLow[randrange(len(playerBetSizeLow))]
                else:
                    betSize = playerBetSizeHigh[randrange(len(playerBetSizeHigh))]
                p.setBetSize(betSize)
                p.reduceChips(p.betSize)
            for p in simGame.gamePlayers:
                decision = p.makeDecision(simGame.gameDealer.showVisibleCard(), playerSoftDeal, playerHardDeal)
                p.setPlayerDecision(decision)  
                while(not p.bust and not p.didDouble and decision != "S"):
                    if(decision == "H"):
                        p.assignCard(simGame.dealCard())
                        p.calculateHandTotal()
                    if decision == "D":
                        p.assignCard(simGame.dealCard())
                        p.calculateHandTotal()
                        p.setDidDouble()
                    decision = p.makeDecision(simGame.gameDealer.showVisibleCard(), playerSoftDeal, playerHardDeal)
                if p.didDouble:
                    p.reduceChips(p.betSize)
            #dealer decision
            simGame.gameDealer.calculateHandTotal()
            dealerDecision = simGame.gameDealer.makeDecision()
            while(not simGame.gameDealer.bust and dealerDecision != "S"):
                if dealerDecision == "H":
                    simGame.gameDealer.assignCard(simGame.dealCard())
                    simGame.gameDealer.calculateHandTotal()
                dealerDecision = simGame.gameDealer.makeDecision()
            #calculate win/loss
            for p in simGame.gamePlayers:
                if not p.bust:
                    if(simGame.gameDealer.bust):
                        p.addChips(2*p.betSize)
                    elif ((p.handTotal > simGame.gameDealer.handTotal) and simGame.gameDealer.handTotal != 21):
                        p.addChips(2*p.betSize)
                    elif (p.handTotal == simGame.gameDealer.handTotal):
                        p.addChips(p.betSize)
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
