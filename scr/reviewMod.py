import random
import copy
import json
from . import ioMix, loadFile

def loadDecks(decks, cmd = 1, cmdPara = []):
    res = []
    fullDecks = {}
    for i in decks:
        cardCnt = 0

        loadingDeckJson = loadFile.openJson(i)
        fullDecks[i] = loadingDeckJson
        loadingDeckName = loadingDeckJson["name"]
        print(f"Loading {loadingDeckName}")

        for eachCard in loadingDeckJson["cards"]:
            flg = 0
            if cmd == 1:
                flg = cmd
            elif cmd == 2:
                if set(eachCard["tag"]) & set(cmdPara) != set():
                    flg = 1

            if flg:
                eachCard["from"] = i
                eachCard["cnt"] = cardCnt
                res.append(eachCard)

            cardCnt += 1

    return (res, fullDecks)

def reviewBase(orderList, cardsJson, fullDecks):
    changeLog = []
    opFullDecks = copy.deepcopy(fullDecks)

    for i in orderList:
        ioMix.clearScreen()
        print(cardsJson[i]["text"]["front"])
        print("\n"
              "Press Q to show hint\n"
              "Press W to show answer\n"
              "Press E to skip\n")
        while True:
            usChoice = ioMix.getCh()
            if usChoice in ('e', 'E'):
                break
            if usChoice in ('q', 'Q'):
                ioMix.clearScreen()
                print(cardsJson[i]["text"]["front"])
                print(cardsJson[i]["text"]["hint"])
                print("\n"
                      "Press Q to show hint\n"
                      "Press W to show answer\n"
                      "Press E to skip\n")
            elif usChoice in ('w', 'W'):
                while True:
                    ioMix.clearScreen()
                    print(cardsJson[i]["text"]["front"])
                    print(cardsJson[i]["text"]["hint"])
                    print(cardsJson[i]["text"]["back"])
                    for j in range(len(cardsJson[i]["tag"])):
                        if j > 0:
                            print(", ", end = "")
                        print(cardsJson[i]["tag"][j], end = "")
                    print("\n\n"
                          "Press Q to put tags for the card\n"
                          "Press W to delete tags for the card\n"
                          "Press R to see next card\n")
                    nextWill = ' '
                    while True:
                        nextWill = ioMix.getCh()
                        if nextWill in ('r', 'R'):
                            break
                        elif nextWill in ('q', 'Q'):
                            newTagName = input("Enter tag name(keep empty to cancel): ")
                            if newTagName == "":
                                break
                            tagList = opFullDecks[cardsJson[i]["from"]]["cards"][cardsJson[i]["cnt"]]["tag"]
                            tagList.append(newTagName)
                            cardsJson[i]["tag"].append(newTagName)
                            if not cardsJson[i]["from"] in changeLog:
                                changeLog.append(cardsJson[i]["from"])
                            break
                        elif nextWill in ('w', 'W'):
                            delTagName = input("Enter tag name(keep empty to cancel): ")
                            if delTagName == "":
                                break
                            if delTagName in cardsJson[i]["tag"]:
                                tagList = opFullDecks[cardsJson[i]["from"]]["cards"][cardsJson[i]["cnt"]]["tag"]
                                tagList.pop(tagList.index(delTagName))
                                cardsJson[i]["tag"].pop(cardsJson[i]["tag"].index(delTagName))
                                if not cardsJson[i]["from"] in changeLog:
                                    changeLog.append(cardsJson[i]["from"])
                            else:
                                print(f"The card has no tag named {delTagName}. Press any key to continue...")
                                ioMix.getCh()
                            break
                    if nextWill in ('r', 'R'):
                        break
                break

    if len(changeLog) > 0:
        for key in changeLog:
            deckCards = opFullDecks[key]
            for itCard in deckCards["cards"]:
                itCard.pop("cnt")
                itCard.pop("from")
            file = open(key, "w", encoding = "utf-8")
            file.write(json.dumps(opFullDecks[key], indent=4, separators=(",", ": ")))

def reviewByNumber(decks, cardNum):
    decksLoad = loadDecks(decks)
    cardsJson = decksLoad[0]
    fullDecks = decksLoad[1]
    if cardNum == -1:
        cardNum = len(cardsJson)
    orderList = [i for i in range(len(cardsJson))]
    random.shuffle(orderList)
    reviewBase(orderList[:cardNum], cardsJson, fullDecks)

def reviewByTags(decks, tagList):
    decksLoad = loadDecks(decks, 2, tagList)
    cardsJson = decksLoad[0]
    fullDecks = decksLoad[1]
    orderList = [i for i in range(len(cardsJson))]
    random.shuffle(orderList)
    reviewBase(orderList, cardsJson, fullDecks)
