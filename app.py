
orders = []
status = False
buy = {}
sell = {}
bid = {}
ask = {}
last = {}

def sort(new_order, type):
    if type == "sell":
        if new_order.getStock() not in sell:
            sell[new_order.getStock()] = [new_order]
        else:
            arr = sell[new_order.getStock()]
            if new_order.getType() == "MKT":
                arr.insert(0, new_order)
            else:
                
                for i in range(len(arr)):
                    if new_order.getPrice() < arr[i].getPrice():
                        arr.insert(i, new_order)
                
                if new_order.getStock() not in ask:
                    ask[new_order.getStock()] = new_order.getPrice()
                else:
                    if ask[new_order.getStock()] > new_order.getPrice():
                        ask[new_order.getStock()] = new_order.getPrice()
    else:
        if new_order.getStock() not in buy:
            buy[new_order.getStock()] = [new_order]
        else:
            arr = buy[new_order.getStock()]
            if new_order.getType() == "MKT":
                arr.insert(0, new_order)
            else:
                
                for i in range(len(arr)):
                    if new_order.getPrice() > arr[i].getPrice():
                        arr.insert(i, new_order)
                if new_order.getStock() not in bid:
                    bid[new_order.getStock()] = new_order.getPrice()
                else:
                    if bid[new_order.getStock()] < new_order.getPrice():
                        bid[new_order.getStock()] = new_order.getPrice()

def perform_transaction(new_order, type):
    if type == "buy":
        i = 0
        if new_order.getStock() in sell:
            arr = sell[new_order.getStock()]
            while i < len(arr):
                
                    if arr[i].getPrice() == None:
                        if new_order.getAmount() >= arr[i].getAmount():
                            new_order.setCurrent(arr[i].getAmount())
                            arr[i].setCurrent(arr[i].getAmount())
                            arr[i].setPrice(new_order.getPrice())
                            
                            last[new_order.getStock()] = new_order.getPrice()
                            
                            arr.pop(i)
                        else:
                            arr[i].setCurrent(new_order.getAmount())
                            new_order.setCurrent(new_order.getAmount())
                            arr[i].setPrice(new_order.getPrice())
                            last[new_order.getStock()] = new_order.getPrice()
                            break
                        
                    else:
                        if new_order.getPrice() >= arr[i].getPrice():
                            if new_order.getAmount() >= arr[i].getAmount():
                                new_order.setCurrent(arr[i].getAmount())
                                arr[i].setCurrent(arr[i].getAmount())
                                
                                last[new_order.getStock()] = arr[i].getPrice()
                                arr.pop(i)
                            else:
                                arr[i].setCurrent(new_order.getAmount())
                                new_order.setCurrent(new_order.getAmount())
                                last[new_order.getStock()] = arr[i].getPrice()
                                break
                        else:
                            break
            
    else:
        if new_order.getStock() in buy:
            arr = buy[new_order.getStock()]
            i = 0
            
            while i < len(arr):
                
                
                    if arr[i].getPrice() == None:
                        if new_order.getAmount() >= arr[i].getAmount():
                            
                            new_order.setCurrent(arr[i].getAmount())
                            arr[i].setCurrent(arr[i].getAmount())
                            arr[i].setPrice(new_order.getPrice())
                            last[new_order.getStock()] = new_order.getPrice()
                            arr.pop(i)
                        else:
                            arr[i].setCurrent(new_order.getAmount())
                            new_order.setCurrent(new_order.getAmount())
                            arr[i].setPrice(new_order.getPrice())
                            last[new_order.getStock()] = new_order.getPrice()
                            break
                        
                    else:
                        if new_order.getPrice() <= arr[i].getPrice():
                            if new_order.getAmount() >= arr[i].getAmount():
                                new_order.setCurrent(arr[i].getAmount())
                                arr[i].setCurrent(arr[i].getAmount())
                                last[new_order.getStock()] = new_order.getPrice()
                                arr.pop(i)
                            else:
                                arr[i].setCurrent(new_order.getAmount())
                                new_order.setCurrent(new_order.getAmount())
                                last[new_order.getStock()] = new_order.getPrice()
                                break
                        else:
                            break
                

class Order:
    def __init__(self, action, stock, type, price, amount,):
        self.action = action
        self.stock = stock
        self.type = type
        self.price = price
        self.amount = amount 
        self.current = 0
        self.status = "PENDING"

    def logg(self):
        if self.price == None:
            return f"{self.action} {self.stock} {self.type} {self.current}/{self.amount} {self.status}"
        else:
            return f"{self.action} {self.stock} {self.type} ${str(self.price)} {self.current}/{self.amount} {self.status}"
    def getCurrent(self):
        return self.current

    def setCurrent(self, result):
        
        self.current += result
        if self.current == self.amount:
            self.status = "FILLED"
        elif self.current > 0:
            self.status = "PARTIAL"
        
    def getAmount(self):
        return self.amount - self.current

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status
    
    def setPrice(self, result):
        self.price = result

    def getStock(self):
        return self.stock


while status == False:

    input_string = input()
    list_str = input_string.split(" ")
    action = list_str[0]
    if action == "VIEW":
        i = 1
        for order in orders:
            print(f"{i}. {order.logg()}")
            i += 1
            
    elif action == "BUY":
        stock = list_str[1]
        type = list_str[2]
        if type == "LMT":
            price = round(float(list_str[3][1:]), 2)
            amount = int(list_str[4])
            order = Order(action, stock, type, price, amount)
            perform_transaction(order, "buy")
            if order.getStatus() != "FILLED":
                sort(order, "buy")
            
            orders.append(order)
            print(f"You have placed a limit buy order for {amount} {stock} shares at ${price} each")
        else:
            amount = int(list_str[3])
            order = Order(action, stock, type, None, amount)
            i = 0
            if order.getStock() in sell:
                arr = sell[order.getStock()]
                while i < len(arr):
                        
                    if order.getAmount() >= arr[i].getAmount():
                        arr[i].setCurrent(arr[i].getAmount())
                        order.setCurrent(arr[i].getAmount())
                        order.setPrice(arr[i].getPrice()) 
                        last[order.getStock()] = arr[i].getPrice() 
                        arr.pop(i)
                    else:
                        arr[i].setCurrent(order.getAmount())
                        order.setCurrent(order.getAmount())
                        order.setPrice(arr[i].getPrice())  
                        last[order.getStock()] = arr[i].getPrice() 
                        break
                    
                     
            if order.getStatus() != "FILLED":
                sort(order, "buy")
            orders.append(order)
            print(f"You have placed a market order for {amount} {stock} shares")
        

    elif action == "SELL":
        stock = list_str[1]
        type = list_str[2]
        if type == "LMT":
            price = round(float(list_str[3][1:]), 2)
            amount = int(list_str[4])
            order = Order(action, stock, type, price, amount)
            perform_transaction(order, "sell")
            if order.getStatus() != "FILLED":
                sort(order, "sell")
            orders.append(order)
            print(f"You have placed a limit sell order for {amount} {stock} shares at ${price} each")
        else:
            amount = int(list_str[3])
            order = Order(action, stock, type, None, amount)
            i = 0
            if order.getStock() in buy:
                arr = buy[order.getStock()]
                while i < len(arr):
                        
                            if order.getAmount() >= arr[i].getAmount():
                                arr[i].setCurrent(arr[i].getAmount())
                                order.setCurrent(arr[i].getAmount())
                                order.setPrice(order.getPrice())    
                                last[order.getStock()] = arr[i].getPrice()
                                arr.pop(i) 
                            else:
                                arr[i].setCurrent(order.getAmount())
                                order.setCurrent(order.getAmount())
                                order.setPrice(order.getPrice())
                                last[order.getStock()] = arr[i].getPrice() 
                                break  
                    
            if order.getStatus() != "FILLED":
                sort(order, "sell")
            orders.append(order)
            print(f"You have placed a market order for {amount} {stock} shares")
        
        

    elif action == "QUIT":
        status = True
        print("Exit")
    elif action == "QUOTE":
        
        stock = list_str[1]
        if stock in buy and len(buy[stock]) != 0:
            bid_price = float(buy[stock][0].getPrice())
        else:
            bid_price = "0.00"
        
        if stock in sell and len(sell[stock]) != 0:
            ask_price = float(sell[stock][0].getPrice())
        else:
            ask_price = "0.00"

        if stock in last:
            last_price = float(last[stock])
        else:
            last_price = "0.00"
        print(f"{stock} BID: ${bid_price} ASK: ${ask_price} LAST: ${last_price}")
    else:
        print("Command not found. Do note that the commands are case sensitive")
    
    
    

