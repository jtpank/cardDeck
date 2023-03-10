#S is stand, H is hit, D is double, P is split, 
#with 0 ace off deal
dealerUpCard_with17 = ["S" for i in range(10)]
dealerUpCard_with13to16 = ["S" for i in range(5)] + ["H" for i in range(5)]
dealerUpCard_with12 = ["H" for i in range(2)] + ["S" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with11 = ["D" for i in range(9)] + ["H"]
dealerUpCard_with10 = ["D" for i in range(8)] + ["H" for i in range(2)]
dealerUpCard_with9 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with5to8 = ["H" for i in range(10)]

#with 1 ace off deal
dealerUpCard_with8to10 = ["S" for i in range(10)]
dealerUpCard_with7 = ["S"] + ["D" for i in range(4)] + ["S" for i in range(2)] + ["H" for i in range(3)]
dealerUpCard_with6 = ["H"] + ["D" for i in range(4)] + ["H" for i in range(5)]
dealerUpCard_with4to5 = ["H" for i in range(2)] + ["D" for i in range(3)] + ["H" for i in range(5)]
dealerUpCard_with2to3 = ["H" for i in range(3)] + ["D" for i in range(2)] + ["H" for i in range(5)]

standAll = ["S" for i in range(10)]
hitAll = ["H" for i in range(10)]

playerHardDeal_book = {
    17: dealerUpCard_with17,
    16: dealerUpCard_with13to16,
    12: dealerUpCard_with12,
    11: dealerUpCard_with11,
    10: dealerUpCard_with10,
    9: dealerUpCard_with9,
    8: dealerUpCard_with5to8
}
playerSoftDeal_book = {
    8: dealerUpCard_with8to10,
    7: dealerUpCard_with7,
    6: dealerUpCard_with6,
    5: dealerUpCard_with4to5,
    3: dealerUpCard_with2to3,
}
playerHardDeal_custom = {
    17: standAll,
    16: standAll,
    12: hitAll,
    11: hitAll,
    10: hitAll,
    9: hitAll,
    8: hitAll
}
playerSoftDeal_custom = {
    8: standAll,
    7: standAll,
    6: standAll,
    5: hitAll,
    3: hitAll,
}

