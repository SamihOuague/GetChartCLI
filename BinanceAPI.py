import requests

class BinanceAPI:
    def __init__(self):
        self.url = "https://api.binance.com/api/v3"

    def getCandles(self, symbol, period = "1m", start = ""):
        url = self.url + "/klines?symbol={}&interval={}".format(symbol, period)
        if start != "":
            url = url + "&startTime={}".format(start)
        return requests.get(url).json()

    def ticker(self, symbol = "CHZUSDT"):
        return requests.get(self.url + "/ticker/price?symbol="+symbol).json()