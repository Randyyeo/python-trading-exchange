# Performs limit buy orders with cases where the opposite orders are either market or limit orders
def limit_buy(new_order, sell, last):
    """
    This function performs a limit buy order

    new_order: New limit order
    sell: Mapping of current sell pending orders
    last: Mapping of the last prices
    return: null
    """
    i = 0
    if new_order.getStock() in sell:
        orders = sell[new_order.getStock()]
        while i < len(orders):
            if orders[i].getType() == "MKT":
                # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                if new_order.getRemaining() > orders[i].getRemaining():
                    new_order.setCurrent(orders[i].getRemaining()) # Set the new order based on the amount of the order stored in exchange
                    orders[i].setCurrent(orders[i].getRemaining()) # Set the order stored in exchange as completed
                    orders[i].setPrice(new_order.getPrice()) # Set price as order stored in exchange
                    last[new_order.getStock()] = new_order.getPrice() # Storing last exchanged price
                    orders.pop(i) # Remove from exchange since it has been completed
                else:
                    orders[i].setCurrent(new_order.getRemaining()) # Since new order amount is lesser, new order is completed and the loop is broken
                    new_order.setCurrent(new_order.getRemaining())
                    orders[i].setPrice(new_order.getPrice())
                    last[new_order.getStock()] = new_order.getPrice()
                    break

            else:
                # Order is only executed when buy price is more than sell price
                # in this case the new_order(buy) is more than the sell price e.g. orders[i]
                if new_order.getPrice() >= orders[i].getPrice():
                    if new_order.getRemaining() > orders[i].getRemaining():
                        new_order.setCurrent(orders[i].getRemaining())
                        orders[i].setCurrent(orders[i].getRemaining())
                        last[new_order.getStock()] = orders[i].getPrice()
                        orders.pop(i)
                    else:
                        orders[i].setCurrent(new_order.getRemaining())
                        new_order.setCurrent(new_order.getRemaining())
                        last[new_order.getStock()] = orders[i].getPrice()
                        break
                else:
                    break  

# Performs limit sell orders with cases where the opposite orders are either market or limit orders
def limit_sell(new_order, buy, last):
    """
    This function performs a limit sell order

    new_order: New limit order
    buy: Mapping of current buy pending orders
    last: Mapping of the last prices
    return: null
    """
    if new_order.getStock() in buy:
        orders = buy[new_order.getStock()]
        i = 0
        while i < len(orders):
            if orders[i].getType() == "MKT":
                # Transaction takes place but breaks when new order amount is less than the order amount in the queue 
                if new_order.getRemaining() > orders[i].getRemaining():
                    
                    new_order.setCurrent(orders[i].getRemaining())
                    orders[i].setCurrent(orders[i].getRemaining())
                    orders[i].setPrice(new_order.getPrice())
                    last[new_order.getStock()] = new_order.getPrice()
                    orders.pop(i)
                else:
                    orders[i].setCurrent(new_order.getRemaining())
                    new_order.setCurrent(new_order.getRemaining())
                    orders[i].setPrice(new_order.getPrice())
                    last[new_order.getStock()] = new_order.getPrice()
                    break
                
            else:
                # Order is only executed when buy price is more than sell price
                # in this case the new_order(sell) is lower than the buy price e.g. orders[i]
                if new_order.getPrice() <= orders[i].getPrice():
                    if new_order.getRemaining() > orders[i].getRemaining():
                        new_order.setCurrent(orders[i].getRemaining())
                        orders[i].setCurrent(orders[i].getRemaining())
                        last[new_order.getStock()] = new_order.getPrice()
                        orders.pop(i)
                    else:
                        orders[i].setCurrent(new_order.getRemaining())
                        new_order.setCurrent(new_order.getRemaining())
                        last[new_order.getStock()] = new_order.getPrice()
                        break
                else:
                    break    