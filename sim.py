import game
import sys
import player

#with 0 ace off deal
dealerUpCard_with17 = ["S" for i in range(10)]
dealerUpCard_with13to16 = ["S" for i in range(5)] + ["H" for i in range(5)]
dealerUpCard_with12 = ["H" for i in range(2)] + ["S" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with11 = ["D" for i in range(9)] + ["H"]
dealerUpCard_with10 = ["D" for i in range(8)] + ["H" for i in range(2)]
dealerUpCard_with9 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with5to8 = ["H" for i in range(10)]

playerHardDeal = {
    17: dealerUpCard_with17,
    16: dealerUpCard_with13to16,
    12: dealerUpCard_with12,
    11: dealerUpCard_with11,
    10: dealerUpCard_with10,
    9: dealerUpCard_with9,
    8: dealerUpCard_with5to8
}

#with 1 ace off deal
dealerUpCard_with8to10 = ["S" for i in range(10)]
dealerUpCard_with7 = ["S"] + ["D" for i in range(4)] + ["S" for i in range(2)] + ["H" for i in range(3)]
dealerUpCard_with6 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with4to5 = ["H" for i in range(2)] + ["D" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with2to3 = ["H" for i in range(3)] + ["D" for i in range(2)] + ["H" for i in range(5)]
playerSoftDeal = {
    8: dealerUpCard_with8to10,
    7: dealerUpCard_with7,
    6: dealerUpCard_with6,
    5: dealerUpCard_with4to5,
    3: dealerUpCard_with2to3,
}


#dealer decision


def main():
    numPlayers = 3
    playerChipSize = 100
    numDecks = 6
    numberTurns = 1
    simGame = game.Game(numPlayers, numDecks, playerChipSize)
    for i in range(numberTurns):
        simGame.resetBlackJackDeck()
        simGame.resetAllHands()
        simGame.printDeckSize()
        simGame.printNumPlayers()
        simGame.dealHand()
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
        #dealer decision
        simGame.gameDealer.calculateHandTotal()
        dealerDecision = simGame.gameDealer.makeDecision()
        while(not simGame.gameDealer.bust and dealerDecision != "S"):
            if dealerDecision == "H":
                simGame.gameDealer.assignCard(simGame.dealCard())
                simGame.gameDealer.calculateHandTotal()
            dealerDecision = simGame.gameDealer.makeDecision()
        
        #calculate win/loss

        #print output
        simGame.printPlayerHands()
        simGame.printDealerHand()
        simGame.printDeckSize()
        print()
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
