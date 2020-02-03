from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer
from openpyxl import Workbook
import getpass

class TestApp(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self,self)
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error",errorString)
    def nextValidId(self,reqId):
        self.start()
    def intodict(self,list):
        d = dict(t.split('=') for t in list.split(';') if t)
        return d

    def tickString(self, tickerId, field, value):
        if field==47:
            self.dict=self.intodict(value)
            self.EBITDA=self.dict['QEBITDA']
            self.Asset=self.dict['AATCA']
            self.DividendYield=self.dict['YIELD']
            self.LongTermDebt = float(self.dict['AFPRD']) - float(self.dict['ALSTD'])
            self.ExpensePreferred=float(self.dict['AFPSS'])*float(self.dict['TTMDIVSHR'])

            print("EBITDA",self.EBITDA,
                  "Asset",self.Asset,
                  "Dividend yield of common share",self.DividendYield,
                  "Long Term Debt",self.LongTermDebt,
                  "Expense on preferred stock dividend",self.ExpensePreferred)
            self.empty_list=[]
            self.empty_list.append(self.EBITDA)
            self.empty_list.append(self.Asset)
            self.empty_list.append(self.DividendYield)
            self.empty_list.append(self.LongTermDebt)
            self.empty_list.append(self.ExpensePreferred)
            wb = Workbook()
            ws1 = wb.active
            ws1.title = "Accounting Info"



            ws1.append(self.empty_list)
            wb.save('D:\\TWS API\\source\\pythonclient\\ibapi\\Accounting Info TGP.xlsx')

        elif field==59:
            a=value.split(",")
            self.stock_date=a[2]
            self.stock_sum_dividend=a[1]
            print(self.stock_date,self.stock_sum_dividend)

            self.empty_list_new=[]
            self.empty_list_new.append(self.stock_date)
            self.empty_list_new.append(self.stock_sum_dividend)

            wb = Workbook()
            ws1 = wb.active
            ws1.title = "Dividend Info"

            ws1.append(self.empty_list_new)
            wb.save('D:\\TWS API\\source\\pythonclient\\ibapi\\Dividend Info TGP.xlsx')



        else:
            print('error')

    def start(self):
        contract = Contract()
        contract.symbol = "TGP"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"
        self.reqMarketDataType(4)
        self.reqMktData(1,contract,'258,456',False,False,[])

    def stop(self):
        self.done=True
        self.disconnect()


def main():
    app = TestApp()
    app.nextOrderId = 0
    app.connect("127.0.0.1", 7497, 0)
    Timer(10000, app.stop).start()


    app.run()
    



if __name__=='__main__':
    main()

