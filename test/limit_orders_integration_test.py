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

def test_buy_one_limit_sell_one_market():
    """
    Purpose: Testing how a limit buy order reacts when a market sell order has already been placed
    Result: Buy order should be processed with 0 remaining units and a price of $20
    """
    sell = {}
    last = {}
    buy_order = Order("BUY", "FB", "LMT", 20.00, 5)
    sell_order = Order("SELL", "FB", "MKT", None, 10)
    sell["FB"] = [sell_order]
    
    limit_buy(buy_order, sell, last)  
    
    assert buy_order.getRemaining() == 0
    assert sell_order.getRemaining() == 5
    assert sell_order.getPrice() == 20

def test_buy_one_limit_sell_one_limit_where_buy_price_is_higher():
    """
    Purpose: Testing how a limit buy order reacts when a limit sell order has already been placed where the 
             buy order price is more than the sell order price
    Result: Buy order should be processed with 0 remaining units
    """
    sell = {}
    last = {}
    buy_order = Order("BUY", "FB", "LMT", 30.00, 5)
    sell_order = Order("SELL", "FB", "LMT", 20.00, 10)
    sell["FB"] = [sell_order]
    
    limit_buy(buy_order, sell, last)  
    
    assert buy_order.getRemaining() == 0
    assert sell_order.getRemaining() == 5

def test_buy_one_limit_sell_one_limit_where_buy_price_is_lower():
    """
    Purpose: Testing how a limit buy order reacts when a limit sell order has already been placed where the 
             buy order price is lower than the sell order price
    Result: Buy order should not be processed
    """
    sell = {}
    last = {}
    buy_order = Order("BUY", "FB", "LMT", 10.00, 5)
    sell_order = Order("SELL", "FB", "LMT", 20.00, 10)
    sell["FB"] = [sell_order]
    
    limit_buy(buy_order, sell, last)  
    
    assert buy_order.getRemaining() == 5
    assert sell_order.getRemaining() == 10
    

def test_buy_two_limit_sell_none():
    """
    Purpose: Testing how a 2 limit buy orders will react with no sell order
    Result: Buy orders will not be processed
    """
    sell = {}
    last = {}
    buy_order = Order("BUY", "FB", "LMT", 20.00, 5)
    buy_order_two = Order("BUY", "FB", "LMT", 30.00, 10)
    
    limit_buy(buy_order, sell, last)
    limit_buy(buy_order_two, sell, last)
    
    assert buy_order.getRemaining() == 5
    assert buy_order_two.getRemaining() == 10
    assert buy_order.getPrice() == 20
    assert buy_order_two.getPrice() == 30
    

# Testing when a trader is trying to place a sell order, similar test cases to the above, 
# just that now the roles are switched

def test_sell_one_limit_buy_one_market():
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "LMT", 20.00, 5)
    buy_order = Order("BUY", "FB", "MKT", None, 10)
    buy["FB"] = [buy_order]
    
    limit_sell(sell_order, buy, last)  
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5
    assert buy_order.getPrice() == 20

def test_sell_one_limit_buy_one_limit_where_buy_price_is_higher():
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "LMT", 10.00, 5)
    buy_order = Order("BUY", "FB", "LMT", 15.00, 10)
    buy["FB"] = [buy_order]
    
    limit_sell(sell_order, buy, last)  
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5

def test_sell_one_limit_buy_one_limit_where_buy_price_is_lower():
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "LMT", 20.00, 5)
    buy_order = Order("BUY", "FB", "LMT", 10.00, 10)
    buy["FB"] = [buy_order]
    
    limit_sell(sell_order, buy, last)  
    
    assert sell_order.getRemaining() == 5
    assert buy_order.getRemaining() == 10


def test_sell_two_limit_buy_none():
    
    buy = {}
    last = {}
    sell_order = Order("SELL", "FB", "LMT", 15, 5)
    sell_order_two = Order("SELL", "FB", "MKT", 16, 10)
    
    market_sell(sell_order, buy, last)  
    market_sell(sell_order_two, buy, last) 
    
    assert sell_order.getRemaining() == 5
    assert sell_order_two.getRemaining() == 10
    assert sell_order.getPrice() == 15
    assert sell_order_two.getPrice() == 16
