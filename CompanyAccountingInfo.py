from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class TestApp(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self,self)
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error")
    def tickString(self,tickerId,field,value):
        print(value)


def main():
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "TGP"
    contract.secType = "INDUSTRIAL"
    contract.exchange = "SMART"
    contract.currency = "USD"

    Dividend_Pershare=app.reqMktData(1,contract,'258',True,False,['TTMDIVSHR'])
    Asset=app.reqMktData(1,contract,'258',False,False,['AATCA'])
    EBITDA=app.reqMktData(1,contract,'258',False,False,['QEBITDA'])
    NetDebt=app.reqMktData(1,contract,'258',False,False,['AFPRD'])
    ShortDebt=app.reqMktData(1,contract,'258',False,False,['ALSTD'])


    LongDebt = NetDebt - ShortDebt
    

    app.run()
    



if __name__=='__main__':
    main()

