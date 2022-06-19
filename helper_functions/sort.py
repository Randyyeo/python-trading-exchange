# These functions sort the orders in terms of priority. 
# Market orders have the most priority followed by limit orders with highest price for 'buy' and lowest price for 'sell'
def sort_buy(new_order, index, buy):
    """
    This function performs a sorting of the buy pending orders in order of priority

    new_order: New order
    index: Index at which to add in the market order since market orders always get fulfilled first
    buy: Mapping of the buy pending orders
    return: null
    """
    
    stock = new_order.getStock()
    if stock not in index:
        index[stock] = 1 # One order in the buy pending orders
    # Check if stock is in the queue
    if stock not in buy:
        buy[stock] = [new_order]
    else:
        # Check if stock is market or limit order
        arr = buy[stock]
        if new_order.getType() == "MKT":
            arr.insert(index[stock], new_order)
            index[stock] +=  1
        else:
            status = False
            # Sorting based on the 'buy' priority mentioned above
            
            for i in range(index[stock], len(arr)):
                
                if new_order.getPrice() > arr[i].getPrice():
                    arr.insert(i, new_order)
                    status = True
                    break
            if not status:
                arr.append(new_order)
    return index

def sort_sell(new_order, index, sell):
    """
    This function performs a sorting of the sell pending orders in order of priority

    new_order: New order
    index: Index at which to add in the market order since market orders always get fulfilled first
    buy: Mapping of the sell pending orders
    return: null
    """
    stock = new_order.getStock()
    # Check if stock has been ordered before
    if stock not in index:
        index[stock] = 1 # one stock in the sell pending orders
    # Check if stock is in the queue
    if stock not in sell:
        sell[stock] = [new_order]
    else:
        # Check if stock is market or limit order
        arr = sell[stock]
        if new_order.getType() == "MKT":
            arr.insert(index[stock], new_order)
            index[stock] +=  1
        else:
            status = False
            # Sorting based on the 'sell' priority mentioned above
            for i in range(index[stock], len(arr)):
                if new_order.getPrice() < arr[i].getPrice():
                    status = True
                    arr.insert(i, new_order)
                    break
            if not status:
                arr.append(new_order)
    return index