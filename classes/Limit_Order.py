from Order import Order

class Limit_Order(Order):
    
    def print(self):
        dot_index = str(self.price).find(".")
        if len(str(self.price)[dot_index+1:]) == 1:
            print(f"You have placed a limit order for {self.amount} {self.stock} shares at ${self.price}0 each")
        else:
            print(f"You have placed a limit order for {self.amount} {self.stock} shares at ${self.price} each")
        