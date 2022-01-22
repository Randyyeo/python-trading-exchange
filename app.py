# data variables
orders = []
status = False
buy = {}
sell = {}
last = {}
mkt_buy_index = 1
mkt_sell_index = 1

# This function sorts the orders in terms of priority. 
# Market orders have the most priority followed by limit orders with highest price for 'buy' and lowest price for 'sell'
def sort(new_order, type, index):
    if type == "sell":
        # Check if stock is in the queue
        if new_order.getStock() not in sell:
            sell[new_order.getStock()] = [new_order]
        else:
            # Check if stock is market or limit order
            arr = sell[new_order.getStock()]
            if new_order.getType() == "MKT":
                arr.insert(index, new_order)
                index +=  1
            else:
                status = False
                # Sorting based on the 'sell' priority mentioned above
                for i in range(len(arr[index:])):
                    if new_order.getPrice() < arr[i].getPrice():
                        status = True
                        arr.insert(i, new_order)
                        break
                if not status:
                    arr.append(new_order)
        return index
    else:
        # Check if stock is in the queue
        if new_order.getStock() not in buy:
            buy[new_order.getStock()] = [new_order]
        else:
            # Check if stock is market or limit order
            arr = buy[new_order.getStock()]
            if new_order.getType() == "MKT":
                arr.insert(index, new_order)
                index +=  1
            else:
                status = False
                # Sorting based on the 'buy' priority mentioned above
                for i in range(len(arr)):
                    if new_order.getPrice() > arr[i].getPrice():
                        arr.insert(i, new_order)
                        status = True
                        break
                if not status:
                    arr.append(new_order)
        return index

# Performs limit orders with cases where the opposite orders are either market or limit orders
def perform_transaction_limit(new_order, type):
    # If the new order is a buy
    if type == "buy":
        i = 0
        if new_order.getStock() in sell:
            arr = sell[new_order.getStock()]
            while i < len(arr):
                if arr[i].getType() == "MKT":
                    # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                    if new_order.getRemaining() > arr[i].getRemaining():
                        new_order.setCurrent(arr[i].getRemaining()) # Set the new order based on the amount of the order stored in exchange
                        arr[i].setCurrent(arr[i].getRemaining()) # Set the order stored in exchange as completed
                        arr[i].setPrice(new_order.getPrice()) # Set price as order stored in exchange
                        last[new_order.getStock()] = new_order.getPrice() # Storing last exchanged price
                        arr.pop(i) # Remove from exchange since it has been completed
                    else:
                        arr[i].setCurrent(new_order.getRemaining()) # Since new order amount is lesser, new order is completed and the loop is broken
                        new_order.setCurrent(new_order.getRemaining())
                        arr[i].setPrice(new_order.getPrice())
                        last[new_order.getStock()] = new_order.getPrice()
                        break

                else:
                    # Order is only executed when buy price is more than sell price
                    if new_order.getPrice() >= arr[i].getPrice():
                        if new_order.getRemaining() > arr[i].getRemaining():
                            new_order.setCurrent(arr[i].getRemaining())
                            arr[i].setCurrent(arr[i].getRemaining())
                            last[new_order.getStock()] = arr[i].getPrice()
                            arr.pop(i)
                        else:
                            arr[i].setCurrent(new_order.getRemaining())
                            new_order.setCurrent(new_order.getRemaining())
                            last[new_order.getStock()] = arr[i].getPrice()
                            break
                    else:
                        break        
    else:
        # If the new order is a sell
        if new_order.getStock() in buy:
            arr = buy[new_order.getStock()]
            i = 0
            while i < len(arr):
                    if arr[i].getType() == "MKT":
                        # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                        if new_order.getRemaining() > arr[i].getRemaining():
                            
                            new_order.setCurrent(arr[i].getRemaining())
                            arr[i].setCurrent(arr[i].getRemaining())
                            arr[i].setPrice(new_order.getPrice())
                            last[new_order.getStock()] = new_order.getPrice()
                            arr.pop(i)
                        else:
                            arr[i].setCurrent(new_order.getRemaining())
                            new_order.setCurrent(new_order.getRemaining())
                            arr[i].setPrice(new_order.getPrice())
                            last[new_order.getStock()] = new_order.getPrice()
                            break
                        
                    else:
                        # Order is only executed when buy price is more than sell price
                        if new_order.getPrice() <= arr[i].getPrice():
                            if new_order.getRemaining() > arr[i].getRemaining():
                                new_order.setCurrent(arr[i].getRemaining())
                                arr[i].setCurrent(arr[i].getRemaining())
                                last[new_order.getStock()] = new_order.getPrice()
                                arr.pop(i)
                            else:
                                arr[i].setCurrent(new_order.getRemaining())
                                new_order.setCurrent(new_order.getRemaining())
                                last[new_order.getStock()] = new_order.getPrice()
                                break
                        else:
                            break
                
def perform_transaction_market(new_order, type):
    # If the new order is a buy
    if type == "buy":
        i = 0
        if new_order.getStock() in sell:
            arr = sell[new_order.getStock()]
            while i < len(arr):
                # Assumption made: Only limit orders stored in the exchange will be transacted when a market order is placed
                if arr[i].getType() != "MKT":   
                    if new_order.getRemaining() > arr[i].getRemaining():
                        new_order.setCurrent(arr[i].getRemaining())
                        arr[i].setCurrent(arr[i].getRemaining())
                        new_order.setPrice(arr[i].getPrice()) 
                        last[new_order.getStock()] = arr[i].getPrice() 
                        arr.pop(i)
                    else:
                        arr[i].setCurrent(new_order.getRemaining())
                        new_order.setCurrent(new_order.getRemaining())
                        new_order.setPrice(arr[i].getPrice())  
                        last[order.getStock()] = arr[i].getPrice() 
                        break
                else:
                    i+=1
    else:
        # If the new order is a sell
        i = 0
        if new_order.getStock() in buy:
            arr = buy[new_order.getStock()]
            while i < len(arr):
                # Assumption made: Only limit orders stored in the exchange will be transacted when a market order is placed
                if arr[i].getType() != "MKT":
                    if new_order.getRemaining() > arr[i].getRemaining():
                        new_order.setCurrent(arr[i].getRemaining())
                        arr[i].setCurrent(arr[i].getRemaining())
                        new_order.setPrice(new_order.getPrice())    
                        last[new_order.getStock()] = arr[i].getPrice()
                        arr.pop(i) 
                    else:
                        arr[i].setCurrent(new_order.getRemaining())
                        new_order.setCurrent(order.getRemaining())
                        new_order.setPrice(new_order.getPrice())
                        last[new_order.getStock()] = arr[i].getPrice() 
                        break  
                else:
                    i+=1
                        

class Order:
    def __init__(self, action, stock, type, price, amount,):
        self.action = action
        self.stock = stock
        self.type = type
        self.price = price
        self.amount = amount 
        self.current = 0
        self.status = "PENDING"

    # Printing out the order placed
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
        
    def getRemaining(self):
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


# Actual block of code run 

while status == False:

    input_string = input("ACTION: ")
    list_str = input_string.split(" ")
    try:
        action = list_str[0]
        # View Orders
        if action == "VIEW":
            i = 1
            for order in orders:
                print(f"{i}. {order.logg()}")
                i += 1
        # Buy Orders        
        elif action == "BUY":
            stock = list_str[1]
            type = list_str[2]
            # Buy Limit Order
            if type == "LMT":
                # Error command validations
                if "$" not in list_str[3] or len(list_str) != 5:
                    print(f"Your limit order is not in the correct format.")
                else:
                    price = round(float(list_str[3][1:]), 2)
                    amount = int(list_str[4])
                    order = Order(action, stock, type, price, amount)
                    perform_transaction_limit(order, "buy")
                    if order.getStatus() != "FILLED":
                        index = sort(order, "buy", mkt_buy_index)
                        mkt_buy_index = index
                    
                    orders.append(order)
                    print(f"You have placed a limit buy order for {amount} {stock} shares at ${price} each")
            # Buy Market Order
            else:
                amount = int(list_str[3])
                order = Order(action, stock, type, None, amount)
                perform_transaction_market(order, "buy")
                        
                if order.getStatus() != "FILLED":
                    index = sort(order, "buy", mkt_buy_index)
                    mkt_buy_index = index
                orders.append(order)
                print(f"You have placed a market order for {amount} {stock} shares")
            
        # Sell Orders
        elif action == "SELL":
            stock = list_str[1]
            type = list_str[2]
            # Sell Limit Order
            if type == "LMT":
                # Error command validations
                if "$" not in list_str[3] or len(list_str) != 5:
                    print(f"Your limit order is not in the correct format.")
                else:
                    price = round(float(list_str[3][1:]), 2)
                    amount = int(list_str[4])
                    order = Order(action, stock, type, price, amount)
                    perform_transaction_limit(order, "sell")
                    if order.getStatus() != "FILLED":
                        index = sort(order, "sell", mkt_sell_index)
                        mkt_sell_index = index
                    orders.append(order)
                    print(f"You have placed a limit sell order for {amount} {stock} shares at ${price} each")
            # Sell Market Order        
            else:
                amount = int(list_str[3])
                order = Order(action, stock, type, None, amount)
                perform_transaction_market(order, "sell")        
                if order.getStatus() != "FILLED":
                    index = sort(order, "sell", mkt_sell_index)
                    mkt_sell_index = index
                orders.append(order)
                print(f"You have placed a market order for {amount} {stock} shares")
            
            
        # Exit Client
        elif action == "QUIT":
            status = True
        # Quote orders    
        elif action == "QUOTE":
            
            stock = list_str[1]
            if stock in buy and len(buy[stock]) != 0:
                if buy[stock][mkt_buy_index].getPrice() != None:
                    bid_price = float(buy[stock][mkt_buy_index].getPrice())
                else:
                    bid_price = "0.00"
            else:
                bid_price = "0.00"
            
            if stock in sell and len(sell[stock]) != 0:
                if sell[stock][mkt_sell_index].getPrice() != None:
                    ask_price = float(sell[stock][mkt_sell_index].getPrice())
                else:
                    ask_price = "0.00"
            else:
                ask_price = "0.00"

            if stock in last:
                last_price = float(last[stock])
            else:
                last_price = "0.00"
            print(f"{stock} BID: ${bid_price} ASK: ${ask_price} LAST: ${last_price}")
        else:
            print("Command not found. Do note that the commands are case sensitive")
        
        print()
    except:
        print("Command not found. Do note that the commands are case sensitive")
    

