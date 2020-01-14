from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class TestApp(EClient,EWrapper):
    def __init__(self,self):
        EClient.__init__(self,self)
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error")
    def fundamentalData(self, reqId , data):
        print(data)


def main():
    app=TestApp()

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    app.req

if __name__=='__main__':
    main()

