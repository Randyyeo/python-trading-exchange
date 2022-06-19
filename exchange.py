import sys
import os

sys.path.append(os.getcwd() + '/classes')
sys.path.append(os.getcwd() + '/helper_functions')

# Helper Functions
from Order import Order  # Order class
from limit_transactions import limit_buy  # Buy limit orders
from limit_transactions import limit_sell  # Sell limit orders
from market_transactions import market_buy  # Buy market orders
from market_transactions import market_sell  # Sell market orders
from sort import sort_buy  # Sort buy queue after each transaction
from sort import sort_sell  # Sort sell queue  after each transaction


# Data variables
orders = []  # Source of Truth for all orders that have been placed
status = False  # Whether the application will stop running

buy = {}  # Mapping containing each different stock and within each stock
            # each order is priced according to their priority (BUY SIDE)

sell = {}  # Mapping containing each different stock within each stock
            # each order is priced according to their priority (SELL SIDE)

last = {}  # Mapping containing each different stock and the prices of
            # the transaction that each stock was last transacted at

mkt_buy_index = {}  # Position of the last price of each stock
mkt_sell_index = {}  # Position of the last price of each stock

# Actual block of code run 

while not status:

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
                    limit_buy(order, sell, last)

                    if order.getStatus() != "FILLED":
                        index = sort_buy(order, mkt_buy_index, buy)
                        mkt_buy_index = index

                    orders.append(order)
                    order.print()

            # Buy Market Order
            else:
                amount = int(list_str[3])
                order = Order(action, stock, type, None, amount)
                market_buy(order, sell, last)  
                if order.getStatus() != "FILLED":
                    index = sort_buy(order, mkt_buy_index, buy)
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
                    order = Order(action, stock, type, price, amount)
                    limit_sell(order, buy, last)
                    if order.getStatus() != "FILLED":
                        index = sort_sell(order, mkt_sell_index, sell)
                        mkt_sell_index = index
                    orders.append(order)
                    order.print()

            # Sell Market Order   
            else:
                amount = int(list_str[3])
                order = Order(action, stock, type, None, amount)
                market_sell(order, buy, last)
                if order.getStatus() != "FILLED":
                    index = sort_sell(order, mkt_sell_index, sell)
                    mkt_sell_index = index
                orders.append(order)
                order.print()

        # Exit Client
        elif action == "QUIT":
            status = True

        # Quote orders
        elif action == "QUOTE":
            stock = list_str[1]
            # Check if the stock exists
            if stock in buy and len(buy[stock]) != 0:
                if buy[stock][mkt_buy_index[stock]].getPrice() != None:
                    bid_price = float(buy[stock][mkt_buy_index[stock]].getPrice())
                else:
                    bid_price = "0.00"
            else:
                bid_price = "0.00"
            
            if stock in sell and len(sell[stock]) != 0:
                if sell[stock][mkt_sell_index[stock]].getPrice() != None:
                    ask_price = float(sell[stock][mkt_sell_index[stock]].getPrice())
                else:
                    ask_price = "0.00"
            else:
                ask_price = "0.00"

            if stock in last:
                last_price = float(last[stock])
            else:
                last_price = "0.00"
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
    

