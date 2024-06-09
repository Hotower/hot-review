import sys
from scr import ioMix, loadFile, reviewMod

def _init():
    ioMix.clearScreen()
    return loadFile.openJson()

def _chooseFunc():
    print("1. Choose Deck\n2. Start Random Review\n3. Start Review by Tags\n4. Exit")
    while True:
        usChoice = ioMix.getCh()
        if usChoice in ('1', '2', '3', '4'):
            break
    if usChoice == '4':
        ioMix.clearScreen()
        print("Now exiting the program...")
        sys.exit(0)
    return usChoice

if __name__ == "__main__":
    DECKS = _init()
    usDeck = [1 for i in DECKS]
    while True:
        ioMix.clearScreen()
        usChoice = _chooseFunc()

        if usChoice == '1':
            ioMix.clearScreen()
            for i in range(len(DECKS)):
                deckName = loadFile.openJson(DECKS[i])["name"]
                print(f"[{'√' if usDeck[i] else ' '}]: {deckName}")
            print("\nPress Any Key to Continue...")
            ioMix.getCh()

        elif usChoice == '2':
            while True:
                cardNumStr = input("Number of cards you would like to review(empty for all cards): ")
                if cardNumStr == "" or cardNumStr.isdecimal():
                    break
            if cardNumStr == "":
                cardNumStr = "-1"
            cardNum = int(cardNumStr)
            reviewMod.reviewByNumber(loadFile.mapUsDeck(DECKS, usDeck), cardNum)
