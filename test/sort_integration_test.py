import sys
import os
import pytest
sys.path.append(os.getcwd() + '/../classes')
sys.path.append(os.getcwd() + '/../helper_functions')

# Order classes
from Buy_Market_Order import Buy_Market_Order
from Sell_Market_Order import Sell_Market_Order
from Buy_Limit_Order import Buy_Limit_Order
from Sell_Limit_Order import Sell_Limit_Order

def test_get_correct_bid_price_with_two_market_orders_then_two_limit_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_buy_index = {}  
    
    buy_market_one = Buy_Market_Order("FB", 5)
    buy_market_two = Buy_Market_Order("FB", 10)
    buy_limit_one = Buy_Limit_Order("FB", 20.00, 5)
    buy_limit_two = Buy_Limit_Order("FB", 30.00, 10)

    buy_market_one.execute(sell, last)
    buy_market_one.sort(mkt_buy_index, buy)

    buy_market_two.execute(sell, last)
    buy_market_two.sort(mkt_buy_index, buy)

    buy_limit_one.execute(sell, last)
    buy_limit_one.sort(mkt_buy_index, buy)

    buy_limit_two.execute(sell, last)
    buy_limit_two.sort(mkt_buy_index, buy)

    assert buy["FB"][mkt_buy_index["FB"]].getPrice() == 30
    

def test_get_correct_ask_price_with_two_market_orders_then_two_limit_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_sell_index = {}

    sell_market_one = Sell_Market_Order("FB", 5)
    sell_market_two = Sell_Market_Order("FB", 10)
    sell_limit_one = Sell_Limit_Order("FB", 20.00, 5)
    sell_limit_two = Sell_Limit_Order("FB", 30.00, 10)

    sell_market_one.execute(buy, last)
    sell_market_one.sort(mkt_sell_index, sell)

    sell_market_two.execute(buy, last)
    sell_market_two.sort(mkt_sell_index, sell)

    sell_limit_one.execute(buy, last)
    sell_limit_one.sort(mkt_sell_index, sell)

    sell_limit_two.execute(buy, last)
    sell_limit_two.sort(mkt_sell_index, sell)

    assert sell["FB"][mkt_sell_index["FB"]].getPrice() == 20
    
def test_no_bid_price_with_two_market_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_buy_index = {}  
    
    buy_market_one = Buy_Market_Order("FB", 5)
    buy_market_two = Buy_Market_Order("FB", 10)

    buy_market_one.execute(sell, last)
    buy_market_one.sort(mkt_buy_index, buy)

    buy_market_two.execute(sell, last)
    buy_market_two.sort(mkt_buy_index, buy)

    assert len(buy["FB"]) == mkt_buy_index["FB"]

def test_no_ask_price_with_two_market_orders():
    buy = {}
    sell = {}
    last = {}
    mkt_sell_index = {}  
    
    sell_market_one = Sell_Market_Order("FB", 5)
    sell_market_two = Sell_Market_Order("FB", 10)

    sell_market_one.execute(buy, last)
    sell_market_one.sort(mkt_sell_index, sell)

    sell_market_two.execute(buy, last)
    sell_market_two.sort(mkt_sell_index, sell)

    assert len(sell["FB"]) == mkt_sell_index["FB"]