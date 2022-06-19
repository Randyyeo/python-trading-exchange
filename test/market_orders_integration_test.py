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

# Testing when trader is placing a buy order

def test_buy_one_market_sell_one_limit():
    """
    Purpose: Testing how a market buy order will react with one limit sell order
    Result: Buy order will be processed with 0 remaining units
    """
    sell = {}
    last = {}
    buy_order = Order("BUY", "FB", "MKT", None, 5)
    sell_order = Order("SELL", "FB", "LMT", 20.00, 10)
    sell["FB"] = [sell_order]
    
    market_buy(buy_order, sell, last)  
    
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
    buy_order = Order("BUY", "FB", "MKT", None, 5)
    buy_order_two = Order("BUY", "FB", "MKT", None, 10)
    
    market_buy(buy_order, sell, last)
    market_buy(buy_order_two, sell, last)
    
    assert buy_order.getRemaining() == 5
    assert buy_order_two.getRemaining() == 10
    assert buy_order.getPrice() == None
    assert buy_order_two.getPrice() == None
    

# Testing whenn a trader is trying to place a sell order, similar test cases to the above, 
# just that now the roles are switched

def test_sell_one_market_buy_one_limit():
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "MKT", None, 5)
    buy_order = Order("BUY", "FB", "LMT", 20.00, 10)
    buy["FB"] = [buy_order]
    
    market_sell(sell_order, buy, last)  
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5
    assert sell_order.getPrice() == 20

def test_sell_two_market_buy_none_limit():
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "MKT", None, 5)
    sell_order_two = Order("SELL", "FB", "MKT", None, 10)
    
    market_sell(sell_order, buy, last)  
    market_sell(sell_order_two, buy, last) 
    
    assert sell_order.getRemaining() == 5
    assert sell_order_two.getRemaining() == 10
    assert sell_order.getPrice() == None
    assert sell_order_two.getPrice() == None

def test_sell_two_market_sell_two_limit():
    """
    No transactions should have taken place as there are no buy orders and only sell market and limit orders
    """
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "MKT", None, 5)
    sell_order_two = Order("SELL", "FB", "MKT", None, 10)
    sell_order_three = Order("SELL", "FB", "LMT", 20.00, 5)
    sell_order_four = Order("SELL", "FB", "LMT", 30.00, 10)
    
    market_buy(sell_order, buy, last)  
    market_buy(sell_order_two, buy, last) 
    market_buy(sell_order_three, buy, last) 
    market_buy(sell_order_four, buy, last) 
    
    assert sell_order.getRemaining() == 5
    assert sell_order_two.getRemaining() == 10
    assert sell_order_three.getRemaining() == 5
    assert sell_order_four.getRemaining() == 10
    assert sell_order.getPrice() == None
    assert sell_order_two.getPrice() == None