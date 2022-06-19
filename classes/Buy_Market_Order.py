from Market_Order import Market_Order
from Buy_Order import Buy_Order

class Buy_Market_Order(Market_Order, Buy_Order):
    
    def execute(self, sell, last):
        """
        This function performs a market buy order

        sell: Mapping of current sell pending orders
        last: Mapping of the last prices
        return: null
        """
        i = 0
        if self.getStock() in sell:
            arr = sell[self.getStock()]
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
            