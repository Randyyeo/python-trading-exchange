import sys
import os
import pytest
sys.path.append(os.getcwd() + '/../classes')
sys.path.append(os.getcwd() + '/../helper_functions')

# Helper Functions
from Order import Order # Order class
from limit_transactions import limit_buy, limit_sell # Functions for selling/buying limit orders
from market_transactions import market_buy, market_sell # Functions for selling/buying market orders
from sort import sort_buy, sort_sell # Sorting the buying and selling queue after each transaction

def test_get_correct_bid_price_with_two_market_orders_then_two_limit_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_buy_index = {}  
    

    buy_market_one = Order("BUY", "FB", "MKT", None, 5)
    buy_market_two = Order("BUY", "FB", "MKT", None, 10)
    buy_limit_one = Order("BUY", "FB", "LMT", 20.00, 5)
    buy_limit_two = Order("BUY", "FB", "LMT", 30.00, 10)

    market_buy(buy_market_one, sell, last)
    sort_buy(buy_market_one, mkt_buy_index, buy)

    market_buy(buy_market_two, sell, last)
    sort_buy(buy_market_two, mkt_buy_index, buy)

    limit_buy(buy_limit_one, sell, last)
    sort_buy(buy_limit_one, mkt_buy_index, buy)

    limit_buy(buy_limit_two, sell, last)
    sort_buy(buy_limit_two, mkt_buy_index, buy)

    assert buy["FB"][mkt_buy_index["FB"]].getPrice() == 30
    

def test_get_correct_ask_price_with_two_market_orders_then_two_limit_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_sell_index = {}

    sell_market_one = Order("BUY", "FB", "MKT", None, 5)
    sell_market_two = Order("BUY", "FB", "MKT", None, 10)
    sell_limit_one = Order("BUY", "FB", "LMT", 20.00, 5)
    sell_limit_two = Order("BUY", "FB", "LMT", 30.00, 10)

    market_sell(sell_market_one, buy, last)
    sort_sell(sell_market_one, mkt_sell_index, sell)

    market_sell(sell_market_two, buy, last)
    sort_sell(sell_market_two, mkt_sell_index, sell)

    limit_sell(sell_limit_one, buy, last)
    sort_sell(sell_limit_one, mkt_sell_index, sell)

    limit_sell(sell_limit_two, buy, last)
    sort_sell(sell_limit_two, mkt_sell_index, sell)

    assert sell["FB"][mkt_sell_index["FB"]].getPrice() == 20
    