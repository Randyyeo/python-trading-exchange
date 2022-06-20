from Market_Order import Market_Order
from Sell_Order import Sell_Order

class Sell_Market_Order(Market_Order, Sell_Order):

    def __init__(self, stock, amount):
        self.action = "SELL"
        self.stock = stock
        self.type = "MKT"
        self.price = None
        self.amount = amount 
        self.current = 0
        self.status = "PENDING"
    
    def execute(self, buy, last):
        """
        This function performs a market sell order

        sell: Mapping of current buy pending orders
        last: Mapping of the last prices of each stock
        return: null
        """
        i = 0
        if self.getStock() in buy:
            arr = buy[self.getStock()]
            while i < len(arr):
                # Assumption made: Only limit orders stored in the exchange will be transacted when a market order is placed
                if arr[i].getType() != "MKT":
                    if self.getRemaining() > arr[i].getRemaining():
                        self.setCurrent(arr[i].getRemaining())
                        arr[i].setCurrent(arr[i].getRemaining())
                        self.setPrice(arr[i].getPrice())    
                        last[self.getStock()] = arr[i].getPrice()
                        arr.pop(i) 
                    else:
                        arr[i].setCurrent(self.getRemaining())
                        self.setCurrent(self.getRemaining())
                        self.setPrice(arr[i].getPrice())
                        last[self.getStock()] = arr[i].getPrice() 
                        break  
                else:
                    i+=1

            