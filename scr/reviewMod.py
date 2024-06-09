import random
from . import ioMix, loadFile

def loadDecks(decks):
    res = []
    for i in decks:
        loadingDeckJson = loadFile.openJson(i)
        loadingDeckName = loadingDeckJson["name"]
        print(f"Loading {loadingDeckName}")
        for j in loadingDeckJson["cards"]:
            res.append(j)
    return res

def reviewByNumber(decks, cardNum):
    cardsJson = loadDecks(decks)
    if cardNum == -1:
        cardNum = len(cardsJson)
    orderList = [i for i in range(cardNum)]
    random.shuffle(orderList)
    for i in orderList:
        ioMix.clearScreen()
        print(cardsJson[i]["text"]["front"])
        print("\nPress Q to show hint\nPress W to show answer\nPress E to skip")
        while True:
            usChoice = ioMix.getCh()
            if usChoice in ('e', 'E'):
                break
            if usChoice in ('q', 'Q'):
                ioMix.clearScreen()
                print(cardsJson[i]["text"]["front"])
                print(cardsJson[i]["text"]["hint"])
                print("\nPress Q to show hint\nPress W to show answer\nPress E to skip")
            elif usChoice in ('w', 'W'):
                ioMix.clearScreen()
                print(cardsJson[i]["text"]["front"])
                print(cardsJson[i]["text"]["back"])
                print("\nPress R to see next card.")
                while True:
                    nextWill = ioMix.getCh()
                    if nextWill in ('r', 'R'):
                        break
                break
