# Performs market buy orders with cases where the opposite orders are either market or limit orders
def market_buy(new_order, sell, last):
    """
    This function performs a market buy order

    new_order: New market order
    sell: Mapping of current sell pending orders
    last: Mapping of the last prices
    return: null
    """
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
                    last[new_order.getStock()] = arr[i].getPrice() 
                    break
            else:
                i+=1



# Performs market sell orders with cases where the opposite orders are either market or limit orders
def market_sell(new_order, buy, last):
    """
    This function performs a market sell order

    new_order: New market order
    sell: Mapping of current buy pending orders
    last: Mapping of the last prices of each stock
    return: null
    """
    i = 0
    if new_order.getStock() in buy:
        arr = buy[new_order.getStock()]
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
                    last[new_order.getStock()] = arr[i].getPrice() 
                    break  
            else:
                i+=1

