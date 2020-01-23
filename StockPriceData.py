

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer
import numpy as np

class TestApp(EClient,EWrapper):

    def __init__(self):
        EClient.__init__(self,self)
        self.barsList=[]
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error",errorString)
    def nextValidId(self,reqId):
        self.start()

    def weightedAvg(self, barsList):
        self.weights = np.repeat(1.0, len(barsList)) / len(barsList)
        self.smas = np.convolve(barsList, self.weights, 'valid')
        return self.smas
    def historicalData(self, reqId, bar):
        avg=(bar.low+bar.high)/2
        self.barsList.append(avg)
        print(self.weightedAvg(self.barsList))

    def historicalDataEnd(self,reqId,start,end):
        print("HistoricalDataEnd")
    def start(self):
        contract = Contract()
        contract.symbol = "TGP PRb"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"

        self.reqHistoricalData(1, contract, "", "26 W", "1 day", "MIDPOINT", 0, 1, False, [])


    def stop(self):

        self.done=True
        self.disconnect()



def main():

    app=TestApp()
    app.nextOrderId=0
    app.connect("127.0.0.1", 7497, 0)
    Timer(10000,app.stop).start()
    app.run()

    TestApp

if __name__=="__main__":
    main()
