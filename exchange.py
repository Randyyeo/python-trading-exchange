import sys
import os

sys.path.append(os.getcwd() + '/classes')
sys.path.append(os.getcwd() + '/helper_functions')

# Order classes
from Buy_Market_Order import Buy_Market_Order
from Sell_Market_Order import Sell_Market_Order
from Buy_Limit_Order import Buy_Limit_Order
from Sell_Limit_Order import Sell_Limit_Order 

# Helper functions
from quote_orders import quote_orders

# Data variables
orders = []  # Source of Truth for all orders that have been placed
status = False  # Whether the application will stop running

buy = {}  # Mapping containing each different stock and within each stock
            # each order is priced according to their priority (BUY SIDE)

sell = {}  # Mapping containing each different stock within each stock
            # each order is priced according to their priority (SELL SIDE)

last = {}  # Mapping containing each different stock and the prices of
            # the transaction that each stock was last transacted at

mkt_buy_index = {}  # Position of the bid price of each stock
mkt_sell_index = {}  # Position of the ask price of each stock

# Actual block of code run 

while not status:
    try:
        input_string = input("ACTION: ")
        list_str = input_string.split(" ")
        
        action = list_str[0]

        # View Orders
        if action == "VIEW":
            i = 1
            for order in orders:
                print(f"{i}. {order.view()}")
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
                    order = Buy_Limit_Order(stock, price, amount)
                    order.execute(sell, last)

                    if order.getStatus() != "FILLED":
                        index = order.sort(mkt_buy_index, buy)
                        mkt_buy_index = index

                    orders.append(order)
                    order.print()

            # Buy Market Order
            else:
                amount = int(list_str[3])
                order = Buy_Market_Order(stock, amount)
                order.execute(sell, last)  

                if order.getStatus() != "FILLED":
                    index = order.sort(mkt_buy_index, buy)
                    mkt_buy_index = index
                orders.append(order)
                order.print()

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
                    order = Sell_Limit_Order(stock, price, amount)
                    order.execute(buy, last)
                    if order.getStatus() != "FILLED":
                        index = order.sort(mkt_sell_index, sell)
                        mkt_sell_index = index
                    orders.append(order)
                    order.print()

            # Sell Market Order   
            else:
                amount = int(list_str[3])
                order = Sell_Market_Order(stock, amount)
                order.execute(buy, last)
                if order.getStatus() != "FILLED":
                    index = order.sort(mkt_sell_index, sell)
                    mkt_sell_index = index
                orders.append(order)
                order.print()

        # Exit Client
        elif action == "QUIT":
            status = True

        # Quote orders
        elif action == "QUOTE":
            stock = list_str[1]

            bid_price, ask_price, last_price = quote_orders(stock, 
                                                        buy, 
                                                        mkt_buy_index, 
                                                        sell, 
                                                        mkt_sell_index, 
                                                        last)

            print(f"{stock} BID: ${bid_price} " +   
                f"ASK: ${ask_price} LAST: ${last_price}")
        else:
            print("Command not found. Do note" +
                "that the commands are case sensitive")
            print()
        
        print()
    except:
        print("Command not found. Do note that the commands are case sensitive")
        print() 
    

