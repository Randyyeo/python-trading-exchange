from Limit_Order import Limit_Order
from Buy_Order import Buy_Order

class Buy_Limit_Order(Limit_Order, Buy_Order):
    
    def execute(self, sell, last):
        """
        This function performs a limit buy order

        sell: Mapping of current sell pending orders
        last: Mapping of the last prices
        return: null
        """
        i = 0
        if self.getStock() in sell:
            orders = sell[self.getStock()]
            while i < len(orders):
                if orders[i].getType() == "MKT":
                    # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                    if self.getRemaining() > orders[i].getRemaining():
                        self.setCurrent(orders[i].getRemaining()) # Set the new order based on the amount of the order stored in exchange
                        orders[i].setCurrent(orders[i].getRemaining()) # Set the order stored in exchange as completed
                        orders[i].setPrice(self.getPrice()) # Set price as order stored in exchange
                        last[self.getStock()] = self.getPrice() # Storing last exchanged price
                        orders.pop(i) # Remove from exchange since it has been completed
                    else:
                        orders[i].setCurrent(self.getRemaining()) # Since new order amount is lesser, new order is completed and the loop is broken
                        self.setCurrent(self.getRemaining())
                        orders[i].setPrice(self.getPrice())
                        last[self.getStock()] = self.getPrice()
                        break

                else:
                    # Order is only executed when buy price is more than sell price
                    # in this case the self(buy) is more than the sell price e.g. orders[i]
                    if self.getPrice() >= orders[i].getPrice():
                        if self.getRemaining() > orders[i].getRemaining():
                            self.setCurrent(orders[i].getRemaining())
                            orders[i].setCurrent(orders[i].getRemaining())
                            last[self.getStock()] = orders[i].getPrice()
                            orders.pop(i)
                        else:
                            orders[i].setCurrent(self.getRemaining())
                            self.setCurrent(self.getRemaining())
                            last[self.getStock()] = orders[i].getPrice()
                            break
                    else:
                        break  

                