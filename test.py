from datetime import datetime
from typing import final
from BinanceAPI import BinanceAPI

def drawSquare(width, height):
    borderTopLeft = chr(9559)
    borderTopRight = chr(9556)
    borderBottomLeft = chr(9565)
    borderBottomRight = chr(9562)
    borderWidth = chr(9552)
    borderheight = chr(9553)
    width = width * 2
    finalTable = []
    for h in range(height):
        line = ""
        for w in range(width):
            if h == 0:
                if w == 0:
                    line += borderTopRight
                elif w == width - 1:
                    line += borderTopLeft
                else:
                    line += borderWidth
            elif h == height - 1:
                if w == 0:
                    line += borderBottomRight
                elif w == width - 1:
                    line += borderBottomLeft
                else:
                    line += borderWidth
            else:
                if w == 0 or w == width - 1:
                    line += borderheight
                else:
                    line += " "

        finalTable.append(line)
    return finalTable

api = BinanceAPI()
candles = api.getCandles("CHZUSDT", "1m")
lenC = len(candles)
candles = [[float(x) for x in c[0:6]] for c in candles[lenC - 15: lenC]]
emptyTable = drawSquare(60, 20)

print(datetime.fromtimestamp(int(candles[0][0])/1000))

for e in emptyTable:
    print(e)