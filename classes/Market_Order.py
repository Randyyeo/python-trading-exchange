from Order import Order

class Market_Order(Order):
    
    def print(self):
        print(f"You have placed a market order for {self.amount} {self.stock} shares")
        
    