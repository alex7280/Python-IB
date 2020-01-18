from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from openpxyl import Workbook
from threading import Timer

class TestApp(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print(reqId, "error")

    def tickString(self,tickerId,field,value):
        empty.append(value)
    def nextValidId(self, orderId):
        self.nextOrderId=orderId
        self.start()
    def start(self):
        contract=Contract()
        contract.symbol = "TGP"
        contract.secType = "INDUSTRIAL"
        contract.exchange = "SMART"
        contract.currency = "USD"

        order=Order()
        order.action="Buy"
        order.totalQuantity=400
        order.orderType="MKT"

        self.placeOrder(self.nextOrderId,contract,order)

    def stop(self):
        self.done=True
        self.disconnect









def main():
    app = TestApp()
    app.nextOrderId=0
    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "TGP"
    contract.secType = "INDUSTRIAL"
    contract.exchange = "SMART"
    contract.currency = "USD"

    empty = []

    Dividend_Pershare=app.reqMktData(1,contract,'258',True,False,['TTMDIVSHR'])
    Asset=app.reqMktData(1,contract,'258',False,False,['AATCA'])
    EBITDA=app.reqMktData(1,contract,'258',False,False,['QEBITDA'])
    NetDebt=app.reqMktData(1,contract,'258',False,False,['AFPRD'])
    ShortDebt=app.reqMktData(1,contract,'258',False,False,['ALSTD'])




    Dividend_Pershare =empty[0]
    Asset=empty[1]
    EBITDA=empty[2]
    LongDebt=empty[3]-empty[4]

    start = datetime.datetime(2020, 1, 10)
    end = datetime.datetime.now()
    barsList = []

    endtime = end
    while endtime > start:
        contract.symbol="TGP PrA"
        bars = app.reqHistoricalData(1, contract, "", "26 W", "1 day", "MIDPOINT", 0, 1, False, [])
        barsList.append(bars)
        contract.symbol="TGP PrB"
        bars = app.reqHistoricalData(1, contract, "", "26 W", "1 day", "MIDPOINT", 0, 1, False, [])
        endtime = bars[0].date

    app = TestApp()
    dividend = app.reqMktData(1, contract, '258', true, false, ['TTMDIVSHR'])

    NewBarsList = []
    for bars in barsList:
        for b in bars:
            c = dividend / b
            NewBarsList.append(c)
    df = util.df(NewBarsList)

    def movingaverage(values, window):
        weights = np.repeat(1.0, window) / window
        smas = np.convolve(values, weights, 'valid')
        return smas

    if Dividend_Pershare<movingaverage(df,len(df)):
        Timer(3,app.stop).start()
    app.run()








