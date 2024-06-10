import sys
from scr import ioMix, loadFile, reviewMod

def _init():
    ioMix.clearScreen()
    return loadFile.openJson()

def _chooseFunc():
    print("1. Choose Deck\n2. Start Random Review\n3. Start Review by Tags\n4. Exit")
    while True:
        usChoice = ioMix.getCh()
        if usChoice > '0' and usChoice < '5':
            break
    if usChoice == '4':
        ioMix.clearScreen()
        print("Now exiting the program...")
        sys.exit(0)
    return usChoice

if __name__ == "__main__":
    decks = _init()
    while True:
        ioMix.clearScreen()
        usChoice = _chooseFunc()

        if usChoice == '1':
            deckNameList = []
            for i in range(len(decks[0])):
                deckNameList.append(loadFile.openJson(decks[0][i])["name"])
            pageStartInd = 0
            while True:
                ioMix.clearScreen()
                for i in range(pageStartInd, pageStartInd + 5 if len(decks[1]) >= pageStartInd + 5 else len(decks[1])):
                    deckName = deckNameList[i]
                    print(f"[{'√' if decks[1][i] else ' '}]{i - pageStartInd + 1}. {deckName}")
                selChoice = ' '
                print("\n"
                      "Press Y to select all\n"
                      "Press N to cancel all\n"
                      "Press R to reverse selection\n"
                      "Press Z, / to change pages\n"
                      "Press H to save review habbit\n"
                      "Press Q to back to home\n")
                while True:
                    selChoice = ioMix.getCh()
                    if (selChoice >= '1' and selChoice <= '5') or selChoice in ('y', 'Y', 'n', 'N', 'r', 'R', 'q', 'Q', 'z', 'Z', '/', '?', 'h', 'H'):
                        if selChoice.isdecimal():
                            decks[1][int(selChoice) - 1] = 1 - decks[1][int(selChoice) - 1]
                        elif selChoice in ('y', 'Y'):
                            for i in range(len(decks[1])):
                                decks[1][i] = 1
                        elif selChoice in ('n', 'N'):
                            for i in range(len(decks[1])):
                                decks[1][i] = 0
                        elif selChoice in ('r', 'R'):
                            for i in range(len(decks[1])):
                                decks[1][i] = 1 - decks[1][i]
                        elif selChoice in ('z', 'Z'):
                            if pageStartInd >= 5:
                                pageStartInd -= 5
                        elif selChoice in ('/', '?'):
                            if pageStartInd <= len(decks[1]) - 6:
                                pageStartInd += 5
                        elif selChoice in ('h', 'H'):
                            loadFile.writeHabbit(decks)
                        break
                if selChoice in ('q', 'Q'):
                    break

        elif usChoice == '2':
            while True:
                cardNumStr = input("Number of cards you would like to review(empty for all cards): ")
                if cardNumStr == "" or cardNumStr.isdecimal():
                    break
            if cardNumStr == "":
                cardNumStr = "-1"
            cardNum = int(cardNumStr)
            reviewMod.reviewByNumber(loadFile.mapUsDeck(decks[0], decks[1]), cardNum)

        elif usChoice == '3':
            tagNameList = []
            while True:
                tagName = input("Name of tags you want to review(keep empty to stop input): ")
                if tagName == "":
                    break
                tagNameList.append(tagName)
            reviewMod.reviewByTags(loadFile.mapUsDeck(decks[0], decks[1]), tagNameList)
