import ast
import json
from . import ioMix

def safeEval(expression):
    try:
        res = ast.literal_eval(expression)
        return res
    except (SyntaxError, ValueError):
        return 0
    
def mapUsDeck(allDecks, usDeck):
    res = []
    for i in range(len(usDeck)):
        if usDeck[i]:
            res.append(allDecks[i])
    return res

def openJson(fileName = "decks.json"):
    file = open(fileName, "r", encoding = "utf-8")
    res = safeEval(file.read())
    return res

def writeHabbit(deckHabbit):
    file = open("decks.json", "w", encoding = "utf-8")
    file.write(ioMix.formatListPrint(deckHabbit))

if __name__ == "__main__":
    print(openJson())