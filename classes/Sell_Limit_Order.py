from Limit_Order import Limit_Order
from Sell_Order import Sell_Order

class Sell_Limit_Order(Limit_Order, Sell_Order):
    
    def __init__(self, stock, price, amount):
        self.action = "SELL"
        self.stock = stock
        self.type = "LMT"
        self.price = price
        self.amount = amount 
        self.current = 0
        self.status = "PENDING"

    def execute(self, buy, last):
        """
        This function performs a limit sell order

        buy: Mapping of current buy pending orders
        last: Mapping of the last prices
        return: null
        """
        if self.getStock() in buy:
            orders = buy[self.getStock()]
            i = 0
            while i < len(orders):
                if orders[i].getType() == "MKT":
                    # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                    if self.getRemaining() > orders[i].getRemaining():
                        
                        self.setCurrent(orders[i].getRemaining())
                        orders[i].setCurrent(orders[i].getRemaining())
                        orders[i].setPrice(self.getPrice())
                        last[self.getStock()] = self.getPrice()
                        orders.pop(i)
                    else:
                        orders[i].setCurrent(self.getRemaining())
                        self.setCurrent(self.getRemaining())
                        orders[i].setPrice(self.getPrice())
                        last[self.getStock()] = self.getPrice()
                        break
                    
                else:
                    # Order is only executed when buy price is more than sell price
                    # in this case the self(sell) is lower than the buy price e.g. orders[i]
                    if self.getPrice() <= orders[i].getPrice():
                        if self.getRemaining() > orders[i].getRemaining():
                            self.setCurrent(orders[i].getRemaining())
                            orders[i].setCurrent(orders[i].getRemaining())
                            last[self.getStock()] = self.getPrice()
                            orders.pop(i)
                        else:
                            orders[i].setCurrent(self.getRemaining())
                            self.setCurrent(self.getRemaining())
                            last[self.getStock()] = self.getPrice()
                            break
                    else:
                        break    