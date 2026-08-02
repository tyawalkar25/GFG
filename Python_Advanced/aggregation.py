# Example of aggregation: a stock broker can be associated with multiple fund houses,
# but the fund houses are independent objects that can exist on their own.

class Stock_Broker:
    def __init__(self,name):
        self.__name : str = name
        self.__fund_house : list[Fund_House] = None

    def get_name(self) -> str:
        return self.__name

    def add_fund_house(self, fundhouse : "Fund_House") -> None:
        if self.__fund_house is None:
            self.__fund_house = []
        self.__fund_house.append(fundhouse)

    def get_stock_broker_fund_house(self) -> None:
        if self.__fund_house is None:
            print(f"{self.get_name()} has no associated fund houses.")
            return
        for f in self.__fund_house:
            print(f"{self.get_name()} is associated with {f.get_name()}")



class Fund_House:
    def __init__(self,name):
        self.__name : str = name

    def get_name(self) -> str:
        return self.__name


zerodha = Stock_Broker("Zerodha")
fund_house1 = Fund_House("HDFC")
fund_house2 = Fund_House("ICICI")

zerodha.add_fund_house(fund_house1)
zerodha.add_fund_house(fund_house2)
zerodha.get_stock_broker_fund_house()
        