from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from datetime import datetime
import numpy as np



class TestApp(EClient,EWrapper):

    def __init__(self,self):
        EClient.__init__(self,self)
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error")
    def historicalData(self, reqId, bar):
        print(reqId, bar)


def main():
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    start = datetime.datetime(2020, 1, 10)
    end = datetime.datetime.now()
    barsList = []

    endtime=end
    while endtime>start:
        app.reqHistoricalData(1,contract,"","1 D","1 hour","MIDPOINT",0,1,False,[])
        barsList.append(bars)
        endtime= bars[0].date

    allBars = [b for bars in barsList for b in bars]
    df = util.df(allBars)
    print(df)
    app.run()
    def movingaverage(values,window):
        weights=np.repeat(1.0,window)/window
        smas=np.convolve(values,weights,'valid')
        return smas
    print movingaverage(df,len(df))

if __name__=='__main__':
    main()