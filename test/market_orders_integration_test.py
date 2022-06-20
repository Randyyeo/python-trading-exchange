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

# Testing when trader is placing a buy order

def test_buy_one_market_sell_one_limit():
    """
    Purpose: Testing how a market buy order will react with one limit sell order
    Result: Buy order will be processed with 0 remaining units
    """
    sell = {}
    last = {}
    buy_order = Buy_Market_Order("FB", 5)
    sell_order = Sell_Limit_Order("FB", 20.00, 10)
    sell["FB"] = [sell_order]
    
    buy_order.execute(sell, last)  
    
    assert buy_order.getRemaining() == 0
    assert sell_order.getRemaining() == 5
    assert buy_order.getPrice() == 20
    

def test_buy_two_market_sell_none():
    """
    Purpose: Testing how two market buy orders will react with no sell orders
    Result: Buy orders will not be processed
    """
    sell = {}
    last = {}
    buy_order = Buy_Market_Order("FB", 5)
    buy_order_two = Buy_Market_Order("FB", 10)
    
    buy_order.execute(sell, last)
    buy_order_two.execute(sell, last)
    
    assert buy_order.getRemaining() == 5
    assert buy_order_two.getRemaining() == 10
    assert buy_order.getPrice() == None
    assert buy_order_two.getPrice() == None
    

# Testing whenn a trader is trying to place a sell order, similar test cases to the above, 
# just that now the roles are switched

def test_sell_one_market_buy_one_limit():
    buy = {}
    last = {}
    sell_order = Sell_Market_Order("FB", 5)
    buy_order = Buy_Limit_Order("FB", 20.00, 10)
    buy["FB"] = [buy_order]
    
    sell_order.execute(buy, last)  
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5
    assert sell_order.getPrice() == 20

def test_sell_two_market_buy_none_limit():
    buy = {}
    last = {}
    sell_order = Sell_Market_Order("FB", 5)
    sell_order_two = Sell_Market_Order("FB", 10)
    
    sell_order.execute(buy, last)  
    sell_order_two.execute(buy, last) 
    
    assert sell_order.getRemaining() == 5
    assert sell_order_two.getRemaining() == 10
    assert sell_order.getPrice() == None
    assert sell_order_two.getPrice() == None
