from datetime import datetime
from BinanceAPI import BinanceAPI

def drawSquare(width, height):
    borderBottomLeft = chr(9565)
    borderWidth = chr(9552)
    borderheight = chr(9567)
    width = width * 2
    finalTable = []
    for h in range(height):
        line = ""
        for w in range(width):
            if h == height - 1:
                if w == width - 1:
                    line += borderBottomLeft
                else:
                    line += borderWidth
            else:
                if w == width - 1:
                    line += borderheight
                else:
                    line += " "

        finalTable.append(line)
    return finalTable

def getLimits(candles):
    higher = round(candles[0][2], 4)
    lower = round(candles[0][3], 4)
    for c in candles:
        if c[2] > higher:
            higher = c[2]
        elif c[3] < lower:
            lower = c[3]

    lower = round(lower * 10000)
    higher = round(higher * 10000)
    while (lower % 5 != 0 or higher % 10 != 0):
        if (lower % 5):
            lower -= 1
        elif (higher % 10):
            higher += 1
    return [round(higher), round(lower)]

api = BinanceAPI()
candles = api.getCandles("CHZUSDT", "1m")
lenC = len(candles)
candles = [[float(x) for x in c[0:6]] for c in candles[lenC - 50: lenC]]
lenC = len(candles)

print(datetime.fromtimestamp(int(candles[lenC - 1][0])/1000))
limits = getLimits(candles)
emptyTable = drawSquare(lenC, (limits[0] - limits[1]))

monoStickBottom = chr(9589)
monoStickTop = chr(9591)
doubleStick = chr(9474)

doubleBlock = chr(9608)
topBlock = chr(9604)
bottomBlock = chr(9600)

for i in range(limits[1], limits[0]):
    pos = limits[1] - (i - limits[1]) + (limits[0] - limits[1] - 1)
    printable = False
    if i != (limits[0] - 1):
        printable = True
    i = i - limits[1]
    nbr = " " + str(pos)
    emptyTable[i] = emptyTable[i] + nbr
    if printable:
        char = ""
        for c in range(0, len(emptyTable[i])):
            lenTable = len(emptyTable[i]) - 6
            linePrice = int(pos)/10000
            if c < lenTable and c % 2 == 0 and candles[round(c/2)][2] >= linePrice and candles[round(c/2)][3] <= linePrice:
                char += doubleStick
            else:
                char += emptyTable[i][c]
        #print((int(char[-4:])/10000))
        print(char)
    else:
        print(emptyTable[i])
