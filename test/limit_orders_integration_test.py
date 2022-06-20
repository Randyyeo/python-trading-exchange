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

def test_buy_one_limit_sell_one_market():
    """
    Purpose: Testing how a limit buy order reacts when a market sell order has already been placed
    Result: Buy order should be processed with 0 remaining units and a price of $20
    """
    sell = {}
    last = {}
    buy_order = Buy_Limit_Order("FB", 20.00, 5)
    sell_order = Sell_Market_Order("FB", 10)
    sell["FB"] = [sell_order]
    
    buy_order.execute(sell, last)  
    
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
    buy_order = Buy_Limit_Order("FB", 30.00, 5)
    sell_order = Sell_Limit_Order("FB", 20.00, 10)
    sell["FB"] = [sell_order]
    
    buy_order.execute(sell, last)  
    
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
    buy_order = Buy_Limit_Order("FB", 10.00, 5)
    sell_order = Sell_Limit_Order("FB", 20.00, 10)
    sell["FB"] = [sell_order]
    
    buy_order.execute(sell, last)  
    
    assert buy_order.getRemaining() == 5
    assert sell_order.getRemaining() == 10
    

def test_buy_two_limit_sell_none():
    """
    Purpose: Testing how a 2 limit buy orders will react with no sell order
    Result: Buy orders will not be processed
    """
    sell = {}
    last = {}
    buy_order = Buy_Limit_Order("FB", 20.00, 5)
    buy_order_two = Buy_Limit_Order("FB", 30.00, 10)
    
    buy_order.execute(sell, last)
    buy_order_two.execute(sell, last)
    
    assert buy_order.getRemaining() == 5
    assert buy_order_two.getRemaining() == 10
    assert buy_order.getPrice() == 20
    assert buy_order_two.getPrice() == 30
    

# Testing when a trader is trying to place a sell order, similar test cases to the above, 
# just that now the roles are switched

def test_sell_one_limit_buy_one_market():
    buy = {}
    last = {}
    sell_order = Sell_Limit_Order("FB", 20.00, 5)
    buy_order = Buy_Market_Order("FB", 10)
    buy["FB"] = [buy_order]
    
    sell_order.execute(buy, last)  
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5
    assert buy_order.getPrice() == 20

def test_sell_one_limit_buy_one_limit_where_buy_price_is_higher():
    buy = {}
    last = {}
    sell_order = Sell_Limit_Order("FB", 10.00, 5)
    buy_order = Buy_Limit_Order("FB", 15.00, 10)
    buy["FB"] = [buy_order]
    
    sell_order.execute(buy, last)
    
    assert sell_order.getRemaining() == 0
    assert buy_order.getRemaining() == 5

def test_sell_one_limit_buy_one_limit_where_buy_price_is_lower():
    buy = {}
    last = {}
    sell_order = Sell_Limit_Order("FB", 20.00, 5)
    buy_order = Buy_Limit_Order("FB", 10.00, 10)
    buy["FB"] = [buy_order]
    
    sell_order.execute(buy, last)  
    
    assert sell_order.getRemaining() == 5
    assert buy_order.getRemaining() == 10


def test_sell_two_limit_buy_none():
    
    buy = {}
    last = {}
    sell_order = Sell_Limit_Order("FB", 15, 5)
    sell_order_two = Sell_Limit_Order("FB", 16, 10)
    
    sell_order.execute(buy, last)  
    sell_order_two.execute(buy, last) 
    
    assert sell_order.getRemaining() == 5
    assert sell_order_two.getRemaining() == 10
    assert sell_order.getPrice() == 15
    assert sell_order_two.getPrice() == 16
